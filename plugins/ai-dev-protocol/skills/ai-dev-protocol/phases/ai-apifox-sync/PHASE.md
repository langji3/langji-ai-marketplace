# AI Apifox Sync

Use whenever API behavior or contracts changed, or when the user needs to enter a requirement/change into Apifox.

This internal phase has three modes:

- A final-delivery sync summary for API changes.
- An independent Apifox entry catalog capability that extracts affected interfaces and data models from a requirement, spec, diff, implementation, or change description.
- A gated Apifox CLI synchronization capability that plans directories and creates or updates models and endpoints in an existing user-selected Apifox module.

## Triggers

- Endpoint added, removed, or changed.
- Request path/query/header/cookie/body changed.
- Response body, status code, error code, or error response changed.
- Auth, permission, example, field meaning, compatibility, or observable behavior changed.
- User asks for Apifox entry, Apifox import or sync, interface list, API list, data model list, request/response model list, or affected API/model checklist.
- User provides a requirement or change and asks what should be recorded in Apifox.

## Modes

### Sync Summary

Use when final handoff only needs a short API change summary.

## Include

Use the [Apifox sync summary template](templates/apifox-sync-summary.md) when structure helps.

- 变更类型
- 受影响 API
- Request 变更
- Response 变更
- 错误码或 status code 变更
- 权限或认证变化
- 兼容性说明
- Apifox 中需同步的文档、示例、Mock、测试用例

### Apifox Entry Catalog

Use the [Apifox entry catalog template](templates/apifox-entry-catalog.md) when the user asks for a list that can be handed to the Apifox maintainer.

When the user asks for an Apifox-ready artifact, or when final delivery should provide a directly transferable API document, produce a complete "接口清单 + 响应数据模型" instead of only a short sync summary.

The catalog can be generated from:

- A confirmed requirement or Chinese spec.
- A code diff or implementation summary.
- A handoff summary.
- A natural-language change description.
- Existing controller/service/API files when available.

The output should be convenient for an Apifox maintainer to copy into Apifox:

- 公共信息：模块、Base Path、认证方式、返回结构、时间格式、变更类型、兼容性
- 影响范围清单：新增 / 修改 / 删除的接口、响应数据模型、错误码、权限
- 接口清单：接口名称、Method、Path、权限、请求参数、响应模型、变更类型
- 接口详情：说明、权限、Path / Query / Body、请求参数定义、响应模型、错误场景、兼容性；请求参数只在接口详情中描述，各接口独立、不共享、不入数据模型库；不输出独立的请求 / 响应 JSON 示例
- 响应数据模型库：重点收录接口实际返回涉及的全部后端数据模型，并完整给出 JSON Schema；保留代码中的真实类型名，不强制改名为 `*Vo`
- 枚举说明：字段、枚举值、含义
- Apifox 同步结论：新增 / 修改 / 删除接口数量，响应数据模型、权限、错误码、Mock、测试用例同步项

### Apifox CLI Sync

Use only when the user asks to write or synchronize resources into Apifox. Read [Apifox CLI runtime rules](references/apifox-cli.md) completely before running any CLI command.

This mode is separate from ordinary repository implementation. It may run as an Apifox-only standalone route without creating a Git branch, spec, plan, implementation commit, or merge-back artifact. Repository changes and Apifox external writes keep separate authorization gates.

#### Required target

Before planning a write, resolve:

- `projectId`: use the value explicitly supplied by the user or an existing `.apifox/settings.json`; never guess it.
- Existing Apifox module: the user must name or identify the module that owns the APIs and schemas. Do not silently create a module.
- Apifox branch: prefer an AI branch. Writing to `main` or another shared branch requires explicit authorization for that exact target.
- Change source: confirmed requirement, spec, diff, implementation, or explicitly selected API set.

Apifox product modules and CLI folders are different concepts. Current public CLI documentation does not establish a module-management command or a target-module option for blanket imports. Inspect the installed CLI's current `--help`, `agentHints`, and dynamic schemas. If the selected module cannot be resolved and assigned with evidence from the current CLI, stop before writing and deliver a read-only synchronization plan with the blocker.

#### Directory planning

- Infer a stable logical directory from the API's business responsibility, controller or route grouping, existing Apifox structure, and repository module/package names—in that order.
- Reuse the closest existing directory when its meaning is unambiguous. Do not create near-duplicate directories that differ only in punctuation, case, singular/plural, or translation.
- Maintain two independent directory trees: `endpoint` for interfaces and `schema` for response models. Apply the same logical business path to both when appropriate, but resolve their folder IDs independently.
- Show the proposed mapping `existing module -> logical directory -> endpoint folder / schema folder` before external writes. Mark uncertain names or placements as `待确认`.

#### Read, validate, authorize, write, verify

1. Confirm the CLI exists and inspect its current help. If missing, provide setup guidance; do not install it silently.
2. Run `apifox whoami` without exposing credentials. If it fails or returns no authenticated identity, stop before reading or writing project resources and provide login guidance. Never ask the user to paste a token into chat or place it in a repository command/file.
3. Read the target project, branch, folder trees, endpoints, and schemas. Resolve real resource IDs; never infer IDs from names alone.
4. Fetch the current `cli-schema` for every complex create/update payload and validate each local payload before use.
5. Build a dry operation plan containing target, directory mapping, create/update/skip operations, stable match keys, conflicts, and excluded destructive actions.
6. Immediately before mutation, obtain explicit approval for the exact project, existing module, Apifox branch, and operation plan. Discussion, catalog generation, repository spec confirmation, or repository implementation approval does not authorize an Apifox write.
7. Create missing response-model directories and response schemas first. Then create missing endpoint directories and endpoints that reference those schemas.
8. Read every changed resource back from the same project and branch. Compare identity, directory, request definition, response references, and relevant metadata with the plan.
9. Report created, updated, skipped, blocked, and verification-failed resources. Leave Apifox branch merge/review to the user.

