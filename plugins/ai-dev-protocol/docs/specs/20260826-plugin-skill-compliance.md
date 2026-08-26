# AI Dev Protocol 插件技能合规与 Apifox CLI 同步 Spec

## 背景与目标

当前 `ai-dev-protocol` 插件的 manifest 与 marketplace 包装可以通过校验，但内部 phase 使用嵌套 `SKILL.md`，导致 Codex 将 phase 作为独立技能暴露，与“单 Router、phase 为内部模块”的产品原则冲突。同时存在 `ai-commit-rules` frontmatter 校验失败、Router 缺少独立 Apifox / 纯讨论路由、模板资源链接不明确，以及源仓库新 Apifox 规则尚未同步到 marketplace 发布包的问题。

本次目标是让插件满足 `skill-creator` 与 `plugin-creator` 的结构和验证要求，使源仓库与 marketplace 发布包在用户可见行为上保持一致，并在保留手工清单模式的同时增加受控的 Apifox CLI 同步模式。

## 分支

- 当前状态：两个开发者汇总分支分别创建同名 AI 分支
- 当前分支：`ai/20260826-langji-plugin-compliance`
- AI 分支：`ai/20260826-langji-plugin-compliance`
- 开发者分支：`main`
- 涉及仓库：`ai-dev-protocol`、`langji-ai-marketplace`

## 本次范围

- 将 `phases/*/SKILL.md` 转为不会被技能发现器注册的内部 phase 资源，并移除内部 skill frontmatter。
- 更新 Router，使其通过明确的相对 Markdown 链接按需读取内部 phase。
- 增加 Apifox-only standalone route：仅生成 Apifox 清单时跳过分支、spec、实现、提交和 merge-back 流程。
- 将 Apifox-only route 拆分为只读清单与 CLI 同步两种模式；用户要求实际同步时，进入独立的外部写入流程。
- CLI 同步要求用户指定已有 Apifox 模块作为业务边界；AI 根据接口职责规划稳定的接口目录和数据模型目录，并在写入前展示目录映射与资源操作计划。
- 接口目录与数据模型目录使用 Apifox 各自独立的 folder 树；先同步后端响应模型，再同步引用这些模型的接口。
- 保留“请求不建立复用数据模型”的规则：JSON Body 使用接口内联 JSON Schema，Query 使用接口参数；手工清单模式继续提供 Query 批量编辑 CSV，CLI 模式直接生成并校验 endpoint payload。
- CLI 写入前检查当前命令帮助和动态 `cli-schema`，读取现有资源并解析真实 ID；禁止猜测未公开的 `moduleId`、`folderId` 或 payload 字段。
- CLI 同步采用幂等策略：默认按稳定接口标识与模型名更新或创建，不删除、不清理、不合并 Apifox 分支；冲突与歧义先进入待确认项。
- CLI 实际写入前单独确认目标 project、已有 module、Apifox branch 和操作计划；写入后回读验证。Token 不进入聊天、日志、仓库文件或交付物。
- 增加明确的 discussion-only guard：用户明确不写代码时不创建开发工作流产物。
- 修正 `main` 分支分类的重复表达，使“未确认时阻断、确认后作为开发者汇总分支”只有一个判定入口。
- 将 phase 内的模板和后续 phase 引用改为可发现的相对 Markdown 链接，包括 `local-plan.md`。
- 保留并纳入当前未提交的 Apifox 请求参数 / 响应模型规则更新。
- 将 canonical source 同步到 `langji-ai-marketplace/plugins/ai-dev-protocol`，更新插件版本与必要发布说明。

## 非目标

- 不改变业务项目的 API、数据库、认证、权限或运行时代码。
- 不新增 MCP、app、hook、包装脚本依赖或 UI 资产；Apifox CLI 作为用户环境中的可选外部能力，不由插件静默安装。
- 不修改个人 Codex marketplace 配置或已安装插件缓存。
- 不在本次开发与验证中登录 Apifox、安装 CLI、创建 Apifox 模块、写入真实 Apifox 项目或合并 Apifox 分支。
- 不执行 merge-back、发布远端版本或推送远端分支。
- 不重写与本次技能发现、路由、Apifox 和发布一致性无关的工作流规则。

## 影响区域

