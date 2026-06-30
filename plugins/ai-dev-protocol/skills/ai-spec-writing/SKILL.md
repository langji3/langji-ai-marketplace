---
name: ai-spec-writing
description: Write and confirm Chinese requirement specs for AI Dev Protocol work. Use before implementation after requirement and branch mode are clear to document goal, branch mode, scope, non-goals, affected areas, approach, verification, and risks.
---

# AI Spec Writing

Use after requirement intake and branch-mode selection, before implementation.

## Do

- Write the spec in Chinese.
- Preserve English for code identifiers, API paths, table names, config keys, commands, and file paths.
- Use `templates/requirement-spec.md` when structure helps.
- Wait for user confirmation before implementation.
- Write the spec after branch mode is known, including after the user confirms an ambiguous branch as personal or requirement branch.
- Treat branch-mode confirmation as input to the spec, not as spec confirmation.
- List affected areas explicitly. Include skills, adapters, docs, templates, manifests, API contracts, database migrations, tests, and configuration when they may need synchronized changes.
- If implementation discovers a target file or area from the spec is missing, irrelevant, or newly required, state the scope change and update or reconfirm the spec before editing outside the confirmed scope.

## Include

- 背景与目标
- 分支模式
- 本次范围
- 非目标
- 影响区域
- 实现思路
- 验证方式
- 风险与注意事项
- 范围变化处理方式

## Stop

If the user changes scope, update the spec or reconfirm before editing.
If no Chinese spec has been confirmed in the current workflow, do not call implementation complete and do not edit files.

Next: `ai-implementation-scope`.
