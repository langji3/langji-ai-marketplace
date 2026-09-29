"""Protect the separate code-simplifier release from partial updates."""

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_code_simplifier import validate  # noqa: E402


class CodeSimplifierReleaseTests(unittest.TestCase):
    def test_current_snapshot_and_indexes_agree(self):
        report = validate(ROOT)
        self.assertEqual(report["plugin"], "code-simplifier")
        self.assertEqual(report["files"], 8)

    def test_modified_skill_does_not_pass_provenance_check(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self._copy_release(Path(temp))
            skill = root / "plugins/code-simplifier/skills/code-simplifier/SKILL.md"
            skill.write_bytes(skill.read_bytes() + b"\nchanged without source update\n")
            with self.assertRaisesRegex(ValueError, "Snapshot differs"):
                validate(root)

    def test_stale_claude_version_does_not_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self._copy_release(Path(temp))
            path = root / ".claude-plugin/marketplace.json"
            index = json.loads(path.read_text(encoding="utf-8"))
            next(item for item in index["plugins"] if item["name"] == "code-simplifier")["version"] = "0.0.0"
            path.write_text(json.dumps(index), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Claude entry differs"):
                validate(root)

    def test_wrong_source_repository_does_not_pass(self):
        with tempfile.TemporaryDirectory() as temp:
            root = self._copy_release(Path(temp))
            path = root / "catalog/plugins.json"
            index = json.loads(path.read_text(encoding="utf-8"))
            next(item for item in index["plugins"] if item["name"] == "code-simplifier")["sourceRepository"] = "https://example.com/other"
            path.write_text(json.dumps(index), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Marketplace source repository differs"):
                validate(root)

    @staticmethod
    def _copy_release(root: Path) -> Path:
        shutil.copytree(ROOT / "plugins/code-simplifier", root / "plugins/code-simplifier")
        for rel in (
            ".agents/plugins/marketplace.json",
            ".claude-plugin/marketplace.json",
            "catalog/plugins.json",
            "catalog/releases/code-simplifier.json",
        ):
            target = root / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / rel, target)
        return root


if __name__ == "__main__":
    unittest.main()
