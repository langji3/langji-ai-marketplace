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

1. Validate the desired plugin revision in the source repository.
2. Run `scripts/sync-ai-dev-protocol.ps1`.
3. Confirm `.codex-plugin/plugin.json` exists in the synced snapshot.
4. Confirm `skills/` exists in the synced snapshot.
5. Review `catalog/plugins.json` and update version metadata if needed.
6. Share or publish the marketplace revision.

## Sync Script Behavior

- By default, the script pulls from `https://github.com/langji3/ai-dev-protocol.git`.
- By default, it fetches `main`.
- For local verification, pass `-SourcePath ..\ai-dev-protocol`.
- The remote checkout cache is stored under `tmp/source-cache/ai-dev-protocol/`.
