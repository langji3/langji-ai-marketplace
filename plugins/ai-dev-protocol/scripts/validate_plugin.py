"""Offline validation and deterministic inventory for AI Dev Protocol (stdlib only)."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import stat
import sys

NAME = "ai-dev-protocol"
PHASES = {
    "ai-requirement-intake", "ai-branch-workflow", "ai-spec-writing",
    "ai-implementation-scope", "ai-commit-rules", "ai-merge-back",
    "ai-handoff", "ai-apifox-sync",
}
RELEASE_DIRS = (".codex-plugin", ".claude-plugin", "skills", "adapters", "docs")
RELEASE_FILES = ("README.md", "CHANGELOG.md", "scripts/validate_plugin.py", "scripts/build_bundle.py")
TEXT_SUFFIXES = {".md", ".mdc", ".json", ".yaml", ".yml", ".py", ".ps1"}
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def read_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def digest(path):
    data = Path(path).read_bytes()
    if Path(path).suffix.lower() in TEXT_SUFFIXES:
        data = data.decode("utf-8-sig").replace("\r\n", "\n").encode("utf-8")
    return hashlib.sha256(data).hexdigest()


def checked_path(path, kind="plugin root"):
    """Reject actual links before canonicalizing harmless Windows 8.3 aliases."""
    path = Path(path).absolute()
    for component in (path, *path.parents):
        try:
            info = component.lstat()
        except FileNotFoundError:
            continue
        if (stat.S_ISLNK(info.st_mode)
                or getattr(info, "st_file_attributes", 0) & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)):
            raise ValueError(f"Linked {kind} is not supported: {component}")
    return path.resolve()


def release_files(root):
    root = checked_path(root)
    selected = []
    for directory in RELEASE_DIRS:
        base = root / directory
        checked_path(base, "release directory")
        if not base.is_dir():
            raise ValueError(f"Missing release directory: {directory}")
        for path in base.rglob("*"):
            rel = path.relative_to(root)
            if rel.parts[:2] == ("docs", "plans"):
                continue
            checked_path(path, "release asset")
            if path.is_file():
                if any(x in {".git", "__pycache__", ".idea"} for x in rel.parts):
                    raise ValueError(f"Unexpected release artifact: {rel}")
                selected.append(path)
    for rel in RELEASE_FILES:
        path = root / rel
        checked_path(path, "release asset")
        if not path.is_file():
            raise ValueError(f"Missing or unsafe release asset: {rel}")
        selected.append(path)
    return sorted(selected, key=lambda p: p.relative_to(root).as_posix())


def inventory(root):
    root = checked_path(root)
    return {p.relative_to(root).as_posix(): digest(p) for p in release_files(root)}


def validate(root):
    root = checked_path(root)
    release = release_files(root)
    errors = []
    manifests = []
    for rel in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
        try:
            item = read_json(root / rel)
            manifests.append(item)
            if item.get("name") != NAME:
                errors.append(f"{rel}: name must be {NAME}")
            if not re.fullmatch(r"\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?", item.get("version", "")):
                errors.append(f"{rel}: expected a release semver without local cachebuster")
            if not isinstance(item.get("description"), str) or not item["description"].strip():
                errors.append(f"{rel}: description is required")
        except (OSError, ValueError, TypeError) as exc:
            errors.append(f"{rel}: {exc}")
    if len(manifests) == 2:
        if manifests[0].get("version") != manifests[1].get("version"):
            errors.append("Codex and Claude versions differ")
        if manifests[0].get("skills") != "./skills/":
            errors.append("Codex skills path must be ./skills/")
    skill = root / "skills" / NAME
    discovered = sorted(p.relative_to(root).as_posix() for p in (root / "skills").rglob("SKILL.md"))
    if discovered != [f"skills/{NAME}/SKILL.md"]:
        errors.append(f"Expected one public Router; found {discovered}")
    try:
        content = (skill / "SKILL.md").read_text(encoding="utf-8-sig")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
        if not match:
            errors.append("Router frontmatter is missing")
        else:
            fields = dict(re.findall(r"^(name|description):[ \t]*(.+)$", match[1], re.M))
            if fields.get("name", "").strip() != NAME or not fields.get("description", "").strip():
                errors.append("Router frontmatter requires matching name and nonempty description")
        ui = (skill / "agents/openai.yaml").read_text(encoding="utf-8-sig")
        if not re.search(r"^interface:\s*$", ui, re.M) or not re.search(r"^\s+default_prompt:.*\$ai-dev-protocol", ui, re.M):
            errors.append("Router UI metadata must reference $ai-dev-protocol in default_prompt")
    except OSError as exc:
        errors.append(str(exc))
    found = {p.parent.name for p in (skill / "phases").glob("*/PHASE.md")}
    if found != PHASES:
        errors.append(f"Expected eight phases; found {sorted(found)}")
    if manifests:
        version = manifests[0].get("version")
        readme = (root / "README.md").read_text(encoding="utf-8-sig")
        changelog = (root / "CHANGELOG.md").read_text(encoding="utf-8-sig")
        if f"`{version}`" not in readme:
            errors.append("README must state the current manifest version")
        latest = re.search(r"^## \[([^\]]+)\]", changelog, re.M)
        if not latest or latest[1] != version:
            errors.append("Latest CHANGELOG version must match manifests")
    for path in (p for p in release if p.suffix == ".md"):
        text = path.read_text(encoding="utf-8-sig")
        if path.name == "PHASE.md" and text.startswith("---"):
            errors.append(f"{path.relative_to(root)}: internal phase has frontmatter")
        for target in LINK.findall(text):
            target = target.strip().split(' "', 1)[0].strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(root) or not resolved.is_file():
                errors.append(f"{path.relative_to(root)}: unresolved/escaping link {target}")
    try:
        assets = inventory(root)
    except (OSError, ValueError) as exc:
        assets = {}
        errors.append(str(exc))
    if errors:
        raise ValueError("\n".join(errors))
    return {"name": NAME, "version": manifests[0]["version"], "publicSkills": discovered,
            "phaseCount": len(found), "hashAlgorithm": "sha256-text-lf-utf8-v1", "files": assets}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (ValueError, OSError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2) if args.json else
          f"Valid {result['name']} {result['version']}: one Router, {result['phaseCount']} phases, {len(result['files'])} release files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
