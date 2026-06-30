# AI Dev Protocol

AI Dev Protocol is a team workflow protocol for AI-assisted software development.

AI Dev Protocol 是一套面向团队的 AI 辅助开发流程规约，用于根据当前分支命名风格自动选择协作模式：需求分支直接开发，个人开发分支则创建独立 AI 分支并在完成后汇总回开发者分支。

## 项目定位

`ai-dev-protocol` 是一个可独立维护、可通过 GitHub 拉取、可被多个 AI 编程工具复用的 workflow skills/plugin 仓库。它不是单个项目里的提示词，也不是普通规范文档。

本仓库采用类似 Superpowers 的组织方式：

- `.codex-plugin/plugin.json` 声明 Codex plugin。
- `.claude-plugin/plugin.json` 声明 Claude Code plugin 元数据。
- `skills/` 下每个子目录都是一个独立 skill。
- `ai-dev-protocol` 是总入口和路由 skill。
- 其他 `ai-*` skills 分别负责需求、分支、spec、范围控制、提交、merge-back、交付和 Apifox 同步。

## 核心工作流

AI Dev Protocol 先查看当前分支命名风格，再选择工作流。

需求分支模式适用于公司常见复杂 Git 流：

```text
feature/order-filter
fix/user-api-field
hotfix/login-timeout
task/image-job-create
JIRA-123-order-export
```

这个模式下：

- 当前分支已经表达一个明确需求、修复、任务或 hotfix。
- AI 直接在当前需求分支工作，不额外创建 `ai/...` 分支。
- AI 完成实现和验证后，开发者在该需求分支上主导 review、自测、联调和 PR。
- 不执行 merge-back。

个人分支模式面向小型团队的个人开发分支流：

```text
developer/<name>
dev/<name>
<name>/dev
  -> ai/{yyyyMMdd}-{developer}-{short-desc}
  -> ai/{yyyyMMdd}-{developer}-{another-desc}
  <- squash merge back to developer/<name>
```

这个模式下：

- 开发者个人分支是多个 AI 需求的汇总站。
- 一个 `ai/...` 分支只处理一个明确需求。
- AI 完成实现和验证后，默认 squash merge 回开发者个人分支。
- 开发者在个人分支上主导 review、联调、检查和后续合并。
- AI 在 merge-back 后转为辅助身份：解释变更、修 review 问题、补测试、整理 Apifox 摘要。

AI 不应直接在 `main`、`master`、`dev`、`develop`、`site`、`staging`、`test`、`prod`、`production` 等主干或环境分支上实现，除非用户明确确认这是团队规则。

## Codex 安装后的 Skills

Codex 以 plugin 形式安装后，会从 `skills/` 加载多个 workflow skills：

```text
ai-dev-protocol
ai-requirement-intake
ai-branch-workflow
ai-spec-writing
ai-implementation-scope
ai-commit-rules
ai-merge-back
ai-handoff
ai-apifox-sync
```

在 Codex plugin 环境中，它们可能显示为带插件前缀的名称，例如 `ai-dev-protocol:ai-spec-writing`。

## 核心目标

1. 一个 AI 工作单元只处理一个明确需求。
2. AI 在动手前必须先确认需求范围。
3. AI 在实现前先根据当前分支命名风格判断分支模式。
4. 当前分支是明确需求分支时，直接在该分支工作并跳过额外 AI 分支。
5. 当前分支是开发者个人分支时，从该分支创建独立 `ai/...` 分支，以支持多个需求并行开发。
6. AI 不直接在主干或环境分支上实现。
7. spec 使用中文，代码标识符、API 路径、表名、配置键保持英文。
8. commit message 使用中文，需求用 `feat:`，修改用 `fix:`。
9. 不混入无关重构、格式化、依赖变更。
10. 不提交单独 plan 文件或 `.superpowers/` 工作流产物，除非明确要求。
11. 最终交付必须包含测试/验证说明。
12. 个人分支模式下，AI 验证完成后 squash merge 回开发者个人分支。
13. 最终由开发者主导 review、联调、检查和后续合并。
14. 如有 API 变更，最终交付必须包含 Apifox sync summary。

## 目录结构

