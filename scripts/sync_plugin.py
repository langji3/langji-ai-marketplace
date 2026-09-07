"""Publish an immutable Git snapshot with rollback and explicit interrupted-run recovery."""
import argparse
from contextlib import contextmanager
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile
import tempfile

from release_support import (NAME, INDEXES, RECORD, allowed, inventory, json_read, json_bytes,
                             sha, single_plugin, validate_package, validate_marketplace, checked_path)


def git(args, cwd=None, binary=False, http_version="HTTP/1.1"):
    command = ["git"]
    if cwd:
        command += ["-c", f"safe.directory={Path(cwd).resolve()}"]
    command += ["-c", f"http.version={http_version}", *args]
    proc = subprocess.run(command, cwd=cwd, capture_output=True)
    if proc.returncode:
        # Do not echo repository URLs or credential-bearing command arguments.
        raise ValueError(f"Git {args[0]} failed (exit {proc.returncode}); check repository access and ref")
    return proc.stdout if binary else proc.stdout.decode("utf-8").strip()


def inside(root, path):
    root, path = checked_path(root, "transaction root"), checked_path(path, "transaction path")
    if not path.is_relative_to(root) or path == root:
        raise ValueError(f"Unsafe transaction path: {path}")
    return path


def separate(a, b):
    a, b = Path(a).resolve(), Path(b).resolve()
    if a == b or a.is_relative_to(b) or b.is_relative_to(a):
        raise ValueError("Source/cache and publication paths overlap")


