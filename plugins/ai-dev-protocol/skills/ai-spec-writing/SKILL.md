---
name: ai-spec-writing
description: Write and confirm Chinese requirement specs for AI Dev Protocol work. Use before implementation to document goal, scope, non-goals, affected areas, implementation approach, verification, and risks while preserving code identifiers and API paths in English.
---

# AI Spec Writing

Use this skill after requirement intake and before implementation.

## Rules

- Write the spec in Chinese.
- Keep code identifiers, API paths, table names, field names, config keys, commands, and file paths in English.
- Include scope, non-goals, affected areas, implementation approach, verification, and risks.
- Wait for user confirmation before implementation.
- If the user changes the requirement, update the spec or reconfirm the changed scope.

## Template

Use `templates/requirement-spec.md` when a structured spec is useful. For small tasks, the spec may be shorter, but it must still include:

- 背景与目标
- 本次范围
- 非目标
- 影响区域
- 验证方式

## Handoff To Implementation

Only route to `ai-implementation-scope` after the user confirms the spec.

