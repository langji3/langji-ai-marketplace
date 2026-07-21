# AI Dev Protocol

AI Dev Protocol is a lightweight team workflow plugin for AI-assisted software development.

AI Dev Protocol 是一套面向小型团队的轻量 AI 辅助开发插件：它不追求覆盖所有 AI 工作方式，而是保证每个 AI 代码变更需求清楚、分支正确、范围可控、提交干净、交付可接管、API 可同步。

## 项目定位

`ai-dev-protocol` 是一个可独立维护、可通过 GitHub 拉取、可被多个 AI 编程工具复用的轻量团队开发流程插件。它不是单个项目里的提示词，也不是普通规范文档。

本仓库借鉴 Superpowers 的 skill 拆分、上下文控制、计划拆分、独立审查和交付质量思想，但不继承大而全的任务系统、隐藏状态、复杂产物和过度自动化。AI Dev Protocol 的定位是团队流程主控层，而不是通用能力增强层。

- `.codex-plugin/plugin.json` 声明 Codex plugin。
- `.claude-plugin/plugin.json` 声明 Claude Code plugin 元数据。
- `skills/` 下只放一个可发现的 Router skill。
- `ai-dev-protocol` 是唯一面向用户和允许隐式触发的 Router skill。
- 其他 `ai-*` 阶段规则放在 Router 的 `phases/` 资源目录，分别负责需求、分支、spec、范围控制、提交、merge-back、交付和 Apifox 录入清单 / 同步。

设计原则见 `docs/design-principles.md`，常见使用方式见 `docs/usage-scenarios.md`。

## 两条执行路径

Router 先判断任务应走哪条路径：

- Quick Fix Path：用户明确要求或接受快速修改，且改动范围小、风险低，不涉及 API / 数据库 / 权限安全 / 依赖构建 / 跨模块行为 / 发布版本 / 分支集成。AI 可在用户明确授权的当前分支直接修改，不创建 AI 分支、spec、plan、提交或 merge-back；AI 做聚焦自检，最终由用户验证。
- Full Development Flow：功能开发、非简单修复、高风险变更或无法确定风险的任务，执行下面的完整开发者分支流。

Quick Fix 一旦出现范围扩大或风险项，立即停止轻量路径并切换到完整流程。

## 完整开发流程

AI Dev Protocol 面向小型团队的开发者分支流：

```text
developer/<name>
dev/<name>
<name>/dev
  -> ai/{yyyyMMdd}-{developer}-{short-desc}
  -> ai/{yyyyMMdd}-{developer}-{another-desc}
  <- squash merge back to developer/<name>
```

这个模式下：

- 开发者分支是多个 AI 需求的汇总站。
- 一个 `ai/...` 分支只处理一个明确需求。
- AI 在 `ai/...` 分支上先提交 `docs/specs/{yyyyMMdd}-{short-desc}.md` 需求 spec，用户确认后再创建本地临时 plan。
- 本地 plan 统一放在 `docs/plans/{yyyyMMdd}-{short-desc}-plan.md`，文件名参考对应 spec，用于拆分 goals 和跟踪执行；该目录必须被 `.gitignore` 忽略，不进入 Git 追踪。
- AI 完成实现、验证、独立审查和提交后，先汇报结果并单独请求 merge-back 授权；只有开发者明确同意后，才 squash merge 回开发者分支。
- 开发者在开发者分支上主导 review、联调、检查和后续合并。
- AI 在 merge-back 后转为辅助身份：解释变更、修 review 问题、补测试、整理 Apifox 摘要。

AI 不应直接在主干或环境分支上实现，除非用户明确确认当前分支就是本团队的开发者汇总分支。即使当前开发者分支名是 `main`，也仍然按“开发者分支 -> AI 分支 -> squash merge-back”的流程执行。

## Plugin 入口与内部阶段

Codex 和 Claude Code 安装 plugin 后只发现一个主 Router：

```text
ai-dev-protocol
```

Router 按需读取自身 `phases/` 下的内部阶段模块：

```text
ai-requirement-intake
ai-branch-workflow
ai-spec-writing
ai-implementation-scope
ai-commit-rules
ai-merge-back
ai-handoff
ai-apifox-sync
```

