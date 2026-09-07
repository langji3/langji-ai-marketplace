# API catalog extraction

Use for Entry Catalog; CLI mode also uses these contract rules but maps requests directly into runtime-validated endpoint payloads.

## Source and output

Read the selected requirement, spec, diff or controller/service/API implementation. Distinguish confirmed contracts from inferred/unknown items. Keep identifiers and backend type names unchanged; explain in Chinese. Never invent endpoints, fields, permissions or errors.

Include common module/base path/auth/response/time/compatibility information, affected endpoints, request definitions, complete response models, enums, errors and relevant Mock/test follow-up. Omit sections that do not apply.

## Requests stay inline

Do not create shared request models or request-side $ref definitions. JSON Body has an inline JSON Schema inside its endpoint. Query uses Apifox comma-mode CSV in manual catalogs:
参数名,类型,必需,示例值,固定参数值,说明
One parameter per row; true/false for 必需; keep unused fixed values empty; quote commas, quotes and newlines according to CSV rules.

Path, Headers and Cookies use parameter tables. Forms/uploads remain endpoint-owned definitions. CLI synchronization uses the same parameters inline in endpoint payloads instead of executing Query CSV import.

## Complete response library

Preserve real backend names and wrappers; never force a *Vo or BaseResponse convention. Trace all reachable response types: envelopes, pagination/containers, roots, nested objects, serialized inherited fields and array items. Supply complete JSON Schema for every transitively referenced model; track visited types so recursive models terminate.

Use $ref for shared response types rather than repeated inline copies. Every referenced type must be present. Inline enum values plus descriptions inside their owning model fields; do not create standalone enum models. Supplementary tables do not replace schemas.

Use actual serialization behavior for required/nullability/formats. If uncertain, omit the field from required, describe uncertainty and list it under 待确认; do not send uncertain payload changes to CLI writes.

Do not emit standalone request/response JSON examples. Known field-level examples and Query CSV example values are allowed. Before delivery trace all response references and verify completeness.
