# Install AI Dev Protocol In Claude Code

Claude Code currently consumes the distributed plugin snapshot from this repository rather than a dedicated marketplace index.

## Current MVP Flow

1. Open `plugins/ai-dev-protocol/`.
2. Read `.claude-plugin/plugin.json` for plugin metadata.
3. Read `adapters/claude-code/install.md` for the adapter-specific installation guide.
4. If needed, merge `adapters/claude-code/CLAUDE.snippet.md` into the target project's `CLAUDE.md`.

## Notes

- This repository is the distribution source.
- The upstream `ai-dev-protocol` repository remains the rule authoring source.
- If the team later adopts a Claude Code marketplace mechanism, this repository should remain the published snapshot source.

