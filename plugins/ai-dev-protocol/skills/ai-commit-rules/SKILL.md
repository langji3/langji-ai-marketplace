---
name: ai-commit-rules
description: Apply AI Dev Protocol commit rules. Use before preparing or reviewing commits on ai/... branches, direct requirement branches, or squash merge-back commits to ensure Chinese commit messages, correct feat:/fix: prefixes, and no unrelated changes.
---

# AI Commit Rules

Use this skill before committing, reviewing commits, or preparing a squash merge-back commit.

## Message Format

Commit messages must be Chinese and use one of:

- `feat:` for requirements, features, or new capabilities.
- `fix:` for modifications, bug fixes, or behavior corrections.

Examples:

```text
feat: 增加订单状态筛选
fix: 修复订单状态筛选参数缺失
```

## Default Mode

When working on an `ai/...` branch:

- Intermediate commits may be created if useful, but they must stay scoped to the requirement.
- The merge-back commit on the developer branch should be a single Chinese squash commit.
- The squash commit message should summarize the requirement, not the internal AI process.

Example:

```text
feat: 增加订单状态筛选
```

## Compatibility Mode

When working directly on an existing requirement branch:

- Use the same Chinese `feat:` / `fix:` rule.
- Do not create an extra merge-back commit.
- Keep commits reviewable by the developer.

## Pre-Commit Checklist

- Branch mode is known: default AI branch mode or direct requirement branch mode.
- Changes belong only to the current requirement.
- No unrelated refactor, formatting sweep, dependency change, or workflow artifact is included.
- Verification has run, or the reason it cannot run is recorded.
- Commit message is Chinese and uses the correct prefix.

