# Implementation Plan: VM Creation GPU Profile Support

**Branch**: `812-vm-mk-gpu-support`  **Date**: 2026-04-06  **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/812-vm-mk-gpu-support/spec.md`

## Summary

Add an optional, repeatable `--gpu-profile` CLI option to all six interactive VM creation commands (`from-template`, `from-clone`, `from-clib`, `shell`, `from-image`, `from-spec`). Each specified GPU profile name/description is resolved to its type identifier via the existing `get_vm_gpu_profiles_by_name_or_desc()` lookup, then assembled into a list and passed as the `gpus` parameter to the corresponding `pyvss` creation method. The `from-file` command already passes arbitrary payload fields through, so GPU profiles in YAML spec files will work without additional CLI changes, though the `VmCliSpec`/`VmApiSpec` dataclasses need a `gpus` field added for first-class support.

## Technical Context

**Language/Version**: Python >=3.10 (3.10 / 3.11 / 3.12 / 3.13 supported)
**Primary Dependencies**: Click 8.x, pyvss >=2025.2.1 (already has `gpus` param), tabulate, ruamel.yaml, rich, jsonpath-ng
**Storage**: N/A (stateless CLI; config in `~/.vss-cli/config.yaml`)
**Testing**: nose (primary), pytest (secondary); mock pyvss via `unittest.mock`
**Target Platform**: macOS, Linux, Windows (Python >=3.10); distributed via PyPI, Homebrew, Docker
**Project Type**: CLI plugin — extending existing plugin in `vss_cli/plugins/compute_plugins/`
**Performance Goals**: Command startup <500 ms; spinner for all API calls
**Constraints**: Black line length 79; flake8 clean; HTTPS only; no creds in logs or stdout; single quotes preferred
**Scale/Scope**: Applies to 6 interactive `mk` subcommands + 3 multi-instance variants; also extends the `from-file` (YAML spec) dataclass pipeline for GPU support

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify compliance with `.specify/memory/constitution.md` v1.1.0:

| # | Principle | Gate Question | Pass? |
|---|-----------|---------------|-------|
| I | Plugin-First Architecture | New commands placed in `vss_cli/plugins/`? Plugin exports `cli` object? No logic added to `cli.py` dispatcher? Sub-plugin groups use `click_plugins.with_plugins()` and `pyproject.toml` entry points? | ☑ No new plugins — extending existing `compute_plugins/vm.py` plugin and `compute_plugins/rel_opts.py` shared options. No changes to `cli.py`. |
| II | CLI Interface Contract | Output via `format_output()` + `COLUMNS_*` in `const.py`? Errors use `VssCliError`? Spinner used for API calls? `--wait` provided for async ops? IaC YAML specs validated before API submission? MCP tools follow same I/O contract? | ☑ No output format changes. Invalid GPU profile lookup raises existing error path from `_get_types_by_name`. Existing spinner and `--wait` semantics unchanged. IaC YAML spec dataclasses updated for `gpus` field. |
| III | Security & Credential Integrity | No credentials logged or printed? Config files under `~/.vss-cli/`? `VSS_*` env vars respected (CLI args > env > config > defaults)? HTTPS only? `requests.Session` used with headers at session level? | ☑ GPU profile names are not credentials. No changes to auth, config, or session handling. |
| IV | Observability & Request Transparency | Async ops return trackable request ID? `wait_for_request_to()` available? Module-level logger used (no bare `print()`)? Bulk ops use `WorkerQueue`? | ☑ All creation commands already return request IDs and support `--wait`. No changes to request tracking. Logging via `_LOGGING.debug()` for payload. |
| V | Simplicity & Calendar Versioning | No speculative features? Existing stack preferred over new deps (extras gate for new optionals)? `bump2version` used for version bumps? Black + flake8 compliance (single quotes)? Type hints on public functions? Google-style docstrings? | ☑ No new dependencies. Reuses existing `vm_gpu_profiles` autocompletion and `get_vm_gpu_profiles_by_name_or_desc` resolution. All code formatted per Black + flake8. Type hints on new option definition. |

All five gates pass. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/812-vm-mk-gpu-support/
├── plan.md              # This file
├── spec.md              # Feature specification (Clarified)
└── checklists/
    └── requirements.md  # Specification quality checklist
```