阶段模块不是独立 plugin skills，不会参与平台自动发现，也不要求用户选择。`agents/openai.yaml` 仅描述主 Router。

## 核心目标

1. Router 先判断 Quick Fix Path 或 Full Development Flow；无法确定时走完整流程。
2. Quick Fix 仅用于用户接受的低风险小修改，由用户完成最终验证。
3. 完整流程中的一个 AI 工作单元只处理一个明确需求。
4. AI 在动手前必须先确认需求范围。
5. 完整流程实现前先确认开发者分支，并从开发者分支创建独立 `ai/...` 分支。
6. 完整流程不直接在开发者分支、主干或环境分支上实现。
7. spec 使用中文，代码标识符、API 路径、表名、配置键保持英文。
8. spec 必须沉淀为 `docs/specs/*.md` 并先提交。
9. 开始完整流程实现前必须在 `docs/plans/` 创建本地临时 plan，并确认 plan 未被 Git 追踪。
10. commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
11. 不混入无关重构、格式化、依赖变更。
12. 完整流程实现阶段先拆分 plan/goals，并随着推进更新状态。
13. 复杂任务或代码变更优先使用 subagent / 多 AI 做独立审查；不可用时记录替代自检。
14. 不提交被 Git 追踪的 plan 文件或 `.superpowers/` 工作流产物，除非明确要求。
15. 最终交付必须包含测试/验证说明。
16. AI 验证完成后汇报 merge-back 准备状态；规格确认和开发授权不等于合回授权，必须取得开发者对本次 merge-back 的明确同意后才能修改开发者分支。
17. 最终由开发者主导 review、联调、检查和后续合并。
18. 如有 API 变更，最终交付必须包含 Apifox sync summary，并主动询问是否需要一份可直接给 Apifox 录入的「接口清单 + 数据模型 JSON Schema」；用户也可以单独要求从需求、spec、diff 或变更说明中抽取 Apifox 录入清单。

## 轻量插件原则

AI Dev Protocol 优先保证真实团队开发的可用性：

- 少入口：用户通常只需要触发 `ai-dev-protocol`。
- 少隐藏状态：流程状态来自当前分支、Git 状态、spec、plan 和提交记录。
- 少自动化魔法：关键 gate 必须让用户知道，例如 spec 确认、分支来源、merge-back。
- 少产物污染：AI 临时 plan、外部 workflow 产物和工具状态默认不进入业务提交。
- 少路径分歧：spec 统一在 `docs/specs/`，本地 plan 统一在 `docs/plans/`。
- 先可接管，再自动化：交付必须让开发者能 review、联调、测试和继续合并。

从 Superpowers 借鉴的是有效开发方法，不是完整系统：

- 借鉴 context hygiene：只读取完成任务需要的上下文。
- 借鉴 plan discipline：复杂任务先拆 goal，推进时更新状态。
- 借鉴 scope guard：发现范围扩大要说明并收口。
- 借鉴 review pass：代码变更后做独立审查或替代自检。
- 借鉴 handoff quality：最终交付说明验证、风险和开发者接管。
- 不借鉴过度嵌套流程、隐藏任务状态、`.superpowers/` 产物或大而全 agent 角色。

## 目录结构

```text
ai-dev-protocol/
  README.md
  CHANGELOG.md
  docs/
    iteration-guide.md
    design-principles.md
    usage-scenarios.md
    specs/
      {yyyyMMdd}-{short-desc}.md
    plans/
      {yyyyMMdd}-{short-desc}-plan.md  # ignored local execution plans
  .codex-plugin/
    plugin.json
  .claude-plugin/
    plugin.json

  skills/
    ai-dev-protocol/
      SKILL.md
      agents/openai.yaml
      phases/
        ai-requirement-intake/SKILL.md
        ai-branch-workflow/SKILL.md
        ai-spec-writing/
          SKILL.md
          templates/requirement-spec.md
        ai-implementation-scope/
          SKILL.md
          templates/local-plan.md
        ai-commit-rules/SKILL.md
        ai-merge-back/SKILL.md
        ai-handoff/
          SKILL.md
          templates/handoff-summary.md
        ai-apifox-sync/
          SKILL.md
          templates/
            apifox-sync-summary.md
            apifox-entry-catalog.md

  adapters/
    codex/
      AGENTS.snippet.md
      install.md
    claude-code/
      CLAUDE.snippet.md
      install.md
    cursor/
      ai-dev-protocol.mdc
      install.md
    generic/
      AI_DEV_PROTOCOL.md
```

