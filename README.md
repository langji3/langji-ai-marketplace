# Langji AI Marketplace

团队 AI 开发插件分发仓库。规则的唯一源仓库是 [ai-dev-protocol](https://github.com/langji3/ai-dev-protocol)；这里保存经过检查、可追溯到 Git 提交的发布快照。

| 插件 | 版本 | 接入方式 |
| --- | --- | --- |
| AI Dev Protocol | 2.2.2 | Codex / Claude Code 原生 plugin，Cursor / 通用工具完整项目包 |

安装指南：[Codex](docs/install-codex.md)、[Claude Code](docs/install-claude-code.md)、[Cursor](docs/install-cursor.md)。手动接入必须包含完整 vendor 资源；复制单个 adapter 只获得摘要。

本次实施结果、验证证据与未覆盖环境见 [2.2.0 验证记录](docs/validation/20260907-release-report.md)。

Windows CI 路径兼容性修复见 [2.2.1 修复记录](docs/validation/20260907-windows-ci-fix.md)。跨对话与并行需求兼容性修正及本次验证见 [2.2.2 发布记录](docs/validation/20260911-conversation-compatibility.md)。

## 维护与校验

需要 Python 3.11+ 和 Git。源仓库先验证、更新版本并提交，再在本仓库根目录同步：

~~~shell
python scripts/sync_plugin.py --source-path ../ai-dev-protocol --source-ref HEAD --expected-commit <完整提交SHA> --dry-run
python scripts/sync_plugin.py --source-path ../ai-dev-protocol --source-ref HEAD --expected-commit <完整提交SHA>
python scripts/validate_marketplace.py
python -m unittest discover -s tests -v
~~~

PowerShell 5.1 / 7 入口仍为 scripts/sync-ai-dev-protocol.ps1，支持 -SourcePath、-SourceRef、-ExpectedCommit、-DryRun 和 -Recover。默认远端模式读取源仓库 main，在 tmp/source-cache/ai-dev-protocol.git 使用 bare cache，不重置工作目录。详见 [更新与恢复策略](docs/update-policy.md)。

同步会先导出并校验临时快照，再更新插件、catalog 和 Claude 索引，生成 [来源记录](catalog/releases/ai-dev-protocol.json)。相同版本下语义内容变化会被拒绝。每次发布仍需审查并按授权提交、合回和推送。

## 文件职责

- plugins/ai-dev-protocol/：源仓库允许发布文件的快照。
- .agents/plugins/marketplace.json：Codex 安装入口和策略。
- .claude-plugin/marketplace.json：Claude Code 安装入口和版本。
- catalog/plugins.json、catalog/releases/：插件目录、源提交和规范化文件摘要。
- scripts/、tests/、.github/workflows/：分发维护工具、离线恢复测试和 Windows/Linux CI。

多文件发布使用恢复日志，不能承诺突然中断时所有读者都看不到中间状态。未完成事务会阻断新同步和校验；恢复时保护中断后的人工修改。

新增插件需独立定义发布约束，当前脚本只维护 ai-dev-protocol；见 [新增插件指南](docs/add-plugin-guide.md)。
