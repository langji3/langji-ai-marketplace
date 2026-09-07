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

Treat the user-selected existing module as a required business boundary, not a guessed CLI flag. Check installed-version capabilities; static examples do not establish support for module assignment.

Before mutation, prove from current CLI output how an endpoint or schema payload is assigned to that module. If no reliable module assignment is exposed, stop and return the planned logical directories and resources for manual review.

## Execution owner

Use [CLI synchronization and recovery](cli-sync.md) for authorization, dependency order, execution records, unknown results, bounded retries and read-back. Build payloads in an OS temporary or confirmed ignored directory.

Never print or persist an Apifox API token. Never delete resources, clean a module, overwrite unrelated fields, merge an Apifox branch, or apply an import conflict policy without separate explicit authorization.

## Official references

- [CLI command reference](https://docs.apifox.com/doc-5637756)
- [Use Apifox CLI with an AI Agent](https://docs.apifox.com/9212297m0)
- [Apifox modules](https://docs.apifox.com/module)
- [Official Apifox CLI skills](https://github.com/apifox/apifox-cli-skills)
