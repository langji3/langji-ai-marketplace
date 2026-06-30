# 需求 Spec：沉淀需求 spec 与 plan 文档

## 背景与目标

当前 AI Dev Protocol 的 spec 主要通过对话回复输出，确认后直接进入实现。这样虽然能推进任务，但缺少仓库内可追踪、可 review、可回溯的需求沉淀。

本次目标先聚焦个人分支模式，参考 Superpowers 的工作方式，把每个个人分支模式下的 AI 需求 spec 沉淀为 Markdown 文档并提交到 Git，同时把 plan 作为本地临时执行文件，用来拆分 goal、跟踪实现和审查，但不进入 Git 追踪：

- 个人分支模式下，每个 AI 需求先生成一份 spec md 文档。
- spec 文档确认后，先提交 spec。
- 开始实现前，再生成一份本地临时 plan md 文件。
- plan 文件不进入 Git 追踪，不作为最终交付产物。
- 后续实现基于已沉淀的 spec 和本地 plan 执行。
- 完成实现、验证、审查和提交后，按个人分支模式 squash merge 回开发者分支。

## 分支模式

- 当前模式：个人分支模式
- 开发者分支：`main`
- AI 分支：`ai/20260630-wzh-spec-plan-artifacts`
- 完成后处理：验证通过后 squash merge 回 `main`

## 本次范围

- 调整 `ai-spec-writing`：在个人分支模式下，从“直接在对话中输出 spec”为主，改为“创建需求 spec md 文档并提交”为默认流程。
- 调整 `ai-implementation-scope`：在个人分支模式下，实现前必须基于已确认 spec 创建本地临时 plan md 文件，但 plan 不进入 Git 追踪。
- 调整 `ai-dev-protocol` 总流程：在个人分支模式下，把 spec commit 和本地 plan 已创建纳入实现前门禁。
- 调整 `ai-merge-back` 和 `ai-handoff`：确保个人分支模式从 spec commit、本地 plan、实现提交、验证审查到 squash merge-back 的链路完整可交接。
- 调整 `ai-handoff`：最终交付需要引用本次 spec 文档路径，并说明 plan 执行状态，不暴露或要求提交临时 plan 文件。
- 调整模板：新增或更新 spec / plan 文档模板。
- 调整 README、adapter、iteration guide、CHANGELOG、plugin manifest。
- 保留对小修小补的轻量策略，但默认需求开发应沉淀文档。

## 非目标

- 不引入 `.superpowers/` 目录。
- 不照搬 Superpowers 的全部文件结构或命令体系。
- 不把每次普通问答、只读分析、代码解释都强制沉淀 spec 或创建 plan。
- 不在本次完整改造需求分支模式；需求分支模式暂时保留现有流程，后续根据个人分支模式试点结果再扩展。
- 不提交 plan md 到 Git。
- 不改变开发者最终 review、联调、PR、合并的责任边界。
- 不为历史需求补写 spec/plan。

## 影响区域

- `skills/ai-dev-protocol/SKILL.md`
- `skills/ai-spec-writing/SKILL.md`
- `skills/ai-spec-writing/templates/requirement-spec.md`
- `skills/ai-implementation-scope/SKILL.md`
- `skills/ai-merge-back/SKILL.md`
- `skills/ai-handoff/SKILL.md`
- `skills/ai-handoff/templates/handoff-summary.md`
- 可能新增 `skills/ai-implementation-scope/templates/local-plan.md`
- 可能新增或更新 `.gitignore`，确保约定的本地 plan 路径不进入 Git 追踪
- `README.md`
- `adapters/codex/AGENTS.snippet.md`
- `adapters/claude-code/CLAUDE.snippet.md`
- `adapters/cursor/ai-dev-protocol.mdc`
- `adapters/generic/AI_DEV_PROTOCOL.md`
- `docs/iteration-guide.md`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `CHANGELOG.md`

## 实现思路

新增正式 spec 文档目录约定：

- `docs/specs/{yyyyMMdd}-{short-desc}.md`

新增本地临时 plan 文件约定：

- 推荐路径：`.ai-dev-protocol/plans/{yyyyMMdd}-{short-desc}-plan.md`
- 该路径必须被 `.gitignore` 忽略，或使用工具环境自身的临时区。
- plan 文件用于实现过程中的 goal 拆分、状态推进、验证和审查记录，不进入 Git 追踪。

个人分支模式推荐流程调整为：

1. 需求澄清完成后，进入 `ai-branch-workflow`。
2. 个人分支模式下创建 `ai/...` 分支。
3. 在 AI 分支上创建 spec md 文档。
4. 提交 spec 文档，提交信息示例：`docs: 添加xxx需求spec`。
5. 用户确认 spec 后，创建本地临时 plan md 文件。
6. 确认 plan 文件未被 Git 追踪。
7. 按 plan 实现代码或协议变更。
8. 实现完成后提交 `feat:` 或 `fix:`。
9. 验证、独立审查、handoff。
10. 使用 `ai-merge-back` squash merge 回开发者分支。
11. 在开发者分支上输出最终交付，说明 spec 文档、plan 执行状态、AI 分支提交、merge-back 提交和开发者接管事项。

同时修正旧规则：

- “不提交单独 plan 文件”保留，但含义收窄为：plan 是本地临时执行文件，不进入 Git 追踪；spec 才是需要提交的需求沉淀。
- spec 不再只作为聊天回复存在；聊天中可以摘要说明，但权威内容以仓库内 spec md 为准。

## 实现计划与审查方式

- plan/goals 拆分：本 spec 确认后创建本地临时 plan md，并确保不进入 Git 追踪。
- 是否适合 subagent / 多 AI 协作：适合。实现完成后使用 subagent 审查协议同步一致性。
- 计划的独立审查方式：subagent 检查 skills、adapters、README、templates、manifest、CHANGELOG 是否一致。
- 无法使用 subagent 时的降级自检方式：用关键词覆盖、release checklist、`git diff --check` 和模板字段检查替代。

## 验证方式

- 检查新增或修改后的协议文本明确要求 spec md 进入 Git，plan md 作为本地临时文件不进入 Git。
- 检查旧的“禁止 plan 文件”规则已改为禁止提交临时 plan 文件，同时允许 AI 在本地创建 plan 辅助实现。
- 检查个人分支模式从 AI 分支创建、spec commit、本地 plan、实现提交、验证审查、squash merge-back 到 handoff 的流程完整。
- 检查 handoff 模板包含 spec 文档路径、spec 提交状态、plan 执行状态和 merge-back 状态。
- 检查 `.gitignore` 或等效说明能防止约定的本地 plan 路径被追踪。
- 检查 README、skills、adapters、iteration guide 同步一致。
- 校验 plugin manifest JSON 可解析，版本号一致。
- 执行 `git diff --check`。

## 风险与注意事项

- 不能让极小修复被过重流程拖慢，需要保留轻量例外。
- spec 文档会增加提交数量，但能换来需求沉淀和 review 入口。
- plan 文档要避免变成空泛清单，应包含可执行 goal、验证和审查安排。
- plan 是本地临时文件，不能依赖它作为长期追溯资料；handoff 需要总结 plan 执行结果。
- 需要明确 spec 文档目录命名规则，否则长期会变乱。

## 范围变化处理方式

如果实现中发现需要新增独立 skill，例如 `ai-plan-writing`，我会先说明原因并更新或重新确认本 spec，再新增该 skill。若现有 `ai-implementation-scope` 能承载 plan 写作，则优先不新增 skill。
