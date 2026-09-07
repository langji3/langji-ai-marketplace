"""Independent marketplace checks. Python 3.11+, standard library only."""
import hashlib
import json
from pathlib import Path
import stat
import subprocess
import sys

NAME = "ai-dev-protocol"
DIRS = {".codex-plugin", ".claude-plugin", "skills", "adapters", "docs"}
FILES = {"README.md", "CHANGELOG.md", "scripts/validate_plugin.py", "scripts/build_bundle.py"}
TEXT = {".md", ".mdc", ".json", ".yaml", ".yml", ".py", ".ps1"}
INDEXES = ("catalog/plugins.json", ".claude-plugin/marketplace.json")
RECORD = "catalog/releases/ai-dev-protocol.json"


def json_read(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def allowed(name):
    parts = Path(name).parts
    return bool(parts) and (
        (parts[0] in DIRS and parts[:2] != ("docs", "plans"))
        or Path(name).as_posix() in FILES
    )


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


def inventory(root):
    root = checked_path(root)
    result = {}
    for path in sorted(root.rglob("*")):
        checked_path(path, "release asset")
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if not allowed(rel) or any(p in {".git", ".idea", "__pycache__"} for p in path.relative_to(root).parts):
            raise ValueError(f"Unexpected release file: {rel}")
        data = path.read_bytes()
        if path.suffix.lower() in TEXT:
            data = data.decode("utf-8-sig").replace("\r\n", "\n").encode("utf-8")
        result[rel] = sha(data)
    return result


def validate_package(root):
    root = checked_path(root)
    actual = inventory(root)
    codex = json_read(root / ".codex-plugin/plugin.json")
    claude = json_read(root / ".claude-plugin/plugin.json")
    if codex.get("name") != NAME or claude.get("name") != NAME:
        raise ValueError("Unexpected plugin identity")
    if not codex.get("version") or codex["version"] != claude.get("version"):
        raise ValueError("Plugin versions differ")
    if codex.get("skills") != "./skills/":
        raise ValueError("Unexpected skills path")
    # The committed first-party validator travels with the release for installation self-checks.
    proc = subprocess.run([sys.executable, str(root / "scripts/validate_plugin.py"), str(root), "--json"],
                          capture_output=True, text=True, encoding="utf-8")
    if proc.returncode:
        raise ValueError(f"Bundled validation failed: {proc.stderr.strip()}")
    report = json.loads(proc.stdout)
    if report.get("files") != actual or report.get("version") != codex["version"]:
        raise ValueError("Validator report differs from independent release inventory")
    return codex, actual


def single_plugin(index):
    matches = [p for p in index.get("plugins", []) if p.get("name") == NAME]
    if len(matches) != 1:
        raise ValueError("Marketplace must contain exactly one matching plugin entry")
    return matches[0]


def validate_marketplace(root, pending=False):
    root = checked_path(root, "marketplace root")
    if not pending and (root / "tmp/release-transaction").exists():
        raise ValueError("Interrupted release exists; run sync --recover before validation")
    manifest, actual = validate_package(root / "plugins" / NAME)
    for rel in INDEXES:
        entry = single_plugin(json_read(root / rel))
        if entry.get("version") != manifest["version"]:
            raise ValueError(f"{rel}: version differs from plugin")
    claude = single_plugin(json_read(root / INDEXES[1]))
    if claude.get("source") != f"./plugins/{NAME}":
        raise ValueError("Claude marketplace source path differs")
    codex = json_read(root / ".agents/plugins/marketplace.json")
    if codex.get("name") != "langji-ai-marketplace":
        raise ValueError("Unexpected marketplace identity")
    entry = single_plugin(codex)
    if entry.get("source") != {"source": "local", "path": f"./plugins/{NAME}"}:
        raise ValueError("Codex marketplace source path differs")
    if entry.get("policy", {}).get("installation") not in {"AVAILABLE", "NOT_AVAILABLE", "INSTALLED_BY_DEFAULT"}:
        raise ValueError("Invalid installation policy")
    if entry.get("policy", {}).get("authentication") not in {"ON_INSTALL", "ON_USE"}:
        raise ValueError("Invalid authentication policy")
    record = json_read(root / RECORD)
    source = record.get("sourceRepository")
    if (not isinstance(source, str) or not source.startswith("https://github.com/")
            or "@" in source or "?" in source or "#" in source):
        raise ValueError("Invalid release source repository")
    canonical = source.removesuffix(".git").rstrip("/")
    for rel, field in (("catalog/plugins.json", "sourceRepository"),
                       (".claude-plugin/marketplace.json", "repository")):
        value = single_plugin(json_read(root / rel)).get(field, "")
        if not isinstance(value, str) or value.removesuffix(".git").rstrip("/") != canonical:
            raise ValueError(f"{rel}: source repository differs from provenance")
    plugin_source = json_read(root / "plugins" / NAME / ".claude-plugin/plugin.json").get("repository")
    if not isinstance(plugin_source, str) or plugin_source.removesuffix(".git").rstrip("/") != canonical:
        raise ValueError("Plugin source repository differs from provenance")
    import re
    if record.get("schemaVersion") != 1 or not re.fullmatch(r"[0-9a-f]{40,64}", record.get("sourceCommit", "")):
        raise ValueError("Invalid provenance schema or source commit")
    if record.get("hashAlgorithm") != "sha256-text-lf-utf8-v1":
        raise ValueError("Unknown provenance hash algorithm")
    if record.get("version") != manifest["version"] or record.get("files") != actual:
        raise ValueError("Release differs from provenance")
    return {"version": manifest["version"], "sourceCommit": record["sourceCommit"], "files": len(actual)}
