param(
    [string]$RepositoryUrl = "https://github.com/langji3/ai-dev-protocol.git",
    [string]$SourceRef = "main",
    [string]$SourcePath = "",
    [string]$CachePath = "",
    [string]$GitHttpVersion = "HTTP/1.1",
    [string]$ExpectedCommit = "",
    [string]$PythonExecutable = "python",
    [switch]$DryRun,
    [switch]$Recover
)
$ErrorActionPreference = "Stop"
$syncArguments = @(
    (Join-Path $PSScriptRoot "sync_plugin.py"),
    "--repository-url", $RepositoryUrl,
    "--source-ref", $SourceRef,
    "--git-http-version", $GitHttpVersion
)
if ($SourcePath) { $syncArguments += @("--source-path", $SourcePath) }
if ($CachePath) { $syncArguments += @("--cache-path", $CachePath) }
if ($ExpectedCommit) { $syncArguments += @("--expected-commit", $ExpectedCommit) }
if ($DryRun) { $syncArguments += "--dry-run" }
if ($Recover) { $syncArguments += "--recover" }
& $PythonExecutable @syncArguments
if ($LASTEXITCODE -ne 0) { throw "Plugin sync failed (exit $LASTEXITCODE)." }
