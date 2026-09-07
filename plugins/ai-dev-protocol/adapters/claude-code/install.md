# Claude Code 安装与更新

推荐通过团队 marketplace 安装原生 plugin，唯一公开入口为 ai-dev-protocol，阶段由 Router 按相对链接加载。

~~~text
/plugin marketplace add langji3/langji-ai-marketplace
/plugin install ai-dev-protocol@langji-ai-marketplace
~~~

更新已安装插件后重新加载：
~~~text
/plugin marketplace update langji-ai-marketplace
/plugin update ai-dev-protocol@langji-ai-marketplace
/reload-plugins
~~~

命令以本机 /plugin 帮助为准；无法使用原生插件时按 [完整项目资源包](../../docs/project-installation.md) 安装 vendor 资源并合并 CLAUDE.snippet.md。GitHub 地址不等于本地依赖已安装。

保留项目既有业务/架构规则，不重复安装同名 skill。核验版本后用新会话测试实际资源读取和行为。手工包升级与卸载见链接；原生 plugin 卸载使用宿主 plugin 管理。