def atomic_write(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp = tempfile.mkstemp(prefix=".release-", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def pid_alive(pid):
    if os.name == "nt":
        import ctypes
        from ctypes import wintypes
        api = ctypes.WinDLL("kernel32", use_last_error=True)
        api.OpenProcess.argtypes = (wintypes.DWORD, wintypes.BOOL, wintypes.DWORD)
        api.OpenProcess.restype = wintypes.HANDLE
        api.GetExitCodeProcess.argtypes = (wintypes.HANDLE, ctypes.POINTER(wintypes.DWORD))
        api.GetExitCodeProcess.restype = wintypes.BOOL
        api.CloseHandle.argtypes = (wintypes.HANDLE,)
        api.CloseHandle.restype = wintypes.BOOL
        handle = api.OpenProcess(0x1000, False, pid)
        if not handle:
            return ctypes.get_last_error() == 5  # access denied: assume alive
        code = wintypes.DWORD()
        try:
            if not api.GetExitCodeProcess(handle, ctypes.byref(code)):
                return True
            return code.value == 259
        finally:
            api.CloseHandle(handle)
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


@contextmanager
def lock(root, recover=False):
    path = inside(root, root / "tmp/release-sync.lock")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and recover:
        try:
            owner = json_read(path)
            if not pid_alive(int(owner["pid"])):
                path.unlink()
        except (ValueError, KeyError, OSError):
            raise ValueError("Unreadable lock; inspect it before manual recovery")
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL)
    except FileExistsError:
        raise ValueError("Another sync owns the lock; use --recover only after it has stopped")
    with os.fdopen(fd, "w", encoding="utf-8") as stream:
        json.dump({"pid": os.getpid()}, stream)
    try:
        yield
    finally:
        path.unlink(missing_ok=True)


def resolve_source(root, source_path, repository_url, ref, cache_path, http_version):
    target = root / "plugins" / NAME
    inside(root, target)
    if source_path:
        source = checked_path(source_path, "source root")
        separate(source, target)
        separate(source, root / "tmp")
        if git(["rev-parse", "--show-toplevel"], source) != str(source).replace("\\", "/"):
            # Git can return native separators on some hosts.
            if Path(git(["rev-parse", "--show-toplevel"], source)).resolve() != source:
                raise ValueError("SourcePath must be a Git repository root")
        if git(["status", "--porcelain", "--untracked-files=no"], source):
            raise ValueError("Source has uncommitted tracked changes; commit before publishing")
        return source
    cache = checked_path(cache_path, "cache") if cache_path else root / "tmp/source-cache/ai-dev-protocol.git"
    inside(root / "tmp", cache)
    separate(cache, target)
    if cache.exists():
        if git(["rev-parse", "--is-bare-repository"], cache) != "true":
            raise ValueError("Cache must be an owned bare Git repository; choose a fresh CachePath")
    else:
        cache.mkdir(parents=True)
        git(["init", "--bare"], cache)
    git(["fetch", "--no-tags", repository_url, ref], cache, http_version=http_version)
    return cache


def export_source(source, ref, output, expected_commit=None, remote=False):
    commit = git(["rev-parse", "--verify", ("FETCH_HEAD" if remote else ref) + "^{commit}"], source)
    if expected_commit and commit != expected_commit:
        raise ValueError("Resolved source commit differs from --expected-commit")
    data = git(["archive", "--format=tar", commit], source, binary=True)
    with tarfile.open(fileobj=io.BytesIO(data)) as archive:
        for member in archive.getmembers():
            parts = Path(member.name).parts
            if member.name.startswith("/") or ".." in parts:
                raise ValueError("Unsafe Git archive path")
            if not allowed(member.name) or member.isdir():
                continue
            if not member.isfile():
                raise ValueError(f"Only regular Git release files are supported: {member.name}")
            target = inside(output, output / member.name)
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.extractfile(member) as stream, target.open("wb") as dest:
                shutil.copyfileobj(stream, dest)
    return commit


def state_digest(path):
    return sha(path.read_bytes()) if path.is_file() else None


def rollback(root):
    tx = inside(root, root / "tmp/release-transaction")
    journal_path = tx / "journal.json"
    if not journal_path.exists():
        # Preparation has no publication side effects.
        if tx.exists():
            shutil.rmtree(tx)
        return
    state = json_read(journal_path)
    target = inside(root, root / "plugins" / NAME)
    # Refuse to overwrite edits made after an interrupted run.
    current = inventory(target) if target.exists() else None
    if current not in (state["oldPlugin"], state["newPlugin"], None):
        raise ValueError("Snapshot changed since interruption; preserve transaction and inspect manually")
    for rel, entry in state["indexes"].items():
        if rel not in (*INDEXES, RECORD):
            raise ValueError("Unexpected journal index path")
        path = inside(root, root / rel)
        if state_digest(path) not in (entry["oldHash"], entry["newHash"]):
            raise ValueError(f"{rel} changed since interruption; preserve transaction")
    backup = tx / "old-plugin"
    if backup.exists() and inventory(backup) != state["oldPlugin"]:
        raise ValueError("Old snapshot backup changed; manual recovery required")
    for rel, entry in state["indexes"].items():
        if entry["oldHash"] is not None:
            saved = inside(tx, tx / "old-indexes" / rel)
            if state_digest(saved) != entry["oldHash"]:
                raise ValueError(f"{rel} backup changed; manual recovery required")
    if backup.exists():
        if target.exists():
            shutil.rmtree(target)
        os.replace(backup, target)
    elif state["oldPlugin"] is None and target.exists():
        shutil.rmtree(target)
    elif state["oldPlugin"] is not None and current != state["oldPlugin"]:
        raise ValueError("Old snapshot backup is missing; manual recovery required")
    for rel, entry in state["indexes"].items():
        path = inside(root, root / rel)
        if entry["oldHash"] is None:
            path.unlink(missing_ok=True)
        else:
            atomic_write(path, (tx / "old-indexes" / rel).read_bytes())
    shutil.rmtree(tx)


def publish(root, stage, updates, checkpoint=lambda step: None):
    tx = inside(root, root / "tmp/release-transaction")
    target = inside(root, root / "plugins" / NAME)
    target.parent.mkdir(parents=True, exist_ok=True)
    state = {"oldPlugin": inventory(target) if target.exists() else None,
             "newPlugin": inventory(stage), "indexes": {}}
    for rel, data in updates.items():
        path = inside(root, root / rel)
        old = path.read_bytes() if path.exists() else None
        if old is not None:
            backup = tx / "old-indexes" / rel
            backup.parent.mkdir(parents=True, exist_ok=True)
            backup.write_bytes(old)
        state["indexes"][rel] = {"oldHash": sha(old) if old is not None else None, "newHash": sha(data)}
    atomic_write(tx / "journal.json", json_bytes(state))
    try:
        if target.exists():
            os.replace(target, tx / "old-plugin")
        checkpoint("old-backed-up")
        os.replace(stage, target)
        checkpoint("snapshot-installed")
        for rel, data in updates.items():
            atomic_write(root / rel, data)
            checkpoint(rel)
        validate_marketplace(root, pending=True)
    except Exception:
        rollback(root)
        raise
    # A crash after validation but before cleanup is recovered conservatively to the old release.
    shutil.rmtree(tx)


def sync(root, source_path=None, repository_url="https://github.com/langji3/ai-dev-protocol.git",
         ref="main", cache_path=None, expected_commit=None, dry_run=False,
         checkpoint=lambda step: None, http_version="HTTP/1.1"):
    root = checked_path(root, "marketplace root")
    with lock(root):
        tx = inside(root, root / "tmp/release-transaction")
        if tx.exists():
            raise ValueError("Interrupted release exists; run --recover before another sync")
        # Source/cache checks run before allocating a transaction or touching publication files.
        source = resolve_source(root, source_path, repository_url, ref, cache_path, http_version)
        tx.mkdir()
        stage = tx / "new-plugin"
        stage.mkdir()
        try:
            commit = export_source(source, ref, stage, expected_commit, remote=source_path is None)
            manifest, files = validate_package(stage)
            target = inside(root, root / "plugins" / NAME)
            if target.exists():
                old_manifest = json_read(target / ".codex-plugin/plugin.json")
                if old_manifest["version"] == manifest["version"] and inventory(target) != files:
                    raise ValueError("Content changed without a version bump")
            origin = json_read(stage / ".claude-plugin/plugin.json").get("repository")
            if (not isinstance(origin, str) or not origin.startswith("https://github.com/")
                    or "@" in origin or "?" in origin or "#" in origin):
                raise ValueError("Expected a credential-free GitHub source repository in plugin metadata")
            actual_origin = (git(["config", "--get", "remote.origin.url"], source)
                             if source_path else repository_url)
            if actual_origin.removesuffix(".git").rstrip("/") != origin.removesuffix(".git").rstrip("/"):
                raise ValueError("Actual Git source differs from plugin repository metadata")
            updates = {}
            for rel in INDEXES:
                index = json_read(root / rel)
                item = single_plugin(index)
                item["version"] = manifest["version"]
                item["description"] = manifest["description"]
                item["sourceRepository" if rel == "catalog/plugins.json" else "repository"] = origin
                updates[rel] = json_bytes(index)
            # Keep provenance free of machine-local paths and URL credentials.
            record = {"schemaVersion": 1, "plugin": NAME, "version": manifest["version"],
                      "sourceRepository": origin, "sourceCommit": commit,
                      "hashAlgorithm": "sha256-text-lf-utf8-v1", "files": files}
            updates[RECORD] = json_bytes(record)
            result = {"version": manifest["version"], "sourceCommit": commit,
                      "files": len(files), "dryRun": dry_run}
            if dry_run:
                shutil.rmtree(tx)
            else:
                publish(root, stage, updates, checkpoint)
            return result
        except Exception:
            if tx.exists() and not (tx / "journal.json").exists():
                shutil.rmtree(tx)
            raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--marketplace-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--source-path", type=Path)
    parser.add_argument("--repository-url", default="https://github.com/langji3/ai-dev-protocol.git")
    parser.add_argument("--source-ref", default="main")
    parser.add_argument("--cache-path", type=Path)
    parser.add_argument("--expected-commit")
    parser.add_argument("--git-http-version", default="HTTP/1.1")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--recover", action="store_true")
    args = parser.parse_args()
    try:
        if args.recover:
            root = checked_path(args.marketplace_root, "marketplace root")
            with lock(root, recover=True):
                rollback(root)
            print("Interrupted publication recovered; review Git status before syncing again.")
        else:
            print(json.dumps(sync(args.marketplace_root, args.source_path, args.repository_url,
                                  args.source_ref, args.cache_path, args.expected_commit, args.dry_run,
                                  http_version=args.git_http_version), indent=2))
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        parser.exit(1, f"Sync failed: {exc}\n")


if __name__ == "__main__":
    main()
