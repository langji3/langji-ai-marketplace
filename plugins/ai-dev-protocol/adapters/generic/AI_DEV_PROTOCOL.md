# AI Dev Protocol

AI Dev Protocol is a team workflow protocol for AI-assisted software development.

AI Dev Protocol 是一套面向小型团队的 AI 辅助开发流程规约，用于让开发者通过个人开发分支快速并行启动多个 AI 需求分支，并在 AI 完成后汇总回开发者分支，由开发者主导 review、联调、检查和后续合并。

## 使用场景

当 AI 工具处理以下任务时，应遵守本协议：

- 需求实现
- 代码修改
- bug fix
- 实现计划
- commit 准备
- merge-back
- 最终交付

普通问答、代码解释、只读分析不需要强制执行完整流程。

## 阶段化 Workflow

Codex 中本协议拆分为多个 skills：

- `ai-dev-protocol`：总入口和路由。
- `ai-requirement-intake`：需求澄清、一需求一工作单元。
- `ai-branch-workflow`：选择默认 AI 分支模式或直接需求分支兼容模式。
- `ai-spec-writing`：中文 spec 和实现前确认。
- `ai-implementation-scope`：范围控制，禁止无关改动。
- `ai-commit-rules`：中文 `feat:` / `fix:` commit。
- `ai-merge-back`：默认模式下 squash merge 回开发者个人分支。
- `ai-handoff`：最终交付、验证说明和开发者接管说明。
- `ai-apifox-sync`：API 变更后的 Apifox sync summary。

其他 AI 工具可以按同样阶段执行。

## 核心规则

1. 一个 AI 工作单元只处理一个明确需求。
2. AI 在动手前必须先确认需求范围。
3. 默认从开发者个人分支创建独立 `ai/...` 分支，以支持多个需求并行开发。
4. 当前分支已是明确需求分支时，可直接工作并跳过额外 AI 分支。
5. AI 不直接在主干或环境分支上实现。
6. spec 使用中文，代码标识符、API 路径、表名、配置键保持英文。
7. commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
8. 不混入无关重构、格式化、依赖变更。
9. 不提交单独 plan 文件或 `.superpowers/` 工作流产物，除非明确要求。
10. 默认模式下，AI 验证完成后 squash merge 回开发者个人分支。
11. 最终由开发者主导 review、联调、检查和后续合并。
12. 如有 API 变更，最终交付必须包含 Apifox sync summary。

## 标准流程

1. 需求进入：判断需求是否清楚，是否是一个独立 requirement。若范围不清，必须先提问。
2. 分支判断：选择默认 AI 分支模式或直接需求分支兼容模式。
3. 规格说明：先写中文 spec，明确目标、范围、非目标、影响文件、验证方式。
4. 实现前确认：用户确认 spec 后，才进入实现或修改阶段。
5. 范围控制：只改与当前需求相关的内容，不做无关重构、格式化、依赖升级。
6. 验证：根据项目情况运行测试、构建、静态检查，不能运行时要说明原因。
7. 提交规则：commit message 使用中文，并按 `feat:` / `fix:` 分类。
8. Merge-back：默认模式下 squash merge 回开发者个人分支。
9. 最终交付：输出变更摘要、分支模式、merge-back 状态、验证结果、风险说明和开发者接管说明。若有 API 变更，附 Apifox sync summary。

## 权威规则

如果该通用文档与仓库中的 skill 规则不一致，以 `skills/` 下各 `SKILL.md` 为准。

