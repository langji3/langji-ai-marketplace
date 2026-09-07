# Add Plugin Guide

## Goal

Add a new distributable plugin to this marketplace without coupling the repository structure to one plugin.

## Checklist

1. Create `plugins/<plugin-name>/`.
2. Copy the validated distribution snapshot from the plugin source repository.
3. Add a new entry to `catalog/plugins.json`.
4. Add a new plugin entry to `.agents/plugins/marketplace.json`.
5. Add a new plugin entry to `.claude-plugin/marketplace.json`.
6. Document installation notes for each supported tool if they differ from existing plugins.
7. Document how the plugin snapshot should be updated.
8. Add plugin-specific identity, version, provenance, and recovery checks. The current sync/validation scripts maintain only ai-dev-protocol; adding an index entry does not automatically extend their coverage. Generalizing these scripts is a separate change.

## Principles

- The marketplace repository distributes snapshots.
- The plugin source repository authors the actual rules and logic.
- Every plugin should be installable from its local marketplace snapshot.