## Workflow Routing

Router 先做路径分类。Quick Fix 按“确认小改动 -> 直接修改 -> 聚焦自检 -> 用户验证”执行；以下阶段只适用于 Full Development Flow：

1. 需求进入：使用 `ai-requirement-intake` 判断需求是否清楚，是否是一个独立 requirement。
2. 分支判断：使用 `ai-branch-workflow` 确认开发者分支、已有 AI 分支或阻断主干/环境分支。
3. 规格说明：使用 `ai-spec-writing` 写中文 spec，明确目标、范围、非目标、影响文件、验证方式；必须创建并提交 `docs/specs/*.md`。
4. 实现前确认：用户确认 spec 后，AI 才进入实现或修改阶段。
5. 本地计划：使用 `ai-implementation-scope` 在 `docs/plans/{yyyyMMdd}-{short-desc}-plan.md` 创建本地临时 plan，并确认它未被 Git 追踪。
6. 范围控制：使用 `ai-implementation-scope` 控制改动范围，不做无关重构、格式化、依赖升级。
7. 实现计划与审查：按本地 plan 拆分 plan/goals，复杂任务优先使用 subagent / 多 AI 做独立审查，不可用时记录替代自检。
8. 验证：根据项目情况运行测试、构建、静态检查，不能运行时要说明原因。
9. 提交规则：使用 `ai-commit-rules` 检查中文 commit message，并按 `feat:` / `fix:` 分类。
10. Merge-back：使用 `ai-merge-back` 汇报实现与验证结果，单独请求开发者授权；明确同意后才将 AI 分支 squash merge 回开发者分支。
11. 最终交付：使用 `ai-handoff` 输出变更摘要、spec 文档和提交状态、本地 plan 执行状态、分支状态、merge-back 状态、实现范围记录、范围变化说明、plan/goals 完成情况、subagent / 独立审查情况、验证结果、风险说明和开发者接管说明。
12. API / Apifox：使用 `ai-apifox-sync` 输出 Apifox sync summary；当用户需要录入 Apifox 时，抽取受影响接口、请求侧模型 JSON Schema（Path / Query / Headers / Cookies / Body）、响应模型 JSON Schema、枚举、错误码和权限清单。

### 状态恢复

AI Dev Protocol 必须能从中途继续，而不是假设所有任务都从零开始：

- 已在开发者分支：确认分支来源，创建或建议创建 `ai/...` 分支。
- 已在 `ai/...` 分支：识别来源开发者分支、spec、plan、提交和未完成项。
- spec 已存在：读取并确认是否仍是当前需求范围。
- plan 已存在：继续使用 `docs/plans/` 下对应 spec 的未追踪本地 plan；如不存在，按当前 spec 创建。
- 已实现未提交：先做范围检查和验证，再按提交规则处理。
- 已提交未 merge-back：记录验证状态，按 `ai-merge-back` 汇报并等待开发者明确授权；未授权时停留在 AI 分支。
- API 已变更但未整理：补充 Apifox sync summary；当用户需要录入 Apifox 时，输出可录入的接口清单和数据模型 JSON Schema。

### 对话式需求入口

开发人员通常会先用自然语言讨论模块设计，例如“我现在要设计一个模块”“我们目前的想法是”“下一步会做什么”。这类对话如果可能进入代码实现，也属于正式流程入口。

