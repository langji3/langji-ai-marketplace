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

Use `templates/handoff-summary.md` when structure helps.

## Verification Blocker

If a check could not run, state:

- 不能运行的命令或验证项
- 原因
- 已执行的替代检查
- 建议补验方式

## API

If API behavior, request/response contracts, endpoints, status codes, examples, permissions, or schemas changed, use `ai-apifox-sync`.

If no API changed:

```text
Apifox sync summary：无 API 变更，无需同步。
```
