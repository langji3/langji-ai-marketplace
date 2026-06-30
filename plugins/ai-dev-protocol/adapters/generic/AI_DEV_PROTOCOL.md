# AI Dev Protocol

AI Dev Protocol is a team workflow protocol for AI-assisted software development.

AI Dev Protocol 是一套面向团队的 AI 辅助开发流程规约，用于根据当前分支命名风格自动选择协作模式：需求分支直接开发，个人开发分支则创建独立 AI 分支并在完成后汇总回开发者分支。

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
- `ai-branch-workflow`：根据当前分支命名风格选择需求分支模式、个人分支模式或停止在主干/环境分支。
- `ai-spec-writing`：中文 spec 和实现前确认。
- `ai-implementation-scope`：范围控制，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-merge-back`：个人分支模式下 squash merge 回开发者个人分支。
- `ai-handoff`：最终交付、实现范围记录、范围变化说明、验证说明和开发者接管说明。
- `ai-apifox-sync`：API 变更后的 Apifox sync summary。

其他 AI 工具可以按同样阶段执行。

## 核心规则

1. 一个 AI 工作单元只处理一个明确需求。
2. AI 在动手前必须先确认需求范围。
3. AI 在实现前先根据当前分支命名风格判断分支模式。
4. 当前分支是明确需求分支时，直接在该分支工作并跳过额外 AI 分支。
5. 当前分支是开发者个人分支时，从该分支创建独立 `ai/...` 分支，以支持多个需求并行开发。
6. 用户确认分支模式只表示分支判断完成，不表示允许实现。
7. 实现前必须在当前工作流里输出中文 spec 并等待用户确认。
8. AI 不直接在主干或环境分支上实现。
9. spec 使用中文，代码标识符、API 路径、表名、配置键保持英文。
10. commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
11. 不混入无关重构、格式化、依赖变更。
12. 不提交单独 plan 文件或 `.superpowers/` 工作流产物，除非明确要求。
13. 个人分支模式下，AI 验证完成后 squash merge 回开发者个人分支。
14. 最终由开发者主导 review、联调、检查和后续合并。
15. 如有 API 变更，最终交付必须包含 Apifox sync summary。

## 标准流程

1. 需求进入：判断需求是否清楚，是否是一个独立 requirement。若范围不清，必须先提问。
2. 分支判断：根据当前分支命名风格选择需求分支模式、个人分支模式或停止在主干/环境分支。
3. 规格说明：先写中文 spec，明确目标、范围、非目标、影响文件、验证方式。
4. 实现前确认：用户确认 spec 后，才进入实现或修改阶段。
5. 范围控制：只改与当前需求相关的内容，不做无关重构、格式化、依赖升级。
6. 验证：根据项目情况运行测试、构建、静态检查，不能运行时要说明原因。
7. 提交规则：commit message 使用中文，并按 `feat:` / `fix:` 分类。
8. Merge-back：个人分支模式下 squash merge 回开发者个人分支；需求分支模式跳过。
9. 最终交付：输出变更摘要、分支模式、merge-back 状态、实现范围记录、范围变化说明、验证结果、风险说明和开发者接管说明。若有 API 变更，附 Apifox sync summary。

自然语言的模块设计讨论如果可能进入代码实现，也从需求进入开始执行。用户回复“个人分支”或“需求分支”只确认第 2 步，下一步仍是中文 spec，不得直接写代码。

## 权威规则

如果该通用文档与仓库中的 skill 规则不一致，以 `skills/` 下各 `SKILL.md` 为准。
