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
| AI Dev Protocol | 0.2.6 | Coding | Codex, Claude Code, Cursor | `https://github.com/langji3/ai-dev-protocol` |

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

Claude Code can add this repository as a plugin marketplace because the repository root now includes `.claude-plugin/marketplace.json`.

Recommended flow:

1. Run `/plugin marketplace add langji3/langji-ai-marketplace`
2. Run `/plugin install ai-dev-protocol@langji-ai-marketplace`
3. Run `/reload-plugins`

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
  .claude-plugin/
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
2. Bump the plugin version when the distributed plugin behavior changes.
3. Validate the plugin behavior in the source repository.
4. Run `scripts/sync-ai-dev-protocol.ps1` in this marketplace repository.
5. Review the updated snapshot under `plugins/ai-dev-protocol/`.
6. Update the marketplace catalog if plugin metadata changed.
7. Publish or share the marketplace repository revision with the team.

The detailed snapshot policy is documented in `docs/update-policy.md`.

The sync script defaults to the source repository URL:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-ai-dev-protocol.ps1
```

For local development or offline verification, you can override the source path:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\sync-ai-dev-protocol.ps1 -SourcePath ..\ai-dev-protocol
```

## Update Behavior By Tool

When this marketplace repository is updated, Codex and Claude Code do not consume the change in exactly the same way.

### Codex

- Codex reads the marketplace entry from `.agents/plugins/marketplace.json`.
- The marketplace entry points directly to `./plugins/ai-dev-protocol`.
- After the marketplace repository is refreshed, Codex will read the updated snapshot from this repository.
- In practice, team members should refresh the marketplace or reinstall/reload the plugin if they do not immediately see the latest snapshot.

### Claude Code

- Claude Code reads the marketplace entry from `.claude-plugin/marketplace.json`.
- Users add the marketplace, then install `ai-dev-protocol` from that marketplace into their local Claude Code plugin cache.
- Updating the marketplace repository alone does not guarantee that already-installed Claude Code plugins refresh automatically.
- Claude Code users should refresh the marketplace, update the plugin, and reload plugins in their current session.

Recommended Claude Code update flow:

```shell
/plugin marketplace update langji-ai-marketplace
/plugin update ai-dev-protocol@langji-ai-marketplace
/reload-plugins
```

Important: Claude Code update detection is version-sensitive. If the plugin content changes but `plugins/ai-dev-protocol/.claude-plugin/plugin.json` keeps the same `version`, users may not receive the new release as expected.

## Recommended Release Flow

Use this flow whenever you publish a new validated version of `ai-dev-protocol` through the marketplace:

1. Update `ai-dev-protocol` in its source repository.
2. Bump the plugin version in the source repository when distributed behavior changes.
3. Validate the plugin there.
4. Run `scripts/sync-ai-dev-protocol.ps1` in this repository.
5. Review the synced marketplace snapshot.
6. Commit and push the marketplace repository update.
7. Ask Claude Code users to run marketplace update, plugin update, and `/reload-plugins`.
8. Ask Codex users to refresh or reinstall the marketplace plugin if needed.

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
- Add it to `.claude-plugin/marketplace.json`
- Document installation and update rules as needed

See `docs/add-plugin-guide.md` for the checklist.
