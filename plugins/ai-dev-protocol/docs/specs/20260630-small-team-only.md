# 需求 Spec：只保留小型团队个人分支模式

## 背景与目标

当前 AI Dev Protocol 同时描述了两种协作方式：

- 个人分支模式：开发者个人分支作为汇总站，AI 从个人分支创建 `ai/...` 分支，完成后 squash merge 回开发者分支。
- 需求分支模式：AI 直接在 `feature/*`、`fix/*` 等需求分支上工作，不创建 `ai/...` 分支。

现在团队希望先只服务小型团队，也就是只保留开发者个人分支模式，让协议更精简、更好执行。需求分支模式相关的兼容说明、判断逻辑、交付字段和 adapter 文案先全部移除。

本次目标：

- 只保留个人分支模式作为唯一正式开发流程。
- 当前开发者分支是需求汇总站，每个 AI 工作单元必须创建独立 `ai/...` 分支。
- AI 分支内必须先提交 `docs/specs/*.md`，确认后创建未追踪的本地 plan，再实现、验证、审查、提交、squash merge-back。
- 移除需求分支模式、直接在需求分支开发、跳过 merge-back 等相关规则。

## 分支模式

- 当前模式：个人分支模式
- 开发者分支：`main`
- AI 分支：`ai/20260630-wzh-small-team-only`
- 完成后处理：验证通过后 squash merge 回 `main`

## 本次范围

- 调整 `ai-dev-protocol`：总流程只描述个人分支模式，不再路由到需求分支模式。
- 调整 `ai-branch-workflow`：只识别开发者个人分支、已有 `ai/...` 分支、主干/环境分支和不明确分支；移除 requirement branch 直开逻辑。
- 调整 `ai-spec-writing`：移除 requirement branch 的 chat-based spec 例外，统一个人分支模式的 `docs/specs/*.md` spec。
- 调整 `ai-implementation-scope`：继续要求本地临时 plan，但只围绕个人分支模式描述。
- 调整 `ai-merge-back`：从“个人分支模式专用”变成标准必经 merge-back 阶段。
- 调整 `ai-handoff`：去掉“无需 merge-back / 需求分支模式”这类选项。
- 同步 README、adapters、install 文档、iteration guide、CHANGELOG、plugin manifest。

## 非目标

- 不支持需求分支模式的完整流程。
- 不再保留“当前分支是 `feature/*` 就直接开发”的默认行为。
- 不新增新的 workflow skill。
- 不引入 `.superpowers/` 目录。
- 不提交本地 plan 文件。
- 不修改历史发布记录中对旧版本的描述。

## 影响区域

- `skills/ai-dev-protocol/SKILL.md`
- `skills/ai-branch-workflow/SKILL.md`
- `skills/ai-spec-writing/SKILL.md`
- `skills/ai-implementation-scope/SKILL.md`
- `skills/ai-merge-back/SKILL.md`
- `skills/ai-handoff/SKILL.md`
- `skills/ai-handoff/templates/handoff-summary.md`
- `skills/ai-spec-writing/templates/requirement-spec.md`
- README
- `adapters/codex/*`
- `adapters/claude-code/*`
- `adapters/cursor/*`
- `adapters/generic/AI_DEV_PROTOCOL.md`
- `docs/iteration-guide.md`
- `.codex-plugin/plugin.json`
- `.claude-plugin/plugin.json`
- `CHANGELOG.md`

## 实现思路

把协议语言收敛成一条主链路：

1. 从开发者个人分支开始。
2. 一个需求创建一个 `ai/{yyyyMMdd}-{developer}-{short-desc}` 分支。
3. 在 AI 分支提交 `docs/specs/{yyyyMMdd}-{short-desc}.md`。
4. 用户确认 spec。
5. 创建 `.ai-dev-protocol/plans/{yyyyMMdd}-{short-desc}-plan.md` 本地临时 plan，并确认未被 Git 追踪。
6. 按 plan 实现、验证、subagent 审查。
7. 在 AI 分支提交实现。
8. squash merge 回开发者分支。
9. 交付 spec 状态、plan 状态、实现提交、merge-back 状态和开发者接管事项。

对非个人分支：

- `ai/...`：允许继续，必须识别来源开发者分支。
- 主干/环境分支：停止，除非用户明确说明它在本团队里就是开发者个人分支。
- 其他分支：视为不明确，先询问是否作为开发者个人分支使用；不再自动视为需求分支。

## 实现计划与审查方式

- 本 spec 确认后创建本地临时 plan。
- 本地 plan 路径：`.ai-dev-protocol/plans/20260630-small-team-only-plan.md`
- 适合 subagent 审查：是。
- 审查重点：是否还有 requirement branch / direct requirement branch / skip merge-back 等残留规则；个人分支链路是否完整。

## 验证方式

- `rg` 检查 requirement branch、需求分支模式、direct requirement branch、skip merge-back 等是否只保留在历史 changelog 或明确说明旧版本的上下文中。
- 检查 README、skills、adapters、install 文档同步为个人分支模式。
- 检查 plugin manifest JSON 可解析，版本号一致。
- 检查 `.ai-dev-protocol/plans/*.md` 被忽略且未被 Git 追踪。
- 执行 `git diff --check`。
- 使用 subagent 做独立审查并修复发现。

## 风险与注意事项

- 删除需求分支模式会让已有复杂 Git 流团队失去兼容说明，这是有意收敛。
- `main`、`dev` 等分支名在很多团队是主干，但本团队可把当前分支显式声明为开发者个人分支；协议要保留这个人工确认入口。
- 历史 changelog 不应为了消除关键词而改写旧版本事实。

## 范围变化处理方式

如果实现时发现某些 install 文档或 adapter 保留需求分支模式是为了历史兼容，需要先改成“旧版本曾支持，当前版本不推荐/不保留”，而不是继续作为当前规则存在。