### Source Code (repository root)

```text
vss_cli/
├── plugins/
│   └── compute_plugins/
│       ├── vm.py           # MODIFY: Add @c_so.gpu_profile_mk_opt decorator and
│       │                   #   `gpu_profile` param + payload logic to 6 commands:
│       │                   #   compute_vm_mk_template, compute_vm_mk_clone,
│       │                   #   compute_vm_mk_clib, compute_vm_mk_shell,
│       │                   #   compute_vm_mk_image, compute_vm_mk_spec
│       └── rel_opts.py     # MODIFY: Add gpu_profile_mk_opt (optional, multiple,
│                           #   --gpu-profile with autocompletion)
├── data_types.py           # MODIFY: Add `gpus` field to VmMachine, VmCliSpec,
│                           #   and VmApiSpec dataclasses + from_cli_spec mapping
└── data/
    ├── template.yaml       # MODIFY: Add commented-out gpus example
    ├── clone.yaml          # MODIFY: Add commented-out gpus example
    ├── clib.yaml           # MODIFY: Add commented-out gpus example
    ├── shell.yaml          # MODIFY: Add commented-out gpus example
    └── image.yaml          # MODIFY: Add commented-out gpus example

tests/
└── test_vm_mk_gpu.py      # CREATE: Unit tests for GPU profile option
```

**Structure Decision**: No new modules or plugins. This is a purely additive change extending existing commands with a new shared option, following the identical pattern used by `--firmware`, `--tpm`, `--vbs`, and `--storage-type`.

## Implementation Details

### Phase 1: New Click Option Definition

**File**: `vss_cli/plugins/compute_plugins/rel_opts.py`

Add a new option `gpu_profile_mk_opt` after the existing `gpu_profile_opt` (line 332). This is analogous to how `firmware_nr_opt` (optional) coexists with `firmware_opt` (required):

```python
gpu_profile_mk_opt = click.option(
    '--gpu-profile',
    type=click.STRING,
    help='GPU profile to add to VM.',
    multiple=True,
    required=False,
    shell_complete=autocompletion.vm_gpu_profiles,
)
```

Key design decisions:
- **`--gpu-profile`** (not `--profile` / `-p`): avoids conflict with `--custom-spec -p` used on from-template, from-clone, from-clib commands
- **`multiple=True`**: matches `pyvss` `gpus: Optional[list]` parameter; follows the pattern of `--disk`, `--net`, `--scsi`
- **`required=False`**: GPU is optional; omitting preserves backward compatibility
- **No callback**: resolution done in the command function body (same pattern as `--firmware`)

### Phase 2: Command Function Updates

**File**: `vss_cli/plugins/compute_plugins/vm.py`

For each of the 6 commands, three changes are needed:

1. **Add decorator**: `@c_so.gpu_profile_mk_opt` — placed after `@c_so.vbs_enable_opt` (grouping it with other hardware options)
2. **Add function parameter**: `gpu_profile` (Click maps `--gpu-profile` with `multiple=True` to a tuple)
3. **Add payload logic**: Resolve each profile and build the `gpus` list in the Hardware section

The payload logic pattern (identical in all 6 commands):

```python
# Hardware section, after other hardware options
if gpu_profile:
    _gpus = []
    for gp in gpu_profile:
        _gp = ctx.get_vm_gpu_profiles_by_name_or_desc(gp)
        _gpus.append(_gp[0]['type'])
    payload['gpus'] = _gpus
```

**Commands to modify** (with line references):

