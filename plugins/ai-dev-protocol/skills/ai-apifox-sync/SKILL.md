---
name: ai-apifox-sync
description: Create Apifox sync summaries for AI Dev Protocol API changes. Use when a task changes endpoints, request parameters, response schemas, status codes, error codes, authentication, permissions, headers, examples, or observable API behavior.
---

# AI Apifox Sync

Use whenever API behavior or contracts changed.

## Triggers

- Endpoint added, removed, or changed.
- Request path/query/header/cookie/body changed.
- Response body, status code, error code, or error response changed.
- Auth, permission, example, field meaning, compatibility, or observable behavior changed.

## Include

Use `templates/apifox-sync-summary.md` when structure helps.

- 变更类型
- 受影响 API
- Request 变更
- Response 变更
- 错误码或 status code 变更
- 权限或认证变化
- 兼容性说明
- Apifox 中需同步的文档、示例、Mock、测试用例

## No API Change

Use:

```text
Apifox sync summary：无 API 变更，无需同步。
```