- skills：主 Router、8 个内部 phase 资源及其链接；Apifox phase 新增只读清单 / CLI 同步模式与授权边界。
- templates：spec、plan、handoff、Apifox 模板的引用路径和现有 Apifox 内容。
- references：新增精简的 Apifox CLI 运行时规则，记录项目、分支、目录树、动态 schema、幂等写入与凭据安全要求。
- docs/adapters：所有仍引用 `phases/*/SKILL.md` 或描述 phase 为公开技能的文案。
- manifests：canonical 与 marketplace 的 `.codex-plugin/plugin.json` 版本。
- marketplace：`plugins/ai-dev-protocol/**` 发布副本。
- API：无业务 API 变更。
- 数据库：无变更。
- 配置：插件不保存凭据；运行时可读取用户已有的 `.apifox/settings.json` 获取 projectId，但不得写入或泄露敏感信息。

## 范围变化处理方式

- 若发现新的 phase 引用、发布清单或校验入口必须同步，先说明并仅纳入维持单 Router 与发布一致性所必需的文件。
- 若需要修改外部个人配置、插件缓存或执行安装 / 发布，停止并单独请求授权。
- 若当前 CLI 未暴露模块选择能力，则不得把模块名臆造为 CLI 参数；先通过当前 `--help` 与 `cli-schema` 核实。无法把资源可靠归入指定模块时，降级为只读同步计划并说明阻断点。

## 实现思路

1. 以 canonical `ai-dev-protocol` 为源，将每个内部 phase 的入口从 `SKILL.md` 改为普通 phase 文档，保留各 phase 目录和模板相对位置。
2. 在 Router 中建立清晰的 discussion-only / Apifox read-only / Apifox CLI sync / quick-fix / full-flow 路由，并使用 Markdown 链接实现渐进披露。
3. 重写 Apifox phase 的模式与执行门：确定 project、已有 module 与 Apifox branch，读取现状，推导双目录树，获取并校验动态 payload schema，展示操作计划，取得外部写入确认，按“模型后接口”执行并回读验证。
4. 把官方公开文档未确认的模块 / 目录 payload 字段留给运行时 CLI schema 解析；默认不采用无法定向模块和目录的 blanket `apifox import`。
5. 更新 phase 之间的 next-step 链接、模板链接和 Apifox CLI 参考资料，确保资源可发现且不会被自动注册为技能。
6. 运行全仓引用检索，修正文档、适配器、目录树和发布说明。
7. 将 canonical 插件目录同步到 marketplace，提升兼容版本并验证两侧语义一致。

## 实现计划与审查方式

- plan/goals 拆分：内部 phase 结构；Router 路由；Apifox CLI 安全同步；资源链接；文档与 adapter；marketplace 同步；验证。
- 适合 subagent：跨仓库引用定位、发布副本差异核验、独立行为前向测试。
- 独立审查：使用全新 subagent 覆盖 Quick Fix、非平凡开发、Apifox 只读清单、Apifox CLI 同步、discussion-only 五个场景。
- 降级自检：逐文件校验、全仓旧路径否定检索、canonical / marketplace 目录比较。

## 验证方式

- 对唯一公开的 `skills/ai-dev-protocol/SKILL.md` 运行 `quick_validate.py`。
- 对 canonical 与 marketplace 插件分别运行 `validate_plugin.py`。
- 检索并确认插件目录下只有主 Router 一个 `SKILL.md`。
- 检索并确认不存在旧的 `phases/*/SKILL.md` 引用。
- 比较 canonical 与 marketplace 的插件目录，除预期发布位置差异外内容一致。
- 运行 `git diff --check`，检查两个仓库的 staged / unstaged 范围。
- 静态演练 CLI 缺失、未登录、模块能力不可核实、目录冲突、payload 校验失败、用户未授权写入、同步成功回读七类分支，不连接真实 Apifox 项目。
- 独立前向测试五类 Router 路由，不执行真实业务修改、Apifox 写入或 merge-back。

## 风险与注意事项

- phase 文件重命名会使旧路径失效，必须同步 Router、docs、adapters 和模板引用。
- installed cache 不在本次范围；新结构只有在后续安装新版插件或新会话加载后生效。
- 两个仓库需要保持同一插件版本和同一发布内容，避免再次出现 source / package 漂移。
- 源仓库已有未提交 Apifox 内容，实施时必须保留并纳入本次分支，不能回退。
- Apifox 产品中的“模块”与 CLI 的 `folder` 不是同一概念；官方公开 CLI 文档尚未证明模块管理或 `import` 定向模块能力，运行时必须以已安装版本的帮助和动态 schema 为准。
- CLI 会修改外部项目状态。用户在对话中提出设计需求不等于授权本次开发过程写入真实项目；每次真实同步仍需明确目标与操作授权。
