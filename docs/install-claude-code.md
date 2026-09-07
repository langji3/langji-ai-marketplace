# 在 Claude Code 安装

原生 marketplace 入口为 .claude-plugin/marketplace.json，插件源为 plugins/ai-dev-protocol/。

~~~text
/plugin marketplace add langji3/langji-ai-marketplace
/plugin install ai-dev-protocol@langji-ai-marketplace
/reload-plugins
~~~

更新已有安装：

~~~text
/plugin marketplace update langji-ai-marketplace
/plugin update ai-dev-protocol@langji-ai-marketplace
/reload-plugins
~~~

使用宿主支持的对应菜单/命令，开始新会话，核对插件版本与唯一 Router；仓库更新不保证已有插件缓存自动刷新。卸载通过插件管理界面/命令完成，保留项目原有 CLAUDE.md 规则。

无法使用原生 marketplace 时，按 [完整项目包指南](../plugins/ai-dev-protocol/docs/project-installation.md) 生成并安装 vendor/ai-dev-protocol/，再把生成 CLAUDE.md 的标记段合入项目文件。只合入 snippet 不具备完整规则。详细说明见 [Claude adapter](../plugins/ai-dev-protocol/adapters/claude-code/install.md)。
