"""Windows path fixtures backed by actual filesystem aliases, not mocked resolution."""
import ctypes
import os
from pathlib import Path
import shutil
import subprocess


def short_path(test, path):
    if os.name != "nt":
        test.skipTest("Windows 8.3 aliases require Windows")
    from ctypes import wintypes
    path = Path(path).resolve(strict=True)
    api = ctypes.WinDLL("kernel32", use_last_error=True).GetShortPathNameW
    api.argtypes = (wintypes.LPCWSTR, wintypes.LPWSTR, wintypes.DWORD)
    api.restype = wintypes.DWORD
    length = api(str(path), None, 0)
    if not length:
        raise ctypes.WinError(ctypes.get_last_error())
    output = ctypes.create_unicode_buffer(length)
    written = api(str(path), output, length)
    if not written or written >= length:
        raise ctypes.WinError(ctypes.get_last_error())
    alias = Path(output.value)
    if alias == path:
        test.skipTest("Volume does not provide an 8.3 alias for this fixture")
    test.assertTrue(alias.samefile(path))
    return alias


def junction(test, link, target):
    if os.name != "nt":
        test.skipTest("Directory junctions require Windows")
    shell = shutil.which("powershell") or shutil.which("pwsh")
    if not shell:
        test.skipTest("PowerShell is unavailable for junction fixture")
    link, target = Path(link).absolute(), Path(target).resolve(strict=True)
    script = link.parent / "create-junction.ps1"
    script.write_text(
        "param([string]$LinkPath, [string]$TargetPath)\n"
        "$ErrorActionPreference = 'Stop'\n"
        "New-Item -ItemType Junction -Path $LinkPath -Target $TargetPath | Out-Null\n",
        encoding="utf-8")
    result = subprocess.run([shell, "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                             str(script), "-LinkPath", str(link), "-TargetPath", str(target)],
                            capture_output=True, text=True)
    if result.returncode:
        test.fail("Could not create junction fixture: " + result.stderr)
    test.addCleanup(link.rmdir)  # Remove only the link before TemporaryDirectory cleans its target.
    test.assertTrue(link.exists())
    return link
