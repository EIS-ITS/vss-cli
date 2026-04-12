# Implementation Plan: [FEATURE]

**Branch**: `[###-feature-name]` | **Date**: [DATE] | **Spec**: [link]
**Input**: Feature specification from `/specs/[###-feature-name]/spec.md`

**Note**: This template is filled in by the `/speckit.plan` command. See `.specify/templates/plan-template.md` for the execution workflow.

## Summary

[Extract from feature spec: primary requirement + technical approach from research]

## Technical Context

<!--
  ACTION REQUIRED: Replace the content in this section with the technical details
  for the project. The structure here is presented in advisory capacity to guide
  the iteration process.
-->

**Language/Version**: Python >=3.10 (3.10 / 3.11 / 3.12 / 3.13 supported)
**Primary Dependencies**: Click 8.x, pyvss >=2025.2.1, tabulate, ruamel.yaml,
  rich, jsonpath-ng — add others only with constitution amendment justification
**Storage**: N/A (stateless CLI; config in `~/.vss-cli/config.yaml`)
**Testing**: nose (primary), pytest (secondary); mock pyvss via `unittest.mock`
**Target Platform**: macOS, Linux, Windows (Python >=3.10); distributed via
  PyPI, Homebrew, Docker
**Project Type**: CLI plugin — new feature = new plugin in `vss_cli/plugins/`
**Performance Goals**: Command startup <500 ms; spinner for all API calls
**Constraints**: Black line length 79; flake8 clean; HTTPS only; no creds in
  logs or stdout
**Scale/Scope**: [Feature-specific — describe VM count, request volume, etc.]

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify compliance with `.specify/memory/constitution.md` v1.1.0:

| # | Principle | Gate Question | Pass? |
|---|-----------|---------------|-------|
| I | Plugin-First Architecture | New commands placed in `vss_cli/plugins/`? Plugin exports `cli` object? No logic added to `cli.py` dispatcher? Sub-plugin groups use `click_plugins.with_plugins()` and `pyproject.toml` entry points? | ☐ |
| II | CLI Interface Contract | Output via `format_output()` + `COLUMNS_*` in `const.py`? Errors use `VssCliError`? Spinner used for API calls? `--wait` provided for async ops? IaC YAML specs validated before API submission? MCP tools follow same I/O contract? | ☐ |
| III | Security & Credential Integrity | No credentials logged or printed? Config files under `~/.vss-cli/`? `VSS_*` env vars respected (CLI args > env > config > defaults)? HTTPS only? `requests.Session` used with headers at session level? | ☐ |
| IV | Observability & Request Transparency | Async ops return trackable request ID? `wait_for_request_to()` available? Module-level logger used (no bare `print()`)? Bulk ops use `WorkerQueue`? | ☐ |
| V | Simplicity & Calendar Versioning | No speculative features? Existing stack preferred over new deps (extras gate for new optionals)? `bump2version` used for version bumps? Black + flake8 compliance (single quotes)? Type hints on public functions? Google-style docstrings? | ☐ |

*Any ☐ remaining after Phase 1 design MUST be resolved or documented in the
Complexity Tracking table below.*

## Project Structure

### Documentation (this feature)

```text
specs/[###-feature]/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
├── contracts/           # Phase 1 output (/speckit.plan command)
└── tasks.md             # Phase 2 output (/speckit.tasks command - NOT created by /speckit.plan)
```

### Source Code (repository root)
<!--
  ACTION REQUIRED: Replace the placeholder tree below with the concrete layout
  for this feature. Delete unused options and expand the chosen structure with
  real paths (e.g., apps/admin, packages/something). The delivered plan must
  not include Option labels.
-->

```text
# VSS CLI single-project layout (DEFAULT for all plugin features)
vss_cli/
├── plugins/
│   ├── <new-plugin>.py          # new top-level plugin (exports cli group)
│   └── <new-plugin>_plugins/   # sub-commands if needed
├── const.py                     # add COLUMNS_* definitions here
├── rel_opts.py                  # global shared Click options
└── validators.py                # Click param validators

tests/
├── contract/
├── integration/
└── unit/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [REMOVE IF UNUSED] Option 3: Mobile + API (when "iOS/Android" detected)
api/
└── [same as backend above]

ios/ or android/
└── [platform-specific structure: feature modules, UI flows, platform tests]
vss_cli/plugins/<group>_plugins/
├── <subcommand>.py
└── rel_opts.py
```

**Structure Decision**: [Document the selected structure and reference the real
directories captured above]

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| [e.g., 4th project] | [current need] | [why 3 projects insufficient] |
| [e.g., Repository pattern] | [specific problem] | [why direct DB access insufficient] |
