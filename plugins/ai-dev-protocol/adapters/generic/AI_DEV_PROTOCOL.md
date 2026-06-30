# AI Dev Protocol

AI Dev Protocol is a team workflow protocol for AI-assisted software development.

AI Dev Protocol 是一套面向小型团队的 AI 辅助开发流程规约：开发者分支作为需求汇总站，每个 AI 工作单元创建独立 `ai/...` 分支，完成后 squash merge 回开发者分支。

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

普通问答、代码解释、只读分析不需要强制执行完整流程。

## 阶段化 Workflow

Codex 中本协议拆分为多个 skills：

- `ai-dev-protocol`：总入口和路由。
- `ai-requirement-intake`：需求澄清、一需求一工作单元。
- `ai-branch-workflow`：确认开发者分支、已有 AI 分支或停止在主干/环境分支。
- `ai-spec-writing`：中文 spec 和实现前确认；spec 写入并提交到 `docs/specs/*.md`。
- `ai-implementation-scope`：范围控制、本地临时 plan、plan/goals 拆分和独立审查，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-merge-back`：squash merge 回开发者分支。
- `ai-handoff`：最终交付、spec 文档路径、spec 提交状态、本地 plan Git 状态、实现提交状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证说明和开发者接管说明。
- `ai-apifox-sync`：API 变更后的 Apifox sync summary。

其他 AI 工具可以按同样阶段执行。

## 核心规则

1. 一个 AI 工作单元只处理一个明确需求。
2. AI 在动手前必须先确认需求范围。
3. AI 在实现前先确认开发者分支，并从开发者分支创建独立 `ai/...` 分支。
4. 用户确认开发者分支只表示分支来源确认，不表示允许实现。
5. 实现前必须在当前工作流里输出中文 spec 并等待用户确认；spec 必须提交到 `docs/specs/*.md`。
8. AI 不直接在主干或环境分支上实现。
9. spec 使用中文，代码标识符、API 路径、表名、配置键保持英文。
10. commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
11. 不混入无关重构、格式化、依赖变更。
12. spec 确认后先创建未追踪的本地 plan，再拆分 plan/goals 并随着推进更新状态；极小改动可使用轻量 plan。
13. 复杂任务或代码变更优先使用 subagent / 多 AI 做独立审查；不可用时记录替代自检。
14. 不提交被 Git 追踪的 plan 文件或 `.superpowers/` 工作流产物，除非明确要求。
15. AI 验证完成后 squash merge 回开发者分支。
16. 最终由开发者主导 review、联调、检查和后续合并。
17. 如有 API 变更，最终交付必须包含 Apifox sync summary。

## 标准流程

1. 需求进入：判断需求是否清楚，是否是一个独立 requirement。若范围不清，必须先提问。
2. 分支判断：确认开发者分支、已有 AI 分支或停止在主干/环境分支。
3. 规格说明：先写中文 spec，明确目标、范围、非目标、影响文件、验证方式；提交 `docs/specs/*.md`。
4. 实现前确认：用户确认 spec 后，才进入实现或修改阶段。
5. 范围控制：只改与当前需求相关的内容，不做无关重构、格式化、依赖升级。
6. 实现计划与审查：先创建未追踪的本地 plan，再拆分 plan/goals；复杂任务优先使用 subagent / 多 AI 做独立审查，不可用时记录替代自检。可以借鉴 Superpowers 式逐 goal 推进的方法，但不提交 plan 或创建 `.superpowers/` 产物。
7. 验证：根据项目情况运行测试、构建、静态检查，不能运行时要说明原因。
8. 提交规则：commit message 使用中文，并按 `feat:` / `fix:` 分类。
9. Merge-back：squash merge 回开发者分支。
10. 最终交付：输出变更摘要、分支状态、merge-back 状态、spec 文档路径、spec 提交状态、本地 plan Git 状态、实现提交状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证结果、风险说明和开发者接管说明。若有 API 变更，附 Apifox sync summary。

自然语言的模块设计讨论如果可能进入代码实现，也从需求进入开始执行。用户确认开发者分支只确认第 2 步，下一步仍是中文 spec，不得直接写代码。

## 权威规则

如果该通用文档与仓库中的 skill 规则不一致，以 `skills/` 下各 `SKILL.md` 为准。