| Command | Function | Decorator Insert After | Param Insert After | Payload Insert After |
|---------|----------|----------------------|-------------------|---------------------|
| `from-template` | `compute_vm_mk_template` (L4257) | `@c_so.vbs_enable_opt` (L4250) | `vbs,` (L4283) | `if os:` block (L4319-4321) |
| `from-clone` | `compute_vm_mk_clone` (L4413) | `@c_so.vbs_enable_opt` (L4405) | `vbs,` (L4440) | `if os:` block (L4480-4482) |
| `from-clib` | `compute_vm_mk_clib` (L4743) | `@c_so.vbs_enable_opt` (L4737) | `vbs,` (L4776) | `if os:` block (L4809-4811) |
| `shell` | `compute_vm_mk_shell` (L4104) | `@c_so.vbs_enable_opt` (L4098) | `vbs,` (L4130) | `if os:` block (L4162-4164) |
| `from-image` | `compute_vm_mk_image` (L4579) | `@c_so.vbs_enable_opt` (L4573) | `vbs,` (L4607) | `if os:` block (L4642-4644) |
| `from-spec` | `compute_vm_mk_spec` (L3941) | `@c_so.firmware_nr_opt` (L3934) | `firmware,` (L3966) | `if os:` block (L4005-4007) |

Note: `from-spec` doesn't have `tpm`/`vbs` options currently, so the decorator goes after `@c_so.firmware_nr_opt`.

### Phase 3: Dataclass Updates (from-file YAML Support)

**File**: `vss_cli/data_types.py`

Three dataclasses need a `gpus` field:

**3a. `VmMachine`** (L216) — add after `item` field (L254-256):

```python
gpus: Optional[List[str]] = field(
    default=None, metadata=dc_config(exclude=lambda x: x is None)
)
```

**3b. `VmApiSpec`** (L589) — add after `additional_parameters` field (L669-671):

```python
gpus: Optional[List[str]] = field(
    default=None, metadata=dc_config(exclude=lambda x: x is None)
)
```

**3c. `VmApiSpec.from_cli_spec()`** (L674) — add GPU resolution after the `additional_parameters` block (L819):

```python
if cli_spec.machine.gpus:
    _gpus = []
    for gp in cli_spec.machine.gpus:
        _resolved = session.get_vm_gpu_profiles_by_name_or_desc(gp)
        _gpus.append(_resolved[0]['type'])
    data['gpus'] = _gpus
```

### Phase 4: YAML Spec Templates

Add commented-out `gpus` example to each YAML spec template, grouped with other hardware options in the `machine` section.

**Pattern** (add after `#  vbs: true` lines in each file):

```yaml
#  gpus:                  # Optional: GPU profiles to attach to VM.
#    - grid_v100d-4q
```

Files: `template.yaml`, `clone.yaml`, `clib.yaml`, `shell.yaml`, `image.yaml`

### Phase 5: Unit Tests

**File**: `tests/test_vm_mk_gpu.py` (new)

Test structure following existing patterns (`test_assist.py`):

1. **Test option registration**: Verify `--gpu-profile` is accepted by each of the 6 commands (no crash on `--help`)
2. **Test single GPU resolution**: Mock `get_vm_gpu_profiles_by_name_or_desc` → verify `gpus` list with one entry in payload
3. **Test multiple GPU resolution**: Two `--gpu-profile` flags → `gpus` list with two entries
4. **Test omission backward compatibility**: No `--gpu-profile` → no `gpus` key in payload
5. **Test invalid GPU profile**: Mock resolution to raise → verify CLI error without API call

## Complexity Tracking

No Constitution violations. No complexity to track.

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| `-p` short flag conflict with `--custom-spec` | N/A | N/A | Resolved: using `--gpu-profile` (long form only, no short flag) |
| `from-spec` missing `tpm`/`vbs` — inconsistent option ordering | Low | Low | Insert `--gpu-profile` after `--firmware` for `from-spec`; separate P2 task could add missing `tpm`/`vbs` to `from-spec` |
| YAML spec `gpus` field not deserialized by `dataclasses_json` | Low | Medium | Add `gpus` field to all three dataclasses (`VmMachine`, `VmCliSpec`, `VmApiSpec`) |
| Partial profile resolution failure in multi-GPU scenario | Low | Low | Resolution loop processes sequentially; first failure raises standard error before any API call |

## Dependency Graph

```
Phase 1 (rel_opts.py)
    └─► Phase 2 (vm.py) — depends on new option being defined
    └─► Phase 3 (data_types.py) — independent of Phase 2
         └─► Phase 4 (YAML templates) — independent
    └─► Phase 5 (tests) — depends on Phases 1-3
```

Phases 2, 3, and 4 can be developed in parallel once Phase 1 is complete.

