# 在 Codex 安装

在 Codex 插件页面添加本仓库的本地路径或 Git 来源，选择 Langji AI Marketplace 中的 AI Dev Protocol 并安装。开始新任务，确认只显示 ai-dev-protocol 这个公开 Router；8 个内部 phase 应作为资源存在。

安装入口为 .agents/plugins/marketplace.json，指向 plugins/ai-dev-protocol/。核对已安装 manifest 的版本与本仓库 [来源记录](../catalog/releases/ai-dev-protocol.json) 的版本一致。更新 marketplace 后按宿主提供的更新或重新安装操作刷新插件，再开始新任务；不要假定运行中的任务自动重读规则。

手动 skill 与完整项目包替代方式、检查和卸载见 [源插件安装指南](../plugins/ai-dev-protocol/adapters/codex/install.md)。避免同一项目重复启用原生 plugin 与另一份同名 skill。

维护者可运行 python scripts/smoke_codex.py --codex <codex可执行文件>，在临时 CODEX_HOME 中验证本地安装和缓存中的唯一 Router。该烟测不调用模型，不证明新任务中的实际行为；不会改个人插件配置。

