"""Build a fresh, complete project integration bundle; never modifies an existing project."""
import argparse
import json
from pathlib import Path
import shutil
import sys

sys.dont_write_bytecode = True
from validate_plugin import NAME, checked_path, release_files, validate


def build(root, output):
    root, output = checked_path(root), checked_path(output, "bundle output")
    metadata = validate(root)
    if output.exists():
        raise ValueError(f"Output already exists; choose a fresh directory: {output}")
    if (root == output or root.is_relative_to(output)
            or (output.is_relative_to(root) and not output.is_relative_to(root / "dist"))):
        raise ValueError("Output must not overlap source assets")
    output.mkdir(parents=True)
    try:
        vendor = output / "vendor" / NAME
        for path in release_files(root):
            target = vendor / path.relative_to(root)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
        rule = output / ".cursor/rules/ai-dev-protocol.mdc"
        rule.parent.mkdir(parents=True)
        shutil.copyfile(root / "adapters/cursor/ai-dev-protocol.mdc", rule)
        for source, name in (
            ("adapters/codex/AGENTS.snippet.md", "AGENTS.md"),
            ("adapters/claude-code/CLAUDE.snippet.md", "CLAUDE.md"),
            ("adapters/generic/AI_DEV_PROTOCOL.md", "AI_DEV_PROTOCOL.md"),
        ):
            shutil.copyfile(root / source, output / name)
        (output / "bundle.json").write_text(json.dumps({
            "plugin": NAME, "version": metadata["version"], "root": f"vendor/{NAME}",
            "hashAlgorithm": metadata["hashAlgorithm"], "files": metadata["files"],
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        validate(vendor)
    except Exception:
        # This newly created output is owned entirely by this build.
        shutil.rmtree(output)
        raise
    return output


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        print(build(args.source, args.output))
    except (OSError, ValueError) as exc:
        parser.exit(1, f"Bundle failed: {exc}\n")
