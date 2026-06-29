param(
    [string]$RepositoryUrl = "https://github.com/langji3/ai-dev-protocol.git",
    [string]$SourceRef = "main",
    [string]$SourcePath = "",
    [string]$CachePath = "",
    [string]$GitHttpVersion = "HTTP/1.1"
)

$ErrorActionPreference = "Stop"

function Resolve-AbsolutePath {
    param(
        [string]$BasePath,
        [string]$CandidatePath
    )

    if ([System.IO.Path]::IsPathRooted($CandidatePath)) {
        return [System.IO.Path]::GetFullPath($CandidatePath)
    }

    return [System.IO.Path]::GetFullPath((Join-Path $BasePath $CandidatePath))
}

function Format-ProcessArgument {
    param(
        [string]$Argument
    )

    if ($Argument -notmatch '[\s"]') {
        return $Argument
    }

    $escaped = $Argument -replace '(\\*)"', '$1$1\"'
    $escaped = $escaped -replace '(\\+)$', '$1$1'
    return '"' + $escaped + '"'
}

function ConvertTo-ProcessArgumentString {
    param(
        [string[]]$Arguments
    )

    return (($Arguments | ForEach-Object { Format-ProcessArgument -Argument $_ }) -join " ")
}

function Invoke-Git {
    param(
        [string[]]$Arguments,
        [string]$WorkingDirectory = $null,
        [string]$HttpVersion = ""
    )

    try {
        $processStartInfo = New-Object System.Diagnostics.ProcessStartInfo
        $processStartInfo.FileName = "git"
        $effectiveArguments = @()
        if ($HttpVersion) {
            $effectiveArguments += @("-c", "http.version=$HttpVersion")
        }
        $effectiveArguments += $Arguments

        $processStartInfo.Arguments = ConvertTo-ProcessArgumentString -Arguments $effectiveArguments
        $processStartInfo.UseShellExecute = $false
        $processStartInfo.RedirectStandardOutput = $true
        $processStartInfo.RedirectStandardError = $true
        $processStartInfo.CreateNoWindow = $true

        if ($WorkingDirectory) {
            $processStartInfo.WorkingDirectory = $WorkingDirectory
        }

        $process = New-Object System.Diagnostics.Process
        $process.StartInfo = $processStartInfo

        $null = $process.Start()
        $stdout = [string]$process.StandardOutput.ReadToEnd()
        $stderr = [string]$process.StandardError.ReadToEnd()
        $process.WaitForExit()

        $stdoutText = if ([string]::IsNullOrEmpty($stdout)) { "" } else { $stdout.TrimEnd() }
        $stderrText = if ([string]::IsNullOrEmpty($stderr)) { "" } else { $stderr.TrimEnd() }
        $combinedOutput = @($stdoutText, $stderrText) | Where-Object { $_ -ne "" }

        if ($process.ExitCode -ne 0) {
            $renderedArguments = $effectiveArguments -join " "
            $message = ($combinedOutput -join [Environment]::NewLine).Trim()
            throw "Git command failed: git $renderedArguments`n$message"
        }

        return $combinedOutput
    } finally {
        if ($process) {
            $process.Dispose()
        }
    }
}

function Get-SourceRoot {
    param(
        [string]$RepoRoot,
        [string]$ExplicitSourcePath,
        [string]$RepoUrl,
        [string]$RefName,
        [string]$ExplicitCachePath,
        [string]$HttpVersion
    )

    if ($ExplicitSourcePath) {
        return Resolve-AbsolutePath -BasePath $RepoRoot -CandidatePath $ExplicitSourcePath
    }

    $resolvedCacheRoot = if ($ExplicitCachePath) {
        Resolve-AbsolutePath -BasePath $RepoRoot -CandidatePath $ExplicitCachePath
    } else {
        Join-Path $RepoRoot "tmp\source-cache\ai-dev-protocol"
    }

    if (-not (Test-Path -LiteralPath $resolvedCacheRoot)) {
        New-Item -ItemType Directory -Path $resolvedCacheRoot -Force | Out-Null
    }

    $gitDir = Join-Path $resolvedCacheRoot ".git"
    if (-not (Test-Path -LiteralPath $gitDir -PathType Container)) {
        Invoke-Git -Arguments @("clone", $RepoUrl, $resolvedCacheRoot) -HttpVersion $HttpVersion
    }

    Invoke-Git -WorkingDirectory $resolvedCacheRoot -Arguments @("remote", "set-url", "origin", $RepoUrl) -HttpVersion $HttpVersion | Out-Null
    Invoke-Git -WorkingDirectory $resolvedCacheRoot -Arguments @("fetch", "--tags", "--prune", "origin", $RefName) -HttpVersion $HttpVersion | Out-Null
    Invoke-Git -WorkingDirectory $resolvedCacheRoot -Arguments @("checkout", "--force", "FETCH_HEAD") -HttpVersion $HttpVersion | Out-Null

    return $resolvedCacheRoot
}

