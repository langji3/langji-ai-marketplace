---
name: ai-handoff
description: Produce AI Dev Protocol final delivery handoffs. Use when finishing a development task to summarize changes, verification results, branch mode, merge-back status, risks, follow-up suggestions, and whether an Apifox sync summary is required.
---

# AI Handoff

Use this skill for final delivery after implementation, verification, and merge-back when applicable.

## Required Content

- 变更摘要：说明完成了什么。
- 分支模式：说明是默认 `ai/...` 分支模式，还是直接需求分支兼容模式。
- Merge-back 状态：默认模式下说明是否已 squash merge 回开发者分支；兼容模式下说明无需 merge-back。
- 验证结果：列出运行过的测试、构建、静态检查或手动验证。
- 开发者接管：说明开发者接下来主导 review、联调、检查和后续合并。
- 风险说明：说明潜在影响、未覆盖场景或已知限制。
- 后续建议：只列出与当前需求相关但未纳入范围的事项。

Use `templates/handoff-summary.md` when a structured handoff is useful.

## Verification Could Not Run

If a check could not run, state:

- 不能运行的命令或验证项。
- 具体原因。
- 已执行的替代检查。
- 建议后续如何补验。

## API Changes

If API behavior, request/response contracts, endpoints, status codes, examples, or schemas changed, use `ai-apifox-sync` and include its summary in the handoff.

If no API changed, write:

```text
Apifox sync summary：无 API 变更，无需同步。
```

