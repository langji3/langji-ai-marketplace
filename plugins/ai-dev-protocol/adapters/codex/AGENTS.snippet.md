# AI Dev Protocol

本项目使用 AI Dev Protocol 作为 AI 辅助开发流程规约。

Full Development Flow 的开发者分支工作流：AI 在实现前先确认当前开发者分支或已有 `ai/...` 分支。

- 开发者分支：例如 `developer/<name>`、`dev/<name>`、`<name>/dev`，或用户明确指定的团队开发者汇总分支。每个明确需求从该分支创建一个 `ai/...` 分支。
- AI 分支：AI 先提交 `docs/specs/*.md`，再在 `docs/plans/` 创建对应 spec 的未追踪本地 plan；完成实现和验证后先汇报，取得开发者对本次 merge-back 的明确授权后才能 squash merge 回开发者分支。
- 分支含义不明确时，AI 必须先询问当前分支是否作为开发者分支使用。

完整流程不应直接在主干或环境分支上实现；用户明确授权的 Quick Fix Path 按下方轻量规则处理。

当任务涉及需求实现、代码修改、bug fix、提交或交付时，Codex 必须先由 `ai-dev-protocol` Router 选择 Quick Fix Path 或 Full Development Flow。其他 skills 是内部阶段模块，不要求用户选择：

- `ai-dev-protocol`：总入口和流程路由。
- `ai-requirement-intake`：需求澄清、一需求一工作单元。
- `ai-branch-workflow`：确认开发者分支、已有 AI 分支或停止在主干/环境分支。
- `ai-spec-writing`：中文 spec 和实现前确认；spec 写入并提交到 `docs/specs/*.md`。
- `ai-implementation-scope`：范围控制、本地临时 plan、plan/goals 拆分、subagent / 独立审查，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-merge-back`：汇报准备状态并请求独立授权，明确同意后才 squash merge 回开发者分支。
- `ai-handoff`：最终交付、spec 文档路径、spec 提交状态、本地 plan Git 状态、实现提交状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证说明和开发者接管说明。
- `ai-apifox-sync`：API 变更后的 Apifox sync summary；用户需要录入 Apifox 时，抽取受影响接口和数据模型 JSON Schema 清单。

这些阶段名称是主 Router 的内部模块，不作为独立 plugin skills 暴露。

用户明确接受快速修改，且任务范围小、风险低，不涉及 API / 数据库 / 权限安全 / 依赖构建 / 跨模块行为 / 发布版本 / 分支集成时，可在用户授权的当前分支直接修改，不创建 AI 分支、spec、plan、提交或 merge-back；Codex 做聚焦自检，并明确由用户最终验证。范围扩大、命中风险项或无法确定时切换到完整流程。

自然语言的模块设计讨论如果可能进入代码实现，且不符合 Quick Fix 条件，必须从 `ai-requirement-intake` 开始。用户确认开发者分支只表示分支来源已确认，不表示允许实现；下一步必须进入 `ai-spec-writing`。先提交 `docs/specs/*.md`，等待中文 spec 确认后，再在 `docs/plans/` 创建对应 spec 的未追踪本地 plan，之后才能改实现文件。

用户确认 spec 只授权进入实现，不授权 merge-back。实现、验证和 AI 分支提交完成后，Codex 必须汇报目标开发者分支和拟合回内容，单独询问是否同意；未明确同意时不得切换、提交、合并、cherry-pick、reset 或 restore 开发者分支。

进入完整流程实现后，Codex 应按本地 plan 拆分 plan/goals 并持续更新状态。复杂任务或代码变更优先使用 subagent / 多 AI 做独立审查。若当前环境不支持 subagent，交付时说明原因并记录替代自检。可以借鉴 Superpowers 中轻量有效的上下文控制、goal 拆分、范围守卫和独立审查方法，但不得提交被 Git 追踪的 plan 文件或创建 `.superpowers/` 产物，除非用户明确要求。

完整规则以 `skills/ai-dev-protocol/SKILL.md` 及其 `phases/` 内部阶段规则为准。
