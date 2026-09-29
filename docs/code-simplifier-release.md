# Code Simplifier 来源与更新

`code-simplifier` 的规则在独立源码项目维护（当前本地为与 `ai-dev-protocol` 同级的 `code-simplifier` Git 仓库）；`plugins/code-simplifier/` 是版本化快照。当前没有远端源码地址。不要在快照里单独改规则，也不要用只支持 `ai-dev-protocol` 的 `scripts/sync_plugin.py` 更新它。

## 一次更新

1. 在源码项目修改，按需提高两个插件清单的相同版本，运行 `python scripts/validate.py` 和 `tests/scenarios.md` 中的决策回归，并提交。记下完整源码 commit。若有 Codex 的 skill-creator/plugin-creator 工具，也运行各自的格式校验。
2. 从该提交导出 `.codex-plugin/plugin.json`、`.claude-plugin/plugin.json`、`skills/code-simplifier/SKILL.md`、`LICENSE`、`NOTICE.md`、`README.md`、`scripts/validate.py` 和 `tests/scenarios.md` 到 `plugins/code-simplifier/`。仅复制这八个文件，不带源码的 `.git`、本地计划或 spec。源提交应与导出的内容一致，不能把未提交的工作目录改动混入快照。
3. 同步更新 `.agents/plugins/marketplace.json`、`.claude-plugin/marketplace.json`、`catalog/plugins.json` 中的插件条目和版本；将完整源码 commit、版本及上述八个文件按 UTF-8、LF 规范化后的 SHA-256 写入 `catalog/releases/code-simplifier.json`。保持其它插件条目不变。
4. 在 marketplace 根目录运行 `python scripts/validate_code_simplifier.py --source-path <源码项目目录>`、`python scripts/validate_marketplace.py`、`python -m unittest discover -s tests -v` 和 `git diff --check`，审阅快照及索引差异。前一个检查可在未来源码 HEAD 前进后仍核对记录的历史提交；不传 `--source-path` 时只验证本地快照与记录。

更新跨多个文件，不能承诺中断时外部读者看不到中间状态。若途中失败，先保留当前 diff，核对记录提交及实际文件，再从同一源码提交补齐或用 Git 恢复本次未完成的修改；不要调用 AI Dev Protocol 的 `--recover` 来处理本插件。合回、推送或面向用户发布仍按项目既有授权流程进行。