function Assert-PathWithinRoot {
    param(
        [string]$RootPath,
        [string]$TargetPath
    )

    $normalizedRoot = [System.IO.Path]::GetFullPath($RootPath).TrimEnd('\') + '\'
    $normalizedTarget = [System.IO.Path]::GetFullPath($TargetPath).TrimEnd('\')

    if (-not $normalizedTarget.StartsWith($normalizedRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Target path '$normalizedTarget' is outside the repository root '$normalizedRoot'."
    }
}

$repoRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot ".."))
$targetPluginsRoot = Join-Path $repoRoot "plugins"
$targetPluginRoot = Join-Path $targetPluginsRoot "ai-dev-protocol"

Assert-PathWithinRoot -RootPath $repoRoot -TargetPath $targetPluginRoot

$resolvedSourceRoot = Get-SourceRoot `
    -RepoRoot $repoRoot `
    -ExplicitSourcePath $SourcePath `
    -RepoUrl $RepositoryUrl `
    -RefName $SourceRef `
    -ExplicitCachePath $CachePath `
    -HttpVersion $GitHttpVersion

if (-not (Test-Path -LiteralPath $resolvedSourceRoot -PathType Container)) {
    throw "Source plugin repository not found: $resolvedSourceRoot"
}

$requiredItems = @(
    ".codex-plugin",
    ".claude-plugin",
    "skills",
    "adapters",
    "docs",
    "README.md",
    "CHANGELOG.md"
)

foreach ($item in $requiredItems) {
    $sourceItemPath = Join-Path $resolvedSourceRoot $item
    if (-not (Test-Path -LiteralPath $sourceItemPath)) {
        throw "Required source item is missing: $sourceItemPath"
    }
}

if (-not (Test-Path -LiteralPath $targetPluginsRoot -PathType Container)) {
    New-Item -ItemType Directory -Path $targetPluginsRoot | Out-Null
}

if (Test-Path -LiteralPath $targetPluginRoot) {
    Remove-Item -LiteralPath $targetPluginRoot -Recurse -Force
}

New-Item -ItemType Directory -Path $targetPluginRoot | Out-Null

foreach ($item in $requiredItems) {
    $sourceItemPath = Join-Path $resolvedSourceRoot $item
    $destinationPath = Join-Path $targetPluginRoot $item
    Copy-Item -LiteralPath $sourceItemPath -Destination $destinationPath -Recurse -Force
}

$manifestPath = Join-Path $targetPluginRoot ".codex-plugin\plugin.json"
$skillsPath = Join-Path $targetPluginRoot "skills"

if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) {
    throw "Synced plugin manifest is missing: $manifestPath"
}

if (-not (Test-Path -LiteralPath $skillsPath -PathType Container)) {
    throw "Synced skills directory is missing: $skillsPath"
}

$manifest = Get-Content -LiteralPath $manifestPath -Raw | ConvertFrom-Json

$sourceDescription = if ($SourcePath) { $resolvedSourceRoot } else { "$RepositoryUrl@$SourceRef" }
Write-Host ("Synced ai-dev-protocol snapshot version {0} from {1} to {2}" -f $manifest.version, $sourceDescription, $targetPluginRoot)
