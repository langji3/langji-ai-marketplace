# Langji AI Marketplace MVP Design

## Goal

Create a lightweight marketplace repository that distributes validated AI plugin snapshots, starting with `ai-dev-protocol`, without turning the marketplace into the source-of-truth for plugin rules.

## Scope

- Create marketplace-level documentation and installation guides.
- Add a Codex marketplace entrypoint at `.agents/plugins/marketplace.json`.
- Add a Claude Code marketplace entrypoint at `.claude-plugin/marketplace.json`.
- Add a tool-agnostic catalog at `catalog/plugins.json`.
- Add a local sync script for `ai-dev-protocol`.
- Store the validated `ai-dev-protocol` distribution snapshot under `plugins/ai-dev-protocol/`.

## Non-Goals

- No CI pipeline.
- No package publishing.
- No automatic tag or release workflow.
- No complex version resolution.
- No rule authoring inside this repository.

## Repository Boundaries

- This repository is for distribution only.
- Plugin rules and adapters continue to live in their own source repositories.
- The marketplace stores release snapshots that are safe for tools to install from directly.
- Snapshot contents must exclude source-control metadata, editor metadata, build artifacts, and source-repository-only scripts.

## Architecture

### Marketplace Index Layer

`catalog/plugins.json` provides a tool-neutral plugin listing for future consumers, while `.agents/plugins/marketplace.json` is the Codex-specific marketplace entrypoint and `.claude-plugin/marketplace.json` is the Claude Code marketplace entrypoint.

### Snapshot Layer

`plugins/ai-dev-protocol/` stores the validated release snapshot that Codex, Claude Code, and Cursor consume. The snapshot contains installable plugin assets rather than the full source repository history.

### Sync Layer

`scripts/sync-ai-dev-protocol.ps1` synchronizes the source repository `https://github.com/langji3/ai-dev-protocol.git` into the marketplace snapshot and validates required plugin assets. For local development, it can also read from an explicit `-SourcePath`.

## Validation

- Confirm the marketplace index exposes `ai-dev-protocol`.
- Confirm the Claude Code marketplace manifest exposes `ai-dev-protocol`.
- Confirm the snapshot contains `.codex-plugin/plugin.json`.
- Confirm the snapshot contains `skills/`.
- Confirm the marketplace docs explain how each tool consumes the snapshot.
