---
name: ai-commit-rules
description: Apply AI Dev Protocol commit rules. Use before preparing, reviewing, squashing, or merging commits on ai/... branches or requirement branches to ensure Chinese commit messages, correct feat:/fix: prefixes, scoped changes, and no workflow artifacts.
---

# AI Commit Rules

Use before committing, reviewing commits, or preparing squash merge-back.

## Message

Use Chinese:

- `feat:` for requirements, features, or new capabilities.
- `fix:` for modifications, bug fixes, or behavior corrections.

Examples:

```text
feat: 增加订单状态筛选
fix: 修复订单状态筛选参数缺失
```

## Rules

- Staged changes must belong only to the current requirement.
- No unrelated refactor, formatting sweep, dependency change, temporary artifact, plan file, or workflow artifact.
- Verification ran, or the blocker is recorded.
- Personal branch mode: squash merge-back commit should be one Chinese `feat:` / `fix:` commit.
- Requirement branch mode: commit directly on the requirement branch; no merge-back commit.

## Output

Provide or validate the final commit message.
