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
- Apifox CLI 状态：未请求 / 只读计划 / 等待外部写入授权 / 已执行并回读 / 已拒绝 / 已阻断
- 如果涉及 API 变更，交付末尾主动询问用户需要只读的「接口清单 + 响应数据模型 JSON Schema」，还是指定已有模块后的 CLI 同步计划

Use the [handoff summary template](templates/handoff-summary.md) when structure helps.

When merge-back has not been explicitly approved, deliver from the AI branch and state that the developer branch is untouched. For a delivery/report-only request, report merge status only; do not ask for integration decisions. Enter merge-back when requested or already due under the user's arrangement, using a verified target and dedicated approval. Do not describe pending approval as a blocker or infer approval from spec confirmation.

When the user requested a report to another conversation, send this same handoff using the supplied, verified destination and available authorized tools. Unknown recipients or merge targets stay unknown; do not guess IDs or reuse another requirement's destination. If the destination or delivery capability is unavailable, provide a transferable summary and explicitly state it was not sent to the requested conversation. A reply in the current task does not deliver it to another conversation or prove user notification. This skill does not start monitoring or define a dispatch workflow.

## Verification Blocker

If a check could not run, state:

- 不能运行的命令或验证项
- 原因
- 已执行的替代检查
- 建议补验方式

## API

If API behavior, request/response contracts, endpoints, status codes, examples, permissions, or schemas changed, use [AI Apifox Sync](../ai-apifox-sync/PHASE.md).

If the user asks to record the requirement/change in Apifox, use [AI Apifox Sync](../ai-apifox-sync/PHASE.md) to produce a read-only catalog or run its gated CLI synchronization mode. Never collapse the CLI operation-plan authorization into repository merge-back authorization.

Also include this prompt in the final handoff:

```text
本次涉及 API 变更。是否需要我继续整理只读的「接口清单 + 响应数据模型 JSON Schema」，或为指定的已有 Apifox 模块生成 CLI 同步计划？
```

If no API changed:

```text
Apifox sync summary：无 API 变更，无需同步。
```
