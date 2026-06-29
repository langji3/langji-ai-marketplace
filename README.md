# Langji AI Marketplace

Langji AI Marketplace is a team plugin marketplace for AI-assisted development tools.

Langji AI Marketplace 是团队内部 AI 工具插件市场，用于统一分发 Codex、Claude Code、Cursor 等工具可复用的 AI workflow 插件。

## Project Positioning

- This repository is a distribution marketplace, not the source of workflow rules.
- Plugin source code stays in independent repositories such as `langji3/ai-dev-protocol`.
- This repository stores validated release snapshots plus marketplace indexes.
- The marketplace structure supports multiple plugins instead of coupling everything to one plugin.

## Current Plugin List

| Plugin | Version | Category | Supported Tools | Source Repository |
| --- | --- | --- | --- | --- |
| AI Dev Protocol | 0.2.1 | Coding | Codex, Claude Code, Cursor | `https://github.com/langji3/ai-dev-protocol` |

The snapshot currently distributed by this marketplace lives in `plugins/ai-dev-protocol/`.

## Install

### Codex

1. Open the Codex plugin marketplace page.
2. Choose to add a plugin marketplace.
3. Enter this repository as the marketplace source.
4. Install `AI Dev Protocol` from `Langji AI Marketplace`.
5. Open a new Codex thread and confirm the plugin skills load correctly.

Detailed guide: `docs/install-codex.md`

### Claude Code

Claude Code currently reads the plugin snapshot from `plugins/ai-dev-protocol/`, especially `.claude-plugin/plugin.json` and `adapters/claude-code/`.

Detailed guide: `docs/install-claude-code.md`

### Cursor

Copy `plugins/ai-dev-protocol/adapters/cursor/ai-dev-protocol.mdc` into the target project's `.cursor/rules/`.

Detailed guide: `docs/install-cursor.md`

## Marketplace Layout

```text
langji-ai-marketplace/
  README.md
  .gitignore
  catalog/
    plugins.json
  .agents/
    plugins/
      marketplace.json
  plugins/
    ai-dev-protocol/
      .codex-plugin/
      .claude-plugin/
      skills/
      adapters/
      docs/
      README.md
      CHANGELOG.md
  docs/
    install-codex.md
    install-claude-code.md
    install-cursor.md
    update-policy.md
    add-plugin-guide.md
  scripts/
    sync-ai-dev-protocol.ps1
```

## Maintenance Flow

1. Update the source plugin in its own repository.
2. Validate the plugin behavior there.
3. Run `scripts/sync-ai-dev-protocol.ps1` in this marketplace repository.
4. Review the updated snapshot under `plugins/ai-dev-protocol/`.
5. Update the marketplace catalog if plugin metadata changed.
6. Publish or share the marketplace repository revision with the team.

The detailed snapshot policy is documented in `docs/update-policy.md`.

The sync script defaults to the source repository URL:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-ai-dev-protocol.ps1
```

For local development or offline verification, you can override the source path:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-ai-dev-protocol.ps1 -SourcePath ..\ai-dev-protocol
```

## Relationship To Source Repositories

- `ai-dev-protocol` remains the source-of-truth repository for workflow rules, skill content, adapters, and plugin metadata.
- This marketplace does not rewrite business rules or invent a second source of plugin logic.
- The local `plugins/ai-dev-protocol/` directory is a validated distribution snapshot refreshed from the source repository, not a full mirror of the source repository.
- Excluded items such as `.git/`, `.idea/`, `dist/`, and source-repository-only scripts stay out of the marketplace snapshot.

## Adding More Plugins

This repository is intentionally multi-plugin friendly:

- Add a new plugin under `plugins/<plugin-name>/`
- Register it in `catalog/plugins.json`
- Add it to `.agents/plugins/marketplace.json`
- Document installation and update rules as needed

See `docs/add-plugin-guide.md` for the checklist.