- AI 应先把自然讨论收口为需求目标、范围、非目标、影响区域和验证方式。
- 用户确认开发者分支只表示分支来源确认，不表示允许实现。
- 即使已经创建 `ai/...` 分支，也必须先创建并提交 `docs/specs/*.md`，再等待用户确认。
- spec 确认后必须创建本地临时 plan，确认 plan 未被 Git 追踪，再进入实现。
- 只有在当前工作流里确认过中文 spec 后，AI 才能进入实现或修改文件。
- 如果实现中发现影响区域变化，AI 必须说明新增或移除的范围，并在最终交付中记录。
- spec 确认只授权按规格开发，不授权 merge-back；合回开发者分支必须在实现和验证汇报后再次明确询问。

## 安装方式

插件设计原则见 `docs/design-principles.md`，真实使用场景见 `docs/usage-scenarios.md`。

### Codex Plugin

本仓库已经包含 `.codex-plugin/plugin.json`，可以作为 Codex plugin 源码仓库分发。

Codex 读取 plugin 后，会加载 `plugin.json` 中声明的：

```json
{
  "skills": "./skills/"
}
```

因此安装的是一个 plugin 和一个主 Router；阶段规则由 Router 从自身目录按需读取。

详细说明见 `adapters/codex/install.md`。

### Codex Skill 直装

如果暂时不使用 plugin，也可以只把 `skills/ai-dev-protocol/` 安装到 `~/.codex/skills/ai-dev-protocol/`。它已包含全部内部阶段规则，但没有 plugin 卡片和 marketplace 分发能力。

### Claude Code

本仓库包含 `.claude-plugin/plugin.json`。由于根目录 `skills/` 只有主 Router，Claude Code 也只发现这一个入口；内部阶段文件作为 Router 的支持资源读取。若项目暂不走 Claude plugin 安装流程，也可以将 `adapters/claude-code/CLAUDE.snippet.md` 合并到目标项目的 `CLAUDE.md`。

### Cursor

复制 `adapters/cursor/ai-dev-protocol.mdc` 到目标项目的 `.cursor/rules/`。

### 通用 AI 工具

引用 `adapters/generic/AI_DEV_PROTOCOL.md`，并要求 AI 在代码修改、需求实现、修复、提交和交付场景遵守协议。

## 阶段计划

### 第一阶段：最小可用版本

完成 Codex plugin manifest、单 Router 与内部阶段模块、模板和 Codex/Claude Code/Cursor 适配文件。

### 第二阶段：真实项目试点

选择 1-2 个需求，用 Codex 或 Claude Code 跑完整流程，记录 AI 是否能稳定遵守规则。

### 第三阶段：规则收敛

根据试点结果优化触发条件、检查清单、模板措辞和交付格式。

### 第四阶段：团队推广

把仓库接入团队项目，形成复制/安装说明，约定版本更新方式，并视需要在单独仓库维护团队 plugin marketplace。

## 可持续迭代

- 使用 `CHANGELOG.md` 记录版本变化。
- 使用 `docs/iteration-guide.md` 约定反馈收集、版本号、发布检查和新增阶段模块判断标准。
- 每次真实项目试点后，优先修改最小相关 skill，避免把规则堆回总入口。
- 当新增独立阶段时再创建新的内部 phase 模块；阶段内规则变化优先更新已有模块。只有确实需要新的用户入口时才新增可发现 skill。

## 验收标准

1. 团队成员可以通过 GitHub 拉取并使用 `ai-dev-protocol`。
2. Codex 和 Claude Code 只发现主 Router，阶段模块由 Router 按需读取。
3. Claude Code 和 Cursor 能通过插件入口或适配文件读取核心规则。
4. AI 能稳定做到一需求一工作单元、一 spec 一范围。
5. 开发者分支支持多个 AI 分支并行开发，并在开发者逐次明确授权后 squash merge 回开发者分支。
6. 单一小型团队流程完整走通 spec 文档提交、本地 plan 未追踪、实现提交、验证审查、merge-back 授权、squash merge-back 和 handoff。
7. 最终交付包含验证结果、spec 文档状态、plan/goals 完成情况、subagent / 独立审查或替代自检结果，API 变更包含 Apifox sync summary；需要录入 Apifox 时可输出接口清单和数据模型 JSON Schema 清单。
8. 开发者在开发者分支上主导 review、联调、检查和后续合并。
9. 用户接受的低风险小修改可不创建 workflow 产物，并明确由用户完成最终验证。
