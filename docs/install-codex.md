# Install AI Dev Protocol In Codex

1. Open the Codex plugin page.
2. Click `Add plugin marketplace`.
3. Enter the repository path or repository URL for `langji-ai-marketplace`.
4. Open `Langji AI Marketplace`.
5. Install `AI Dev Protocol`.
6. Start a new Codex thread.
7. Confirm the plugin skills are available in the thread.

## What Codex Reads

Codex reads `.agents/plugins/marketplace.json` as the marketplace entrypoint.

For `ai-dev-protocol`, the marketplace points Codex to:

```text
./plugins/ai-dev-protocol
```

Codex then loads the plugin snapshot from that directory, including `.codex-plugin/plugin.json` and `skills/`.

