"""Opt-in Codex CLI installation smoke test using a disposable CODEX_HOME."""
import argparse
import json
import os
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def smoke(executable):
    version = json.loads((ROOT / "plugins/ai-dev-protocol/.codex-plugin/plugin.json").read_text(encoding="utf-8-sig"))["version"]
    with tempfile.TemporaryDirectory(prefix="codex-plugin-smoke-") as directory:
        isolated = Path(directory)
        env = os.environ.copy()
        env["CODEX_HOME"] = str(isolated)
        commands = [
            ["--version"],
            ["plugin", "marketplace", "add", str(ROOT), "--json"],
            ["plugin", "add", "ai-dev-protocol@langji-ai-marketplace", "--json"],
            ["plugin", "list", "--json"],
        ]
        evidence = []
        for args in commands:
            result = subprocess.run([executable, *args], cwd=isolated, env=env,
                                    capture_output=True, text=True, encoding="utf-8", timeout=60)
            evidence.append({"args": args, "exitCode": result.returncode,
                             "stdout": result.stdout, "stderr": result.stderr})
            if result.returncode:
                raise ValueError(json.dumps(evidence, ensure_ascii=False, indent=2))
        installed = []
        for manifest in isolated.rglob(".codex-plugin/plugin.json"):
            data = json.loads(manifest.read_text(encoding="utf-8-sig"))
            if data.get("name") == "ai-dev-protocol":
                installed.append((manifest.parent.parent, data))
        if len(installed) != 1:
            raise ValueError(f"Expected one cached plugin, found {len(installed)}")
        root, manifest = installed[0]
        skills = list((root / "skills").rglob("SKILL.md"))
        phases = list((root / "skills").rglob("PHASE.md"))
        if (manifest["version"] != version or len(skills) != 1 or len(phases) != 8
                or skills[0].parent.name != "ai-dev-protocol"):
            raise ValueError("Installed version/Router/phase discovery does not match release")
        if "ai-dev-protocol" not in evidence[-1]["stdout"]:
            raise ValueError("Installed plugin is missing from CLI listing")
        report = {"kind": "native-installation-smoke", "pluginVersion": version,
                  "publicSkills": 1, "internalPhases": 8, "passed": True,
                  "modelBehavior": "unverified", "evidence": evidence}
        def redact(value):
            if isinstance(value, list):
                return [redact(item) for item in value]
            if isinstance(value, dict):
                return {key: redact(item) for key, item in value.items()}
            if isinstance(value, str):
                for path, label in ((isolated, "<isolated-home>"), (isolated.parent, "<temp-root>"), (ROOT, "<marketplace-root>")):
                    for candidate in (str(path).replace("\\", "\\\\"), str(path), path.as_posix()):
                        value = value.replace(candidate, label)
            return value
        return json.dumps(redact(report), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--codex", required=True)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    try:
        report = smoke(args.codex)
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(report + "\n", encoding="utf-8")
        print(report)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        parser.exit(1, f"Installation smoke failed: {exc}\n")
