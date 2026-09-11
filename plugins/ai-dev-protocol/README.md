# AI Dev Protocol

面向小型团队的 AI 辅助开发流程插件。当前版本：`2.2.2`。

独立维护规则，通过 Langji AI Marketplace 分发可追溯快照。Codex / Claude Code 使用一个公开 Router；Cursor 和通用工具通过完整项目资源包接入。

## 工作路径

| 请求 | 行为 |
| --- | --- |
| 讨论、解释、review、执行方案 | 只读回答，不创建开发产物 |
| Apifox 摘要、录入清单或同步计划 | 直接选择 Apifox 模式；实际写入独立授权 |
| 已授权的低风险小修改 | 当前合适分支聚焦修改和自检，用户最终验证 |
| 功能、非简单修复或风险不明确 | 开发者分支 -> 独立 AI 分支 -> 中文 spec -> 本地 plan -> 实现/验证/审查 -> 提交 -> 授权合回 -> 交付 |

Quick Fix 排除 API/schema、数据库迁移、认证安全、依赖构建/CI、发布版本、跨模块和分支集成变化。用户明确指令、项目业务规则和宿主约束优先。

完整流程保留开发者分支作为需求汇总站。默认 AI 分支为 ai/{yyyyMMdd}-{developer}-{short-desc}；明确的仓库/宿主命名约定可覆盖默认。并发实现使用独立工作目录。用户确认分支只确定来源；确认 spec 才授权按范围实现；合回与 Apifox 写入有各自的具体方案授权。

对明确方案回复“确认”“可以”“OK”即可按上下文生效。同一内容从对话落成 spec 不重复确认；目标或范围实质改变时只确认变化部分。

跨对话或并行需求按用户已有安排协作。插件保持对话已分配的职责，接续已有分支/spec 和可核实的确认，不因加载插件重复派发；“一个需求”约束实现单元，缺失决策只暂停受影响工作。用户要求回报其他对话时复用交付摘要，如实说明投递结果。插件不内建协调模式或通知机制。

## 唯一入口和内部资源

[Router](skills/ai-dev-protocol/SKILL.md) 选择以下内部阶段：
需求澄清、分支、spec、实现、commit、merge-back、handoff、Apifox。
只有一个 SKILL.md；8 个 PHASE.md 由 Router 按需读取，不要求用户编排阶段。

spec 存在 docs/specs/ 并进入 Git；完整流程本地 plan 存在 ignored docs/plans/，保留目标、确认出处、来源/验证提交和恢复起点。确认状态以对话证据为准，不由文件自行授权。恢复与并发细则由 [恢复资源](skills/ai-dev-protocol/references/recovery.md) 维护。

## 安装、更新与卸载

- [Codex](adapters/codex/install.md)：原生 plugin 或完整 Router skill。
- [Claude Code](adapters/claude-code/install.md)：原生 plugin 或完整项目资源包。
- [Cursor](adapters/cursor/install.md)：短 rule + 完整项目资源包。
- [通用工具](adapters/generic/install.md)：完整资源的明确读取入口。
- [完整项目包操作说明](docs/project-installation.md)：生成、安装、更新、自检和卸载。

复制单个 adapter 只获得摘要，不能声称完整规则已安装。GitHub 链接也不等于资源已加载。

## 本地质量检查

需要 Python 3.11+ 和 Git，无第三方 Python 依赖。以下维护命令在源仓库根目录运行；发布快照只包含 validate_plugin.py 和 build_bundle.py：

~~~shell
python scripts/validate_plugin.py
python -m unittest discover -s tests -v
python scripts/evaluate.py list
python scripts/build_bundle.py --output dist/project-bundle
~~~

静态检查验证版本、入口、资源和发布清单。行为场景检查动作/状态证据；人工或独立代理演练与真实平台运行分别记录。CI 执行离线测试，不能代替真实工具试点。

## 发布

1. 修改 source 的最小相关规则和测试。
2. 更新两个 manifest 的相同版本与 CHANGELOG；确认兼容性。
3. 执行上述检查、行为回归和必要真实工具烟测；记录未覆盖环境。
4. 提交源仓库，记录 commit。
5. 在 marketplace 使用该源提交同步并校验。插件快照中包含自检与完整包生成脚本，不包含 tests、CI、本地 plan 或维护用评测脚本。
6. 审阅两仓变更；合回、推送和发布按明确授权执行。

详见 [设计原则](docs/design-principles.md)、[迭代指南](docs/iteration-guide.md) 和 [使用场景](docs/usage-scenarios.md)。
