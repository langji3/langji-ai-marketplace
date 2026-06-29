---
name: ai-requirement-intake
description: Clarify AI development requirements before implementation. Use when a user request may be unclear, too broad, mixed across multiple requirements, missing success criteria, or needs the AI Dev Protocol one-requirement-per-branch rule enforced.
---

# AI Requirement Intake

Use this skill before spec writing when the requirement, scope, success criteria, or boundaries are not fully clear.

## Rules

- Confirm the user request maps to one independent requirement.
- If the request combines unrelated work, ask the user to choose one requirement for the current AI branch.
- Do not start implementation from a vague direction, broad goal, or mixed backlog item.
- Keep the discussion in Chinese unless the user asks otherwise; keep code identifiers, API paths, table names, config keys, and commands in English.

## Must Confirm

- Problem to solve.
- Expected successful result.
- In-scope behavior.
- Explicit non-goals.
- Affected areas, especially API, database, config, permissions, async jobs, frontend interactions, or external systems.
- Verification expectation.

## Stop And Ask When

- The user only describes a direction.
- Multiple independent requirements are bundled together.
- The impact may span multiple modules but the boundary is not confirmed.
- Acceptance criteria are unclear.
- A business decision cannot be derived from the repository.

## Output Before Next Phase

State in Chinese:

- 本次需求目标
- 本次需求范围
- 明确不做的内容
- 初步影响区域
- 计划验证方式

Then route to `ai-branch-workflow` or `ai-spec-writing` as appropriate.

