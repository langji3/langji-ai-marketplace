---
name: ai-spec-writing
description: Write and confirm Chinese repository specs for AI Dev Protocol work. Use before implementation after requirement and developer branch source are clear to document goal, branch source, scope, non-goals, affected areas, approach, verification, and risks.
---

# AI Spec Writing

Use after requirement intake and developer-branch selection, before implementation.

## Do

- Write the spec in Chinese.
- Preserve English for code identifiers, API paths, table names, config keys, commands, and file paths.
- Use `templates/requirement-spec.md` when structure helps.
- Wait for user confirmation before implementation.
- Write the spec after the developer branch source is known, including after the user confirms an ambiguous branch as the developer aggregation branch.
- Treat developer-branch confirmation as input to the spec, not as spec confirmation.
- Create a Markdown spec under `docs/specs/{yyyyMMdd}-{short-desc}.md` on the `ai/...` branch and commit it before implementation.
- The repository spec document is the source of truth; the chat reply may summarize it and ask for confirmation.
- List affected areas explicitly. Include skills, adapters, docs, templates, manifests, API contracts, database migrations, tests, and configuration when they may need synchronized changes.
- If implementation discovers a target file or area from the spec is missing, irrelevant, or newly required, state the scope change and update or reconfirm the spec before editing outside the confirmed scope.

## Include

- 背景与目标
- 分支状态
- 本次范围
- 非目标
- 影响区域
- 实现思路
- 实现计划与审查方式
- 验证方式
- 风险与注意事项
- 范围变化处理方式

## Stop

If the user changes scope, update the spec or reconfirm before editing.
If no Chinese spec has been confirmed in the current workflow, do not call implementation complete and do not edit files.
If the spec has not been committed under `docs/specs/`, do not start implementation.

Next: `ai-implementation-scope`.
