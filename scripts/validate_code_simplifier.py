"""Check the code-simplifier snapshot, marketplace entries and source commit."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys


NAME = "code-simplifier"
FILES = {
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    "LICENSE",
    "NOTICE.md",
    "README.md",
    "scripts/validate.py",
    "skills/code-simplifier/SKILL.md",
    "tests/scenarios.md",
}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def digest(data: bytes) -> str:
    return hashlib.sha256(data.decode("utf-8-sig").replace("\r\n", "\n").encode("utf-8")).hexdigest()


def one_entry(path: Path) -> dict:
    entries = [item for item in read_json(path)["plugins"] if item.get("name") == NAME]
    if len(entries) != 1:
        raise ValueError(f"Expected one {NAME} entry in {path}")
    return entries[0]


def validate(root: Path, source: Path | None = None) -> dict:
    plugin = root / "plugins" / NAME
    record = read_json(root / "catalog" / "releases" / f"{NAME}.json")
    if (record.get("plugin") != NAME or record.get("sourceProject") != NAME
            or record.get("schemaVersion") != 1):
        raise ValueError("Invalid code-simplifier provenance identity")
    commit = record.get("sourceCommit", "")
    if not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("Expected a full source commit")
    if record.get("hashAlgorithm") != "sha256-text-lf-utf8-v1":
        raise ValueError("Unknown hash algorithm")
    repository = record.get("sourceRepository")
    if repository != "https://github.com/langji3/code-simplifier":
        raise ValueError("Unexpected source repository")
    actual_paths = set()
    for path in plugin.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Linked release asset: {path}")
        if path.is_file():
            actual_paths.add(path.relative_to(plugin).as_posix())
    if actual_paths != FILES:
        raise ValueError(f"Unexpected snapshot files: {sorted(actual_paths ^ FILES)}")
    actual = {rel: digest((plugin / rel).read_bytes()) for rel in sorted(FILES)}
    if record.get("files") != actual:
        raise ValueError("Snapshot differs from recorded source contents")

    report = subprocess.run(
        [sys.executable, str(plugin / "scripts/validate.py"), str(plugin)],
        capture_output=True, text=True, encoding="utf-8", check=False,
    )
    if report.returncode:
        raise ValueError(f"Bundled plugin validation failed: {report.stderr.strip()}")
    version = json.loads(report.stdout)["version"]
    if record.get("version") != version:
        raise ValueError("Recorded version differs from snapshot")
    for rel in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
        if read_json(plugin / rel).get("repository") != repository:
            raise ValueError(f"Plugin source repository differs: {rel}")
    codex = one_entry(root / ".agents/plugins/marketplace.json")
    if codex.get("source") != {"source": "local", "path": f"./plugins/{NAME}"}:
        raise ValueError("Codex source path differs")
    if codex.get("policy") != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
        raise ValueError("Codex installation policy differs")
    claude = one_entry(root / ".claude-plugin/marketplace.json")
    catalog = one_entry(root / "catalog/plugins.json")
    if claude.get("source") != f"./plugins/{NAME}" or claude.get("version") != version:
        raise ValueError("Claude entry differs from snapshot")
    if catalog.get("version") != version or catalog.get("sourceProject") != NAME:
        raise ValueError("Catalog entry differs from source")
    if claude.get("repository") != repository or catalog.get("sourceRepository") != repository:
        raise ValueError("Marketplace source repository differs")

    if source is not None:
        source = source.resolve()
        origin = subprocess.run(
            ["git", "-C", str(source), "remote", "get-url", "origin"],
            capture_output=True, text=True, encoding="utf-8", check=True,
        ).stdout.strip()
        if origin.removesuffix(".git").rstrip("/") != repository:
            raise ValueError("Actual source origin differs from provenance")
        for rel in FILES:
            blob = subprocess.run(
                ["git", "-C", str(source), "show", f"{commit}:{rel}"],
                capture_output=True, check=True,
            ).stdout
            if digest(blob) != actual[rel]:
                raise ValueError(f"Source commit differs from snapshot: {rel}")
    return {"plugin": NAME, "version": version, "sourceCommit": commit, "files": len(actual)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--source-path", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(validate(args.root, args.source_path), ensure_ascii=False, indent=2))
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"Code Simplifier validation failed: {exc}\n")
