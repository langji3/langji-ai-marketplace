# AI Dev Protocol

AI Dev Protocol is a team workflow protocol for AI-assisted software development.

AI Dev Protocol 是一套面向小型团队的 AI 辅助开发流程规约：Router 先选择 Discussion Only、Apifox Standalone、Quick Fix Path 或 Full Development Flow；完整流程中，开发者分支作为需求汇总站，每个 AI 工作单元创建独立 `ai/...` 分支，完成后先汇报并取得开发者明确授权，再 squash merge 回开发者分支。

## 使用场景

当 AI 工具处理以下任务时，应遵守本协议：

- 需求实现
- 代码修改
- bug fix
- 实现计划
- 模块设计或需求讨论后准备进入实现
- commit 准备
- merge-back
- 最终交付

普通问答、代码解释、只读分析不需要强制执行完整流程。低风险小修改可由 Router 选择 Quick Fix Path。

## 阶段化 Workflow

Codex 中本协议拆分为一个对外 Router skill 和多个打包在 Router 内的阶段模块：

- `ai-dev-protocol`：总入口和路由。
- `ai-requirement-intake`：需求澄清、一需求一工作单元。
- `ai-branch-workflow`：确认开发者分支、已有 AI 分支或停止在主干/环境分支。
- `ai-spec-writing`：中文 spec 和实现前确认；spec 写入并提交到 `docs/specs/*.md`。
- `ai-implementation-scope`：范围控制、`docs/plans/` 本地临时 plan、plan/goals 拆分和独立审查，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-merge-back`：汇报 merge-back 准备状态，取得开发者明确授权后才 squash merge 回开发者分支。
- `ai-handoff`：最终交付、spec 文档路径、spec 提交状态、本地 plan Git 状态、实现提交状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证说明和开发者接管说明。
- `ai-apifox-sync`：API 变更后的 sync summary、手工录入清单，以及指定已有模块后的受控 CLI 同步；请求不建立复用模型，重点完整同步响应后端模型。

其他 AI 工具可以按同样阶段执行。

## 核心规则

1. `ai-dev-protocol` 先选择 Discussion Only、Apifox Standalone、Quick Fix Path 或 Full Development Flow；无法确定开发风险时走完整流程。
2. 用户明确接受快速修改，且范围小、风险低、不涉及 API / 数据库 / 权限安全 / 依赖构建 / 跨模块行为 / 发布版本 / 分支集成时，可直接修改用户授权的当前分支，不创建 AI 分支、spec、plan、提交或 merge-back；AI 做聚焦自检，用户最终验证。
3. 完整流程中的一个 AI 工作单元只处理一个明确需求。
4. AI 在动手前必须先确认需求范围。
5. 完整流程实现前先确认开发者分支，并从开发者分支创建独立 `ai/...` 分支。
6. 用户确认开发者分支只表示分支来源确认，不表示允许实现。
7. 完整流程实现前必须在当前工作流里输出中文 spec 并等待用户确认；spec 必须提交到 `docs/specs/*.md`。
8. 完整流程不直接在主干或环境分支上实现。
9. spec 使用中文，代码标识符、API 路径、表名、配置键保持英文。
10. commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
11. 不混入无关重构、格式化、依赖变更。
12. spec 确认后先在 `docs/plans/` 创建对应 spec 的未追踪本地 plan，再拆分 plan/goals 并随着推进更新状态。
13. 复杂任务或代码变更优先使用 subagent / 多 AI 做独立审查；不可用时记录替代自检。
14. 不提交被 Git 追踪的 plan 文件或 `.superpowers/` 工作流产物，除非明确要求。
15. AI 验证完成后单独请求 merge-back 授权；spec 确认不代表合回授权，未明确同意时不得修改开发者分支。
16. 最终由开发者主导 review、联调、检查和后续合并。
17. 如有 API 变更，最终交付必须包含 Apifox sync summary；用户可选择只读接口/完整响应模型 JSON Schema 清单，或指定已有模块后的 CLI 同步计划。
18. Apifox CLI 写入前必须核验当前 CLI、project、已有模块、Apifox branch、接口/响应模型双目录和动态 payload schema，展示幂等操作计划并取得独立授权；默认不删除、不 blanket import、不合并 Apifox 分支，写入后回读。

## 完整流程

以下步骤只适用于 Full Development Flow：

1. 需求进入：判断需求是否清楚，是否是一个独立 requirement。若范围不清，必须先提问。
2. 分支判断：确认开发者分支、已有 AI 分支或停止在主干/环境分支。
3. 规格说明：先写中文 spec，明确目标、范围、非目标、影响文件、验证方式；提交 `docs/specs/*.md`。
4. 实现前确认：用户确认 spec 后，才进入实现或修改阶段。
5. 范围控制：只改与当前需求相关的内容，不做无关重构、格式化、依赖升级。
6. 实现计划与审查：先在 `docs/plans/` 创建对应 spec 的未追踪本地 plan，再拆分 plan/goals；复杂任务优先使用 subagent / 多 AI 做独立审查，不可用时记录替代自检。可以借鉴 Superpowers 中轻量有效的上下文控制、goal 拆分、范围守卫和独立审查方法，但不提交 plan 或创建 `.superpowers/` 产物。
7. 验证：根据项目情况运行测试、构建、静态检查，不能运行时要说明原因。
8. 提交规则：commit message 使用中文，并按 `feat:` / `fix:` 分类。
9. Merge-back：先汇报实现、验证、目标分支和拟用提交信息，明确询问并取得开发者授权后才 squash merge。
10. 最终交付：输出变更摘要、分支状态、merge-back 状态、spec 文档路径、spec 提交状态、本地 plan Git 状态、实现提交状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证结果、风险说明和开发者接管说明。若有 API 变更，附 Apifox sync summary；用户可选择只读接口/完整响应模型 JSON Schema 清单，或指定已有模块后的 CLI 同步计划。

自然语言的模块设计讨论如果可能进入代码实现，也从需求进入开始执行。用户确认开发者分支只确认第 2 步，下一步仍是中文 spec，不得直接写代码。

用户确认 spec 只授权进入实现，不授权 merge-back。实现和验证完成后必须单独询问是否同意合回；未明确同意时停留在 AI 分支，不得修改、重置或恢复开发者分支。

## 权威规则

如果该通用文档与仓库中的规则不一致，以 `skills/ai-dev-protocol/SKILL.md` 及其 `phases/` 内部阶段规则为准。
