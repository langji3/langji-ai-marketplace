"""Isolated release transactions; no network, user cache, or real repository mutation."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from release_support import NAME, INDEXES, RECORD, inventory, json_bytes, json_read, validate_marketplace
from sync_plugin import git, inside, lock, pid_alive, rollback, sync
from path_fixtures import short_path, junction


class SimulatedCrash(BaseException):
    pass


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.market = self.base / "market"
        self.source = self.base / "source"
        self.market.mkdir()
        shutil.copytree(ROOT / "plugins" / NAME, self.market / "plugins" / NAME,
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        shutil.copytree(self.market / "plugins" / NAME, self.source)
        for rel in (*INDEXES, RECORD, ".agents/plugins/marketplace.json"):
            dest = self.market / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / rel, dest)
        git(["init", "-b", "main"], self.source)
        git(["config", "user.name", "Release Fixture"], self.source)
        git(["config", "user.email", "fixture@example.invalid"], self.source)
        origin = json_read(self.source / ".claude-plugin/plugin.json")["repository"]
        git(["remote", "add", "origin", origin], self.source)
        self.commit()
        self.before = self.state()

    def commit(self):
        git(["add", "."], self.source)
        git(["commit", "--allow-empty", "-m", "fixture"], self.source)
        return git(["rev-parse", "HEAD"], self.source)

    def state(self):
        target = self.market / "plugins" / NAME
        return (inventory(target) if target.exists() else None,
                {rel: (self.market / rel).read_bytes() if (self.market / rel).exists() else None
                 for rel in (*INDEXES, RECORD)})

    def publish(self, **kwargs):
        return sync(self.market, source_path=self.source, ref="HEAD", **kwargs)

    def bump(self):
        old = json_read(self.source / ".codex-plugin/plugin.json")["version"]
        new = "99.0.0"
        for rel in (".codex-plugin/plugin.json", ".claude-plugin/plugin.json"):
            data = json_read(self.source / rel)
            data["version"] = new
            (self.source / rel).write_bytes(json_bytes(data))
        path = self.source / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")
        path = self.source / "CHANGELOG.md"
        path.write_text("## [99.0.0] - fixture\n\n" + path.read_text(encoding="utf-8"), encoding="utf-8")
        return self.commit()

    def test_exact_commit_and_idempotent_publication(self):
        commit = self.bump()
        result = self.publish(expected_commit=commit)
        self.assertEqual(commit, result["sourceCommit"])
        self.assertEqual("99.0.0", validate_marketplace(self.market)["version"])
        first = self.state()
        self.publish(expected_commit=commit)
        self.assertEqual(first, self.state())
        self.assertFalse((self.market / "tmp/release-transaction").exists())

    def test_dry_run_does_not_publish(self):
        self.bump()
        self.assertTrue(self.publish(dry_run=True)["dryRun"])
        self.assertEqual(self.before, self.state())

    def test_source_untracked_artifact_is_not_exported(self):
        (self.source / "docs/stray.md").write_text("untracked private scratch")
        (self.source / "scratch.txt").write_text("private scratch")
        self.publish()
        self.assertFalse((self.market / "plugins" / NAME / "docs/stray.md").exists())
        self.assertFalse((self.market / "plugins" / NAME / "scratch.txt").exists())

    def test_dirty_source_is_rejected(self):
        with (self.source / "README.md").open("a", encoding="utf-8") as stream:
            stream.write("\nuncommitted")
        with self.assertRaisesRegex(ValueError, "uncommitted"):
            self.publish()
        self.assertEqual(self.before, self.state())

    def test_same_version_changed_content_is_rejected(self):
        with (self.source / "README.md").open("a", encoding="utf-8") as stream:
            stream.write("\nchanged")
        self.commit()
        with self.assertRaisesRegex(ValueError, "version bump"):
            self.publish()
        self.assertEqual(self.before, self.state())

    def test_invalid_manifest_never_replaces_old_snapshot(self):
        (self.source / ".claude-plugin/plugin.json").write_text("{invalid")
        self.commit()
        with self.assertRaises(ValueError):
            self.publish()
        self.assertEqual(self.before, self.state())

    def test_unexpected_commit_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "expected-commit"):
            self.publish(expected_commit="0" * 40)
        self.assertEqual(self.before, self.state())

    def test_actual_origin_must_match_release_metadata(self):
        git(["remote", "set-url", "origin", "https://github.com/example/wrong.git"], self.source)
        with self.assertRaisesRegex(ValueError, "Actual Git source"):
            self.publish()
        self.assertEqual(self.before, self.state())

    def test_source_and_cache_overlap_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            sync(self.market, source_path=self.market / "plugins" / NAME)
        with self.assertRaisesRegex(ValueError, "Unsafe transaction path"):
            sync(self.market, cache_path=self.market / "plugins" / NAME)
        with self.assertRaisesRegex(ValueError, "Unsafe transaction path"):
            inside(self.market, self.market)
        self.assertEqual(self.before, self.state())

    def test_copy_failure_leaves_old_release_and_cleans_preparation(self):
        with patch("sync_plugin.shutil.copyfileobj", side_effect=OSError("copy failure")):
            with self.assertRaisesRegex(OSError, "copy failure"):
                self.publish()
        self.assertEqual(self.before, self.state())
        self.assertFalse((self.market / "tmp/release-transaction").exists())

    def test_every_publication_checkpoint_rolls_back_on_exception(self):
        self.bump()
        for fail_at in ("old-backed-up", "snapshot-installed", *INDEXES, RECORD):
            with self.subTest(fail_at=fail_at):
                def fail(step):
                    if step == fail_at:
                        raise OSError("injected replacement/metadata failure")
                with self.assertRaisesRegex(OSError, "injected"):
                    self.publish(checkpoint=fail)
                self.assertEqual(self.before, self.state())
                self.assertFalse((self.market / "tmp/release-transaction").exists())

    def crash(self):
        self.bump()
        def fail(step):
            if step == "catalog/plugins.json":
                raise SimulatedCrash()
        with self.assertRaises(SimulatedCrash):
            self.publish(checkpoint=fail)

    def test_interrupted_transaction_blocks_sync_and_recovers(self):
        self.crash()
        with self.assertRaisesRegex(ValueError, "Interrupted release"):
            self.publish()
        with self.assertRaisesRegex(ValueError, "Interrupted release"):
            validate_marketplace(self.market)
        rollback(self.market)
        self.assertEqual(self.before, self.state())
        validate_marketplace(self.market)
        self.publish()

    def test_recovery_preserves_manual_edits_after_crash(self):
        self.crash()
        path = self.market / "plugins" / NAME / "README.md"
        path.write_text("manual edit after interruption", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Snapshot changed"):
            rollback(self.market)
        self.assertEqual("manual edit after interruption", path.read_text())

    def test_recovery_preserves_index_edits_after_crash(self):
        self.crash()
        path = self.market / "catalog/plugins.json"
        path.write_text("manual catalog edit")
        with self.assertRaisesRegex(ValueError, "changed since interruption"):
            rollback(self.market)
        self.assertEqual("manual catalog edit", path.read_text())

    def test_recovery_rejects_corrupted_backup_before_mutation(self):
        self.crash()
        path = self.market / "tmp/release-transaction/old-indexes/catalog/plugins.json"
        path.write_text("corrupted backup")
        current = self.state()
        with self.assertRaisesRegex(ValueError, "backup changed"):
            rollback(self.market)
        self.assertEqual(current, self.state())

    def test_active_process_lock_cannot_be_stolen(self):
        self.assertTrue(pid_alive(os.getpid()))
        with lock(self.market):
            with self.assertRaisesRegex(ValueError, "owns the lock"):
                with lock(self.market, recover=True):
                    self.fail("active lock was stolen")

    def test_missing_provenance_or_inconsistent_index_is_rejected(self):
        path = self.market / RECORD
        data = json_read(path)
        data["files"]["README.md"] = "0" * 64
        path.write_bytes(json_bytes(data))
        with self.assertRaisesRegex(ValueError, "differs from provenance"):
            validate_marketplace(self.market)

    def test_windows_short_paths_allow_sync_and_recovery(self):
        alias = short_path(self, self.market)
        source_alias = short_path(self, self.source)
        self.assertEqual(self.before[0], inventory(alias / "plugins" / NAME))
        self.assertEqual(self.market.resolve() / "tmp/alias-check", inside(self.market, alias / "tmp/alias-check"))
        sync(alias, source_path=source_alias, ref="HEAD")
        baseline = self.state()
        self.bump()
        def fail(step):
            if step == "catalog/plugins.json":
                raise SimulatedCrash()
        with self.assertRaises(SimulatedCrash):
            sync(alias, source_path=source_alias, ref="HEAD", checkpoint=fail)
        rollback(alias)
        self.assertEqual(baseline, self.state())
        validate_marketplace(alias)

    def test_junction_snapshot_is_rejected_without_touching_target(self):
        target = self.market / "plugins" / NAME
        outside = self.base / "outside-plugin"
        target.rename(outside)
        junction(self, target, outside)
        with self.assertRaisesRegex(ValueError, "Linked"):
            self.publish()
        with self.assertRaisesRegex(ValueError, "Linked"):
            inventory(target)
        self.assertEqual(self.before[0], inventory(outside))

    def test_junction_marketplace_root_is_rejected(self):
        alias = junction(self, self.base / "linked-market", self.market)
        with self.assertRaisesRegex(ValueError, "Linked"):
            sync(alias, source_path=self.source, ref="HEAD")
        with self.assertRaisesRegex(ValueError, "Linked"):
            validate_marketplace(alias)

    def run_wrapper(self, executable):
        if not shutil.which(executable):
            self.skipTest(f"{executable} is unavailable")
        shutil.copytree(ROOT / "scripts", self.market / "scripts",
                        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        result = subprocess.run(
            [executable, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
             str(self.market / "scripts/sync-ai-dev-protocol.ps1"),
             "-SourcePath", str(self.source), "-SourceRef", "HEAD",
             "-PythonExecutable", sys.executable, "-DryRun"],
            cwd=self.market, capture_output=True, text=True)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn('"dryRun": true', result.stdout)
        self.assertEqual(self.before, self.state())

    def test_powershell_7_entrypoint(self):
        self.run_wrapper("pwsh")

    @unittest.skipUnless(os.name == "nt", "Windows PowerShell 5.1 requires Windows")
    def test_windows_powershell_5_entrypoint(self):
        self.run_wrapper("powershell")


if __name__ == "__main__":
    unittest.main()
