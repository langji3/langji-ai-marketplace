# Langji AI Marketplace MVP Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a distribution-only marketplace repository that exposes `ai-dev-protocol` as an installable Codex and Claude Code marketplace plugin and keeps a validated local snapshot for Codex, Claude Code, and Cursor.

**Architecture:** The repository has three layers: marketplace indexes, human-facing documentation, and a sync script that copies the validated plugin snapshot from `https://github.com/langji3/ai-dev-protocol.git` into `plugins/ai-dev-protocol`. The marketplace never authors plugin rules; it only republishes validated plugin assets. For local verification, the script can also read from an explicit local source path.

**Tech Stack:** Markdown, JSON, PowerShell

## Global Constraints

- Keep this repository distribution-only.
- Do not copy `.git/`, `.idea/`, `dist/`, or source-repository-only marketplace/build scripts.
- Snapshot content must include `.codex-plugin/`, `.claude-plugin/`, `skills/`, `adapters/`, `docs/`, `README.md`, and `CHANGELOG.md`.
- `catalog/plugins.json` must stay tool-agnostic.
- `.agents/plugins/marketplace.json` must remain the Codex marketplace entrypoint.
- `.claude-plugin/marketplace.json` must remain the Claude Code marketplace entrypoint.

---

### Task 1: Create Marketplace Metadata And Docs

**Files:**
- Create: `README.md`
- Create: `.gitignore`
- Create: `catalog/plugins.json`
- Create: `.agents/plugins/marketplace.json`
- Create: `.claude-plugin/marketplace.json`
- Create: `docs/install-codex.md`
- Create: `docs/install-claude-code.md`
- Create: `docs/install-cursor.md`
- Create: `docs/update-policy.md`
- Create: `docs/add-plugin-guide.md`

**Interfaces:**
- Consumes: `D:\project\ai-dev-protocol\.codex-plugin\plugin.json`, `D:\project\ai-dev-protocol\.claude-plugin\plugin.json`
- Produces: Marketplace metadata files that reference `plugins/ai-dev-protocol`

- [ ] **Step 1: Gather plugin metadata**

```powershell
Get-Content 'D:\project\ai-dev-protocol\.codex-plugin\plugin.json'
Get-Content 'D:\project\ai-dev-protocol\.claude-plugin\plugin.json'
```

- [ ] **Step 2: Create marketplace documentation and indexes**

```text
Write README.md, install docs, update policy, add-plugin guide, catalog/plugins.json, .agents/plugins/marketplace.json, and .claude-plugin/marketplace.json
```

- [ ] **Step 3: Verify metadata files exist**

Run: `Get-ChildItem README.md, .gitignore, catalog/plugins.json, .agents/plugins/marketplace.json, .claude-plugin/marketplace.json, docs`
Expected: all files exist

### Task 2: Implement Local Snapshot Sync Script

**Files:**
- Create: `scripts/sync-ai-dev-protocol.ps1`

**Interfaces:**
- Consumes: `https://github.com/langji3/ai-dev-protocol.git` or a local override path
- Produces: `plugins/ai-dev-protocol/`

- [ ] **Step 1: Write sync script with validated include list**

```powershell
param(
  [string]$RepositoryUrl = "https://github.com/langji3/ai-dev-protocol.git",
  [string]$SourceRef = "main",
  [string]$SourcePath = ""
)
```

- [ ] **Step 2: Add target cleanup, copy, and validation**

```powershell
Remove-Item -LiteralPath $TargetPluginRoot -Recurse -Force
Copy-Item -LiteralPath $SourceItemPath -Destination $DestinationPath -Recurse -Force
Test-Path -LiteralPath (Join-Path $TargetPluginRoot '.codex-plugin\plugin.json')
Test-Path -LiteralPath (Join-Path $TargetPluginRoot 'skills')
```

- [ ] **Step 3: Run script to verify snapshot sync**

Run: `powershell -ExecutionPolicy Bypass -File .\scripts\sync-ai-dev-protocol.ps1`
Expected: success message with synced version

### Task 3: Verify Snapshot Output

**Files:**
- Modify: `plugins/ai-dev-protocol/`

**Interfaces:**
- Consumes: `scripts/sync-ai-dev-protocol.ps1`
- Produces: validated distribution snapshot

- [ ] **Step 1: Inspect synced output**

Run: `Get-ChildItem .\plugins\ai-dev-protocol -Force`
Expected: `.codex-plugin`, `.claude-plugin`, `skills`, `adapters`, `docs`, `README.md`, `CHANGELOG.md`

- [ ] **Step 2: Inspect plugin manifest**

Run: `Get-Content .\plugins\ai-dev-protocol\.codex-plugin\plugin.json`
Expected: plugin name `ai-dev-protocol` and version `0.2.2`

- [ ] **Step 3: Inspect marketplace entry**

Run: `Get-Content .\.agents\plugins\marketplace.json`
Expected: plugin source path `./plugins/ai-dev-protocol`
