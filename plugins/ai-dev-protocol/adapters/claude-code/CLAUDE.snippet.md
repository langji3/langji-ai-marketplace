# AI Dev Protocol

本项目使用 AI Dev Protocol 作为 AI 辅助开发流程规约。

开发者分支工作流：AI 在实现前先确认当前开发者分支或已有 `ai/...` 分支。

- 开发者分支：例如 `developer/<name>`、`dev/<name>`、`<name>/dev`，或用户明确指定的团队开发者汇总分支。每个明确需求从该分支创建一个 `ai/...` 分支。
- AI 分支：AI 先提交 `docs/specs/*.md`，再创建未追踪的本地 plan，完成实现和验证后 squash merge 回开发者分支。
- 分支含义不明确时，AI 必须先询问当前分支是否作为开发者分支使用。

当任务涉及需求实现、代码修改、bug fix、提交或交付时，Claude Code 必须遵守本协议的阶段化 workflow：

- 需求进入：先澄清需求，确保一个 AI 工作单元只处理一个明确 requirement。
- 分支判断：确认开发者分支、已有 AI 分支或停止在主干/环境分支。
- Spec：实现前必须写中文 spec，并等待用户确认；spec 必须写入并提交到 `docs/specs/*.md`。
- 实现：先创建未追踪的本地 plan，再拆分 plan/goals 并持续更新状态；极小改动可使用轻量 plan；只修改当前需求相关内容，不混入无关重构、格式化、依赖升级或 workflow 产物。
- 审查：复杂任务或代码变更优先使用 subagent / 多 AI 做独立审查；不可用时记录替代自检。
- 提交：commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
- Merge-back：squash merge 回开发者分支。
- 交付：最终交付包含 spec 文档路径、spec 提交状态、本地 plan Git 状态、实现提交状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证结果、merge-back 状态和开发者接管说明；API 变更包含 Apifox sync summary。

代码标识符、API 路径、表名、配置键保持英文。

自然语言的模块设计讨论如果可能进入代码实现，也必须先作为需求进入处理。用户确认开发者分支只表示分支来源已确认，不表示允许实现；下一步必须提交 `docs/specs/*.md` 并等待确认。

可以借鉴 Superpowers 式逐 goal 推进的方法，但 plan 是本地临时执行文件，不得进入 Git 追踪；不得创建 `.superpowers/` 产物，除非用户明确要求。

完整规则以本仓库 `skills/` 下各 `SKILL.md` 为准。
