# Code Simplifier

An independent plugin with one public `code-simplifier` skill. It helps AI code reviews identify avoidable complexity and helps authorized implementation keep business logic readable without changing behavior. It does not replace a project's development workflow; it can run alongside AI Dev Protocol or another local process.

The source of truth is this project. The `langji-ai-marketplace/plugins/code-simplifier/` directory is a versioned distribution snapshot, not an editing location. Update the skill and version here first; validate the plugin and representative review decisions, commit a source revision, then update and verify the marketplace snapshot, indexes, and provenance together. The marketplace's existing `ai-dev-protocol` sync script does not manage this plugin. No remote repository is configured yet.

Run `python scripts/validate.py` in this project for a portable distribution check. Maintainers with the Codex skill-creator and plugin-creator tools can additionally run their `quick_validate.py skills/code-simplifier` and `validate_plugin.py .` checks. The scenarios require a reviewer to judge the actual recommendation and authorized side effects; the portable check deliberately does not pretend to test model decisions.

The single public entry point is [skills/code-simplifier/SKILL.md](skills/code-simplifier/SKILL.md). [Acceptance scenarios](tests/scenarios.md) describe decisions to revisit when the skill changes. The [attribution](NOTICE.md) and [Apache-2.0 license](LICENSE) travel with each snapshot.