```text
ai-dev-protocol/
  README.md
  CHANGELOG.md
  docs/
    iteration-guide.md
    team-collaboration-guide.md
  .codex-plugin/
    plugin.json
  .claude-plugin/
    plugin.json

  skills/
    ai-dev-protocol/
      SKILL.md
    ai-requirement-intake/
      SKILL.md
    ai-branch-workflow/
      SKILL.md
    ai-spec-writing/
      SKILL.md
      templates/
        requirement-spec.md
    ai-implementation-scope/
      SKILL.md
    ai-commit-rules/
      SKILL.md
    ai-merge-back/
      SKILL.md
    ai-handoff/
      SKILL.md
      templates/
        handoff-summary.md
    ai-apifox-sync/
      SKILL.md
      templates/
        apifox-sync-summary.md

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

1. 需求进入：使用 `ai-requirement-intake` 判断需求是否清楚，是否是一个独立 requirement。
2. 分支判断：使用 `ai-branch-workflow` 根据当前分支命名风格选择需求分支模式、个人分支模式或停止在主干/环境分支。
3. 规格说明：使用 `ai-spec-writing` 写中文 spec，明确目标、范围、非目标、影响文件、验证方式。
4. 实现前确认：用户确认 spec 后，AI 才进入实现或修改阶段。
5. 范围控制：使用 `ai-implementation-scope` 控制改动范围，不做无关重构、格式化、依赖升级。
6. 验证：根据项目情况运行测试、构建、静态检查，不能运行时要说明原因。
7. 提交规则：使用 `ai-commit-rules` 检查中文 commit message，并按 `feat:` / `fix:` 分类。
8. Merge-back：个人分支模式下使用 `ai-merge-back` 将 AI 分支 squash merge 回开发者个人分支；需求分支模式跳过。
9. 最终交付：使用 `ai-handoff` 输出变更摘要、分支模式、merge-back 状态、实现范围记录、范围变化说明、验证结果、风险说明和开发者接管说明。
10. API 变更：使用 `ai-apifox-sync` 输出 Apifox sync summary。

### 对话式需求入口

开发人员通常会先用自然语言讨论模块设计，例如“我现在要设计一个模块”“我们目前的想法是”“下一步会做什么”。这类对话如果可能进入代码实现，也属于正式流程入口。

- AI 应先把自然讨论收口为需求目标、范围、非目标、影响区域和验证方式。
- 用户确认“个人分支”或“需求分支”只表示分支模式确认，不表示允许实现。
- 个人分支模式下，即使已经创建 `ai/...` 分支，也必须先输出中文 spec 并等待用户确认。
- 只有在当前工作流里确认过中文 spec 后，AI 才能进入实现或修改文件。
- 如果实现中发现影响区域变化，AI 必须说明新增或移除的范围，并在最终交付中记录。

## 安装方式

团队协作落地说明见 `docs/team-collaboration-guide.md`，其中包含团队插件市场的使用方式。

### Codex Plugin

本仓库已经包含 `.codex-plugin/plugin.json`，可以作为 Codex plugin 源码仓库分发。

Codex 读取 plugin 后，会加载 `plugin.json` 中声明的：

```json
{
  "skills": "./skills/"
}
```

因此安装的是一个 plugin，但可用的是多个 workflow skills。

详细说明见 `adapters/codex/install.md`。

### Codex Skills 直装

如果暂时不使用 plugin，也可以把 `skills/` 下的每个 skill 子目录分别安装到 `~/.codex/skills/`。这种方式同样会得到多个 skills，但没有 plugin 卡片和 marketplace 分发能力。

### Claude Code

本仓库包含 `.claude-plugin/plugin.json`，可作为 Claude Code plugin 源码仓库使用。若项目暂不走 Claude plugin 安装流程，也可以将 `adapters/claude-code/CLAUDE.snippet.md` 合并到目标项目的 `CLAUDE.md`。

### Cursor

复制 `adapters/cursor/ai-dev-protocol.mdc` 到目标项目的 `.cursor/rules/`。

### 通用 AI 工具

引用 `adapters/generic/AI_DEV_PROTOCOL.md`，并要求 AI 在代码修改、需求实现、修复、提交和交付场景遵守协议。

## 阶段计划

### 第一阶段：最小可用版本

完成 Codex plugin manifest、多阶段 workflow skills、模板和 Codex/Claude Code/Cursor 适配文件。

### 第二阶段：真实项目试点

选择 1-2 个需求，用 Codex 或 Claude Code 跑完整流程，记录 AI 是否能稳定遵守规则。

### 第三阶段：规则收敛

根据试点结果优化触发条件、检查清单、模板措辞和交付格式。

### 第四阶段：团队推广

把仓库接入团队项目，形成复制/安装说明，约定版本更新方式，并视需要在单独仓库维护团队 plugin marketplace。

## 可持续迭代

- 使用 `CHANGELOG.md` 记录版本变化。
- 使用 `docs/iteration-guide.md` 约定反馈收集、版本号、发布检查和新增 skill 判断标准。
- 每次真实项目试点后，优先修改最小相关 skill，避免把规则堆回总入口。
- 当新增独立阶段时再创建新 skill；阶段内规则变化优先更新已有 skill。

## 验收标准

1. 团队成员可以通过 GitHub 拉取并使用 `ai-dev-protocol`。
2. Codex 能以 plugin 方式读取多个 workflow skills。
3. Claude Code 和 Cursor 能通过适配文件读取核心规则。
4. AI 能稳定做到一需求一工作单元、一 spec 一范围。
5. 个人分支模式支持多个 AI 分支并行开发并 squash merge 回开发者个人分支。
6. 最终交付包含验证结果，API 变更包含 Apifox sync summary。
7. 开发者在个人分支或需求分支上主导 review、联调、检查和后续合并。
