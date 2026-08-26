# Apifox CLI Runtime Rules

Use this reference only for Apifox CLI synchronization. The installed CLI's current help, `agentHints`, and `cli-schema` output override static examples in this file.

## Capability discovery

Check the local version before building commands:

```text
apifox --help
apifox whoami
apifox cli-schema list
```

For every complex create or update operation, fetch and validate the exact runtime payload schema. Common keys include:

```text
apifox cli-schema get endpoint-create
apifox cli-schema validate endpoint-create --file <payload-file>
apifox cli-schema get endpoint-update
apifox cli-schema validate endpoint-update --file <payload-file>
apifox cli-schema get schema-create
apifox cli-schema validate schema-create --file <payload-file>
apifox cli-schema get schema-update
apifox cli-schema validate schema-update --file <payload-file>
apifox cli-schema get folder-create
```

Do not assume a schema key or payload field exists merely because it appears in this reference. Resolve available keys from `cli-schema list` and command help.

## Resource discovery

Read resources from the exact project and branch before planning writes:

```text
apifox folder list --project <projectId> --branch <branchName> --type endpoint
apifox folder list --project <projectId> --branch <branchName> --type schema
apifox endpoint list --project <projectId> --branch <branchName>
apifox schema list --project <projectId> --branch <branchName>
```

Endpoint and schema folders are separate trees. Use folder-list output to resolve parent IDs and the current CLI's create/move options; never reuse an endpoint folder ID as a schema folder ID.

## Module boundary

Apifox modules own their own APIs, components, and OpenAPI document, but public CLI documentation currently exposes project, branch, endpoint, schema, and typed folder commands without a documented module-management command. Treat the user-selected existing module as a required business boundary, not as a guessed CLI flag.

Before mutation, prove from current CLI output how an endpoint or schema payload is assigned to that module. If no reliable module assignment is exposed, stop and return the planned logical directories and resources for manual review.

## Safe mutation sequence

1. Confirm `apifox whoami` returns an authenticated identity; otherwise stop and provide login guidance without requesting a token in chat.
2. Resolve project, existing module, AI branch, identities, and current folders.
3. Fetch runtime payload schemas.
4. Build payloads in an OS temporary directory or another confirmed ignored location.
5. Validate every payload.
6. Present the exact create/update/skip plan and obtain explicit approval.
7. Create or update response schemas in dependency order.
8. Create or update endpoints after referenced schema IDs are known.
9. Read back each changed resource from the same project and branch.
10. Report differences and leave branch review/merge to the user.

Never print or persist an Apifox API token. Never delete resources, clean a module, overwrite unrelated fields, merge an Apifox branch, or apply an import conflict policy without separate explicit authorization.

## Official references

- [CLI command reference](https://docs.apifox.com/doc-5637756)
- [Use Apifox CLI with an AI Agent](https://docs.apifox.com/9212297m0)
- [Apifox modules](https://docs.apifox.com/module)
- [Official Apifox CLI skills](https://github.com/apifox/apifox-cli-skills)
