---
name: ai-branch-workflow
description: Detect and manage AI Dev Protocol branch modes. Use before creating, validating, switching, committing, or implementing on a branch to classify requirement branches, personal developer branches, existing ai/... branches, forbidden trunk/environment branches, or ambiguous branches.
---

# AI Branch Workflow

Use before implementation when Git branch context matters.

## Detect

Apply project rules first. Otherwise classify current branch:

- Requirement branch: `feature/*`, `feat/*`, `fix/*`, `bugfix/*`, `hotfix/*`, `task/*`, `story/*`, `requirement/*`, `JIRA-123-*`.
- Personal branch: `developer/<name>`, `dev/<name>`, `<name>/dev`, `<name>/develop`, `personal/<name>`, `users/<name>`.
- Existing AI branch: `ai/*`.
- Forbidden branch: `main`, `master`, `dev`, `develop`, `site`, `staging`, `test`, `prod`, `production`.
- Ambiguous: short names such as `wzh`, `dev-wzh`, `login`, `order`.

## Do

- Requirement branch: work directly on current branch; skip `ai/...` and merge-back.
- Personal branch: create `ai/{yyyyMMdd}-{developer}-{short-desc}` from it.
- Existing `ai/...`: continue work; identify source developer branch.
- Forbidden branch: stop unless user confirms exception.
- Ambiguous branch: ask whether it is personal or requirement branch.

## Naming

Use:

```text
ai/{yyyyMMdd}-{developer}-{short-desc}
```

Ask for `developer` if unknown. Use lowercase English kebab-case for `short-desc`.

## Output

Record:

- 分支模式
- 当前分支
- AI 分支
- 开发者分支
- 是否需要 merge-back

Next: `ai-spec-writing`.
