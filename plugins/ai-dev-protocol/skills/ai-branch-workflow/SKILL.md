---
name: ai-branch-workflow
description: Detect and manage the AI Dev Protocol developer branch workflow. Use before creating, validating, switching, committing, or implementing to classify developer branches, existing ai/... branches, blocked trunk/environment branches, or ambiguous branches.
---

# AI Branch Workflow

Use before implementation when Git branch context matters.

## Detect

Apply project rules first. Otherwise classify current branch:

- Developer branch: `developer/<name>`, `dev/<name>`, `<name>/dev`, `<name>/develop`, `personal/<name>`, `users/<name>`, or a team-confirmed aggregation branch such as `main`.
- Existing AI branch: `ai/*`.
- Blocked trunk/environment branch: `main`, `master`, `dev`, `develop`, `site`, `staging`, `test`, `prod`, `production`, unless the user explicitly confirms it is their developer aggregation branch.
- Ambiguous: short names such as `wzh`, `dev-wzh`, `login`, `order`.
- Any other branch, including names like `feature/*`, `fix/*`, `hotfix/*`, or ticket branches, is ambiguous in the current small-team workflow. Ask whether it should be treated as the developer aggregation branch; do not work directly on it by default.

## Do

- Developer branch: create `ai/{yyyyMMdd}-{developer}-{short-desc}` from it.
- Existing `ai/...`: continue work; identify source developer branch.
- Blocked trunk/environment branch: stop unless the user confirms it is their developer aggregation branch.
- Ambiguous branch: ask whether it should be treated as the developer aggregation branch.
- Other branch names: ask before proceeding; if confirmed, treat the current branch as the developer aggregation branch and create an `ai/...` branch from it.
- User confirmation of the developer branch only resolves branch source. It is not approval to implement.
- After branch source is resolved, always continue to `ai-spec-writing` unless a confirmed repository spec already exists for the same requirement in the current workflow.
- After creating or switching to the `ai/...` branch, stop at `ai-spec-writing` and wait for spec confirmation before editing files.

## Naming

Use:

```text
ai/{yyyyMMdd}-{developer}-{short-desc}
```

Ask for `developer` if unknown. Use lowercase English kebab-case for `short-desc`.

## Output

Record:

- 分支状态
- 当前分支
- AI 分支
- 开发者分支
- merge-back 目标

Next: `ai-spec-writing`.
