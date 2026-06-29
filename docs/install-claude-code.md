# Install AI Dev Protocol In Claude Code

Claude Code can consume this repository as a plugin marketplace because the repository root provides `.claude-plugin/marketplace.json`.

## Marketplace Install

Add the marketplace:

```shell
/plugin marketplace add langji3/langji-ai-marketplace
```

Install the plugin:

```shell
/plugin install ai-dev-protocol@langji-ai-marketplace
```

Reload plugins in the current session:

```shell
/reload-plugins
```

## What Claude Code Reads

- Marketplace entry: `.claude-plugin/marketplace.json`
- Plugin snapshot: `plugins/ai-dev-protocol/`
- Plugin manifest: `plugins/ai-dev-protocol/.claude-plugin/plugin.json`

## Fallback Manual Flow

If your Claude Code environment is not ready to use marketplaces yet:

1. Open `plugins/ai-dev-protocol/`.
2. Read `.claude-plugin/plugin.json` for plugin metadata.
3. Read `adapters/claude-code/install.md` for the adapter-specific installation guide.
4. If needed, merge `adapters/claude-code/CLAUDE.snippet.md` into the target project's `CLAUDE.md`.

## Notes

- This repository is the distribution source.
- The upstream `ai-dev-protocol` repository remains the rule authoring source.
- The marketplace name exposed to Claude Code is `langji-ai-marketplace`.