#### Idempotency and conflict rules

- Match an endpoint by the CLI's stable resource ID when already known; otherwise use an unambiguous `Method + normalized Path` match within the selected module/branch. A title alone is not a stable key.
- Match a response schema by known resource ID or an unambiguous real backend type name within the selected module/branch.
- Update only the fields covered by the confirmed API change. Preserve unrelated Apifox metadata when the CLI payload supports partial or merge-safe updates.
- If zero or multiple candidates match unexpectedly, do not guess. Mark the resource `待确认` and exclude it from the write plan.
- Default actions are create, update, or skip. Never delete, prune, replace an entire module, merge a branch, or use destructive import conflict policies unless the user separately requests and authorizes that exact action.
- Do not use blanket `apifox import` for directory-aware synchronization unless the installed CLI explicitly proves it can target the selected existing module, directories, and branch with the required conflict behavior.

#### CLI payload mapping

- Request-side definitions remain owned by the endpoint. JSON Body uses an inline JSON Schema; Query, Path, Header, Cookie, form, and file parameters stay inline in the endpoint payload and never become reusable schemas.
- CLI mode does not generate Query CSV for execution; map Query fields directly into the validated endpoint payload. Query CSV remains a manual-entry aid in Apifox Entry Catalog mode.
- Create reusable Apifox schemas only for response-side backend models, including envelopes, containers, roots, nested types, inherited serialized fields, and transitively referenced models.
- Do not add standalone request or response JSON examples. Field-level examples may be retained only when they are known and accepted by the current CLI schema.
- Store temporary payload files outside tracked repository paths, remove them after use when safe, and never include tokens or secrets.

## Extraction Rules

- Separate confirmed facts from inferred items.
- If an API or model is likely affected but not confirmed, mark it as `待确认`.
- Keep code identifiers, API paths, field names, and enum values in their original English/case.
- Use Chinese for explanations, descriptions, and Apifox maintainer notes.

### Request side — interface parameters, not data models

- Do **not** create request-side data models for Path params, Query params, Headers, Cookies, form data, or Body. Describe them only inside the owning interface detail; never share or `$ref` request definitions across interfaces.
- For a JSON Body, provide an inline `Body JSON Schema`. The schema documents the body but is not entered into Apifox as a reusable data model.
- For Query params, provide an Apifox batch-edit CSV block instead of JSON Schema. Use comma mode with this exact column order: `参数名,类型,必需,示例值,固定参数值,说明`. Emit one parameter per line, use `true` / `false` for 必需, leave an unused fixed value empty, and follow standard CSV quoting when a value contains a comma, quote, or newline.
- For Path params, Headers, and Cookies, use compact inline parameter tables with name, type, required flag, example, and description. Include only categories that exist for the interface.
- Other request encodings such as form data or file upload remain inline in the interface detail using the representation most convenient for direct Apifox entry; they never enter the data-model library.

### Response side — complete backend response model library

- The interface detail states the actual backend response type and points to the **响应数据模型库**; do not duplicate the response schema inline there.
- Preserve the backend's real wrapper and model names (`BaseResponse<XxxVo>`, `Result<XxxDto>`, page types, or any project-specific equivalent). Do not invent `BaseResponse` or rename a model merely to fit the template.
- Include every model reachable from each interface response: envelopes, page/container models, root response objects, nested objects, inherited fields that are serialized, and array item models.
- Response models may reference each other via `$ref`. **Any model that is `$ref`-ed by another response model must also be fully given** in the library section; apply this transitively until no referenced response type is missing.
- Use `$ref` for response-model references (including array `items` and nested objects); do not duplicate the same model's fields inline in more than one place.
- The library contains **response-side models only**. Request parameters and request bodies are not part of it.

### Enums — inlined, not separate models

- Enum-backed fields (e.g. status fields) are inlined **inside the owning response-model field** using `enum` + `description`; do **not** create a separate enum model in the library.
- The 枚举说明 table is supplementary only and must stay consistent with the `enum` values inlined in each response model; it does not replace the inline `enum`.

### General

- Every response model in the library and every JSON Body must include a JSON Schema block. Query params use the Apifox batch-edit CSV format; Path/Header/Cookie params use inline parameter tables rather than JSON Schema.
- Do not output standalone request or response JSON example blocks. Field-level `example` values inside JSON Schema and the Query CSV `示例值` column are allowed when known.
- Treat response-model completeness as the catalog's primary deliverable. Before finishing, trace every response `$ref` and verify that the referenced model has a complete JSON Schema entry.
- Do not output data models as only prose, tables, TypeScript/Java classes, or field lists; tables can be supplementary, but JSON Schema is required.
- If a field is uncertain, keep it out of `required`, describe the uncertainty in `description`, and list it again in `待确认项`.
- Include examples only when they are known or can be safely inferred from the contract.
- Do not invent endpoints, fields, permissions, or error codes; list unknowns explicitly.

## No API Change

Use:

```text
Apifox sync summary：无 API 变更，无需同步。
```
