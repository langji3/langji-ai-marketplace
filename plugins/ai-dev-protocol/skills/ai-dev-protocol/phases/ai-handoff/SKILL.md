---
name: ai-handoff
description: Produce AI Dev Protocol final delivery handoffs. Use when finishing a development task to summarize changes, branch state, merge-back status, verification results, risks, developer takeover, follow-up suggestions, and Apifox sync status.
---

# AI Handoff

Use for final delivery.

## Include

- 变更摘要
- 分支状态
- Merge-back 状态
- Merge-back 授权状态：未请求 / 等待开发者授权 / 已授权 / 已拒绝 / 已取消
- spec 文档路径、spec 提交状态、本地 plan 执行状态、plan 未追踪状态、实现提交状态
- 实现范围记录：改了什么、为什么属于本次范围
- 范围变化说明：无变化，或说明新增/移除的范围及确认状态
- plan/goals 完成情况
- subagent / 独立审查情况：是否执行、发现什么、如何处理；未执行时说明原因和替代自检
- 验证结果
- 开发者接管：review、联调、检查和后续合并由开发者主导
- 风险说明
- 后续建议
- Apifox sync summary
- 如果涉及 API 变更，交付末尾主动询问用户是否需要一份可直接给 Apifox 录入的「接口清单 + 数据模型 JSON Schema」

Use `templates/handoff-summary.md` when structure helps.

When merge-back has not been explicitly approved, deliver from the AI branch, state that the developer branch is untouched, and ask the dedicated merge-back authorization question. Do not describe pending approval as a blocker or infer approval from spec confirmation.

## Verification Blocker

If a check could not run, state:

- 不能运行的命令或验证项
- 原因
- 已执行的替代检查
- 建议补验方式

## API

If API behavior, request/response contracts, endpoints, status codes, examples, permissions, or schemas changed, use `ai-apifox-sync`.

If the user asks to record the requirement/change in Apifox, use `ai-apifox-sync` to produce the Apifox entry catalog, including affected interfaces and data model JSON Schemas.

Also include this prompt in the final handoff:

```text
本次涉及 API 变更。是否需要我继续整理一份可直接给 Apifox 录入的「接口清单 + 数据模型 JSON Schema」？
```

If no API changed:

```text
Apifox sync summary：无 API 变更，无需同步。
```
