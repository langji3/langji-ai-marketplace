# 在 Codex 安装

在 Codex 插件页面添加本仓库的本地路径或 Git 来源，按需单独安装 Langji AI Marketplace 中的 AI Dev Protocol 和 Code Simplifier。Code Simplifier 只有一个公开 `code-simplifier` skill，普通代码审查任务也应能发现它；AI Dev Protocol 仍只有一个公开 Router，8 个内部 phase 是资源。

安装入口为 .agents/plugins/marketplace.json，分别指向 plugins/ai-dev-protocol/ 和 plugins/code-simplifier/。核对已安装 manifest 的版本与各自的 [AI Dev Protocol 来源记录](../catalog/releases/ai-dev-protocol.json)、[Code Simplifier 来源记录](../catalog/releases/code-simplifier.json) 一致。更新 marketplace 后按宿主提供的更新或重新安装操作刷新插件，再开始新任务；不要假定运行中的任务自动重读规则。

手动 skill 与完整项目包替代方式、检查和卸载见 [源插件安装指南](../plugins/ai-dev-protocol/adapters/codex/install.md)。避免同一项目重复启用原生 plugin 与另一份同名 skill。

维护者可运行 python scripts/smoke_codex.py --codex <codex可执行文件>，在临时 CODEX_HOME 中验证 AI Dev Protocol 的本地安装和缓存中的唯一 Router。该烟测不覆盖 Code Simplifier，也不调用模型；不会改个人插件配置。Code Simplifier 的快照核对见[维护说明](code-simplifier-release.md)。

