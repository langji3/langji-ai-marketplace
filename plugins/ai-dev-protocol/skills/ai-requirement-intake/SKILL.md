---
name: ai-requirement-intake
description: Clarify AI development requirements before implementation. Use when a request is unclear, broad, mixed across multiple requirements, missing acceptance criteria, or needs the one-requirement-per-AI-work-unit rule enforced.
---

# AI Requirement Intake

Use before spec writing when the request is not clearly one actionable requirement.

## Do

- Confirm the problem, expected result, scope, non-goals, affected areas, and verification.
- Keep discussion in Chinese unless the user asks otherwise.
- Keep code identifiers, API paths, table names, config keys, commands, and file paths in English.
- Split bundled work; handle only one independent requirement per AI work unit.

## Stop

Ask before continuing when:

- The request is only a direction.
- Multiple independent requirements are mixed.
- Acceptance criteria or affected modules are unclear.
- A business, compatibility, permission, or data-risk decision is missing.

## Output

State in Chinese:

- 本次需求目标
- 本次需求范围
- 明确不做的内容
- 初步影响区域
- 计划验证方式

Next: `ai-branch-workflow` or `ai-spec-writing`.
