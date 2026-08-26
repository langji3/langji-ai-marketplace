# AI Dev Protocol

本项目使用 AI Dev Protocol 作为 AI 辅助开发流程规约。

Full Development Flow 的开发者分支工作流：AI 在实现前先确认当前开发者分支或已有 `ai/...` 分支。

- 开发者分支：例如 `developer/<name>`、`dev/<name>`、`<name>/dev`，或用户明确指定的团队开发者汇总分支。每个明确需求从该分支创建一个 `ai/...` 分支。
- AI 分支：AI 先提交 `docs/specs/*.md`，再在 `docs/plans/` 创建对应 spec 的未追踪本地 plan；完成实现和验证后先汇报，取得开发者对本次 merge-back 的明确授权后才能 squash merge 回开发者分支。
- 分支含义不明确时，AI 必须先询问当前分支是否作为开发者分支使用。

Claude Code 必须先由 AI Dev Protocol Router 选择 Discussion Only、Apifox Standalone、Quick Fix Path 或 Full Development Flow。以下开发阶段只用于完整流程：

- 需求进入：先澄清需求，确保一个 AI 工作单元只处理一个明确 requirement。
- 分支判断：确认开发者分支、已有 AI 分支或停止在主干/环境分支。
- Spec：实现前必须写中文 spec，并等待用户确认；spec 必须写入并提交到 `docs/specs/*.md`。
- 实现：先在 `docs/plans/` 创建对应 spec 的未追踪本地 plan，再拆分 plan/goals 并持续更新状态；只修改当前需求相关内容，不混入无关重构、格式化、依赖升级或 workflow 产物。
- 审查：复杂任务或代码变更优先使用 subagent / 多 AI 做独立审查；不可用时记录替代自检。
- 提交：commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
- Merge-back：汇报准备状态并单独请求授权；开发者明确同意后才 squash merge 回开发者分支。
- 交付：最终交付包含 spec 文档路径、spec 提交状态、本地 plan Git 状态、实现提交状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证结果、merge-back 状态和开发者接管说明；API 变更包含 Apifox sync summary；用户可选择只读接口/完整响应模型清单或指定已有模块后的 CLI 同步计划。

代码标识符、API 路径、表名、配置键保持英文。

用户明确接受快速修改，且任务范围小、风险低，不涉及 API / 数据库 / 权限安全 / 依赖构建 / 跨模块行为 / 发布版本 / 分支集成时，可在用户授权的当前分支直接修改，不创建 AI 分支、spec、plan、提交或 merge-back；Claude Code 做聚焦自检，并明确由用户最终验证。范围扩大、命中风险项或无法确定时切换到完整流程。

自然语言的模块设计讨论如果可能进入代码实现，且不符合 Quick Fix 条件，也必须先作为需求进入处理。用户确认开发者分支只表示分支来源已确认，不表示允许实现；下一步必须提交 `docs/specs/*.md` 并等待确认。

用户确认 spec 只授权进入实现，不授权 merge-back。实现和验证完成后必须单独询问是否同意合回；未明确同意时停留在 AI 分支，不得修改、重置或恢复开发者分支。

Apifox CLI 写入与 Git merge-back 分别授权：先核验当前 CLI、project、已有模块、Apifox branch、双目录映射和动态 payload schema，展示幂等操作计划并取得明确确认后才能写入；默认不删除、不 blanket import、不合并 Apifox 分支，写入后必须回读。

可以借鉴 Superpowers 中轻量有效的上下文控制、goal 拆分、范围守卫和独立审查方法，但 plan 是本地临时执行文件，不得进入 Git 追踪；不得创建 `.superpowers/` 产物，除非用户明确要求。

完整规则以本仓库 `skills/ai-dev-protocol/SKILL.md` 及其 `phases/` 内部阶段规则为准。
