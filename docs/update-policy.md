# Marketplace Update Policy

## Purpose

This repository distributes validated plugin snapshots. It does not author workflow rules.

## Snapshot Rules

- Sync from the plugin source repository only after the plugin has been validated.
- Keep only the distribution snapshot in `plugins/<plugin-name>/`.
- Do not copy `.git/`, `.idea/`, `dist/`, or source-repository-only marketplace/build scripts.
- Preserve the upstream plugin content without editing workflow behavior in the marketplace repository.

## AI Dev Protocol Snapshot Contents

The `ai-dev-protocol` snapshot should include:

- `.codex-plugin/`
- `.claude-plugin/`
- `skills/`
- `adapters/`
- `docs/`
- `README.md`
- `CHANGELOG.md`

This is a validated release snapshot, not a full mirror of the source repository.

## Update Workflow

1. Update the desired plugin revision in the source repository.
2. Bump the plugin version when the distributed plugin behavior changes.
3. Validate the plugin in the source repository.
4. Run `scripts/sync-ai-dev-protocol.ps1`.
5. Confirm `.codex-plugin/plugin.json` exists in the synced snapshot.
6. Confirm `skills/` exists in the synced snapshot.
7. Review `catalog/plugins.json` and update version metadata if needed.
8. Share or publish the marketplace revision.

## Sync Script Behavior

- By default, the script pulls from `https://github.com/langji3/ai-dev-protocol.git`.
- By default, it fetches `main`.
- For local verification, pass `-SourcePath ..\ai-dev-protocol`.
- The remote checkout cache is stored under `tmp/source-cache/ai-dev-protocol/`.

## Consumer Update Notes

### Codex

- Codex reads this repository's marketplace snapshot through `.agents/plugins/marketplace.json`.
- Once the repository is updated, Codex consumes the new snapshot from `plugins/ai-dev-protocol/`.
- If a user does not immediately see the new version, they should refresh or reinstall the plugin from the marketplace.

### Claude Code

- Claude Code reads this repository's marketplace entry through `.claude-plugin/marketplace.json`, then installs plugins into its local cache.
- Users should refresh the marketplace, update the plugin, and reload plugins after a marketplace release:

```shell
/plugin marketplace update langji-ai-marketplace
/plugin update ai-dev-protocol@langji-ai-marketplace
/reload-plugins
```

- Claude Code relies on plugin version resolution. If the plugin snapshot changes but `.claude-plugin/plugin.json` keeps the same `version`, users may not get the new release as expected.
