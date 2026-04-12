# Tasks: VM Creation GPU Profile Support

**Input**: Design documents from `/specs/812-vm-mk-gpu-support/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

**Tests**: Included — the plan explicitly specifies unit tests in Phase 5.

**Organization**: Tasks grouped by user story to enable independent implementation and testing.

**Status**: ✅ All 26 tasks complete. 8/8 tests passing. flake8 clean.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3, US4)
- Include exact file paths in descriptions

## Path Conventions

- **Sub-plugin group**: `vss_cli/plugins/compute_plugins/vm.py`
- **Shared options**: `vss_cli/plugins/compute_plugins/rel_opts.py`
- **Dataclasses**: `vss_cli/data_types.py`
- **YAML templates**: `vss_cli/data/*.yaml`
- **Tests**: `tests/test_vm_mk_gpu.py`

---

## Phase 1: Foundational (Blocking Prerequisites)

**Purpose**: Shared option definition that ALL user stories depend on. No command can use `--gpu-profile` until this is complete.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [x] T001 Define `gpu_profile_mk_opt` Click option in `vss_cli/plugins/compute_plugins/rel_opts.py` — add after existing `gpu_profile_opt` (line 332). Optional, multiple, `--gpu-profile` long name only, `click.STRING` type, `shell_complete=autocompletion.vm_gpu_profiles`. Implements FR-010 (autocompletion). *(Plan Phase 1)*

**Checkpoint**: ✅ Shared option defined — command integration can begin.

---

## Phase 2: User Story 1 — Deploy VM from Template with GPU (Priority: P1) 🎯 MVP

**Goal**: Users can deploy a GPU-equipped VM from a template in a single command.

**Independent Test**: Run `vss-cli compute vm mk from-template --gpu-profile <profile> ...` and verify the request payload includes `gpus` list.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T002 [US1] Create test file `tests/test_vm_mk_gpu.py` with `TestVmMkGpuProfileRegistration` class — test that `compute_vm_mk_template` has `gpu_profile` parameter, is optional, is multiple, uses `--gpu-profile` long name, and has help text mentioning GPU. *(Plan Phase 5, item 1)*
- [x] T003 [US1] Add `TestVmMkGpuProfilePayload.test_single_gpu_profile_from_template` in `tests/test_vm_mk_gpu.py` — mock `get_vm_gpu_profiles_by_name_or_desc`, invoke `from-template` with one `--gpu-profile`, assert `gpus` list with one entry in `deploy_vm_from_template` call kwargs. *(Plan Phase 5, item 2)*
- [x] T004 [US1] Add `TestVmMkGpuProfilePayload.test_multiple_gpu_profiles_from_template` in `tests/test_vm_mk_gpu.py` — invoke with two `--gpu-profile` flags, assert `gpus` list with two entries. *(Plan Phase 5, item 3)*
- [x] T005 [US1] Add `TestVmMkGpuProfilePayload.test_no_gpu_profile_omits_gpus_key` in `tests/test_vm_mk_gpu.py` — invoke `from-template` without `--gpu-profile`, assert `gpus` key absent from payload. *(Plan Phase 5, item 4)*

### Implementation for User Story 1

- [x] T006 [US1] Add `@c_so.gpu_profile_mk_opt` decorator to `compute_vm_mk_template` in `vss_cli/plugins/compute_plugins/vm.py` — insert after `@c_so.vbs_enable_opt`. Add `gpu_profile` function parameter after `vbs,`. Implements FR-001. *(Plan Phase 2, from-template row)*
- [x] T007 [US1] Add GPU profile resolution and payload logic to `compute_vm_mk_template` in `vss_cli/plugins/compute_plugins/vm.py` — in Hardware section after `if os:` block, add `if gpu_profile:` loop resolving each profile via `ctx.get_vm_gpu_profiles_by_name_or_desc()` and setting `payload['gpus']`. Implements FR-007, FR-008, FR-009, FR-011. *(Plan Phase 2, payload pattern)*
- [x] T008 [P] [US1] Add commented-out `gpus` example to `vss_cli/data/template.yaml` — insert after `#  vbs: true` line with `#  gpus:` and `#    - nvidia_l4-24c`. *(Plan Phase 4)*

**Checkpoint**: ✅ User Story 1 complete — `from-template` supports `--gpu-profile`. Tests pass. MVP delivered.

---

## Phase 3: User Story 2 — Deploy VM from Clone with GPU (Priority: P1)

**Goal**: Users can clone a VM with GPU profiles attached at creation time.

**Independent Test**: Run `vss-cli compute vm mk from-clone --gpu-profile <profile> ...` and verify request payload includes `gpus` list.

### Tests for User Story 2

- [x] T009 [US2] Extend `TestVmMkGpuProfileRegistration` in `tests/test_vm_mk_gpu.py` — ensure `compute_vm_mk_clone` is included in `COMMANDS` dict and passes all registration tests (parameter exists, optional, multiple, correct name, help text).

### Implementation for User Story 2

- [x] T010 [US2] Add `@c_so.gpu_profile_mk_opt` decorator, `gpu_profile` parameter, and GPU payload logic to `compute_vm_mk_clone` in `vss_cli/plugins/compute_plugins/vm.py` — decorator after `@c_so.vbs_enable_opt`, param after `vbs,`, payload after `if os:` block. Implements FR-002. *(Plan Phase 2, from-clone row)*
- [x] T011 [P] [US2] Add commented-out `gpus` example to `vss_cli/data/clone.yaml` — insert after `#  vbs: true` line. *(Plan Phase 4)*

**Checkpoint**: ✅ User Story 2 complete — `from-clone` supports `--gpu-profile`.

---

## Phase 4: User Story 3 — Deploy VM from Content Library with GPU (Priority: P1)

**Goal**: Users can deploy a VM from a Content Library item with GPU profiles.

**Independent Test**: Run `vss-cli compute vm mk from-clib --gpu-profile <profile> ...` and verify request payload includes `gpus` list.

### Tests for User Story 3

- [x] T012 [US3] Extend `TestVmMkGpuProfileRegistration` in `tests/test_vm_mk_gpu.py` — ensure `compute_vm_mk_clib` is included in `COMMANDS` dict and passes all registration tests.

### Implementation for User Story 3

- [x] T013 [US3] Add `@c_so.gpu_profile_mk_opt` decorator, `gpu_profile` parameter, and GPU payload logic to `compute_vm_mk_clib` in `vss_cli/plugins/compute_plugins/vm.py` — decorator after `@c_so.vbs_enable_opt`, param after `vbs,`, payload after `if os:` block. Implements FR-003. *(Plan Phase 2, from-clib row)*
- [x] T014 [P] [US3] Add commented-out `gpus` example to `vss_cli/data/clib.yaml` — insert after `#  vbs: true` line. *(Plan Phase 4)*

**Checkpoint**: ✅ User Story 3 complete — `from-clib` supports `--gpu-profile`. All P1 stories done.

---

## Phase 5: User Story 4 — Deploy VM from Shell, Image, and Spec with GPU (Priority: P2)

**Goal**: Complete GPU support across all remaining creation methods for consistency.

**Independent Test**: Run `vss-cli compute vm mk shell --gpu-profile <profile> ...`, `from-image --gpu-profile ...`, `from-spec --gpu-profile ...` and verify payloads.

### Tests for User Story 4

- [x] T015 [US4] Extend `TestVmMkGpuProfileRegistration` in `tests/test_vm_mk_gpu.py` — ensure `compute_vm_mk_shell`, `compute_vm_mk_image`, and `compute_vm_mk_spec` are included in `COMMANDS` dict and pass all registration tests.

### Implementation for User Story 4

- [x] T016 [P] [US4] Add `@c_so.gpu_profile_mk_opt` decorator, `gpu_profile` parameter, and GPU payload logic to `compute_vm_mk_shell` in `vss_cli/plugins/compute_plugins/vm.py` — decorator after `@c_so.vbs_enable_opt`, param after `vbs,`, payload after `if iso:` block. Implements FR-004. *(Plan Phase 2, shell row)*
- [x] T017 [P] [US4] Add `@c_so.gpu_profile_mk_opt` decorator, `gpu_profile` parameter, and GPU payload logic to `compute_vm_mk_image` in `vss_cli/plugins/compute_plugins/vm.py` — decorator after `@c_so.vbs_enable_opt`, param after `vbs,`, payload after `if os:` block. Implements FR-005. *(Plan Phase 2, from-image row)*
- [x] T018 [P] [US4] Add `@c_so.gpu_profile_mk_opt` decorator, `gpu_profile` parameter, and GPU payload logic to `compute_vm_mk_spec` in `vss_cli/plugins/compute_plugins/vm.py` — decorator after `@c_so.firmware_nr_opt` (no tpm/vbs on this command), param after `firmware,`, payload after `if iso:` block. Implements FR-006. *(Plan Phase 2, from-spec row)*
- [x] T019 [P] [US4] Add commented-out `gpus` example to `vss_cli/data/shell.yaml` — insert after `#  vbs: true` line. *(Plan Phase 4)*
- [x] T020 [P] [US4] Add commented-out `gpus` example to `vss_cli/data/image.yaml` — insert after `#  power_on: true` line (no tpm/vbs in this template). *(Plan Phase 4)*

**Checkpoint**: ✅ All six creation commands support `--gpu-profile`. FR-001 through FR-006 complete.

---

## Phase 6: Dataclass Updates (from-file YAML Support)

**Purpose**: Enable `gpus` field in YAML spec files used by `from-file` command for first-class GPU support via IaC workflow.

- [x] T021 [P] Add `gpus: Optional[List[str]]` field to `VmMachine` dataclass in `vss_cli/data_types.py` — insert after `item` field with `default=None, metadata=dc_config(exclude=lambda x: x is None)`. *(Plan Phase 3a)*
- [x] T022 [P] Add `gpus: Optional[List[str]]` field to `VmApiSpec` dataclass in `vss_cli/data_types.py` — insert after `additional_parameters` field with same metadata. *(Plan Phase 3b)*
- [x] T023 Add GPU profile resolution to `VmApiSpec.from_cli_spec()` in `vss_cli/data_types.py` — after `additional_parameters` block, add `if cli_spec.machine.gpus:` loop resolving each profile via `session.get_vm_gpu_profiles_by_name_or_desc()` and setting `data['gpus']`. *(Plan Phase 3c)*

**Checkpoint**: ✅ YAML spec files with `gpus:` list are deserialized and resolved correctly by `from-file` pipeline.

---

## Phase 7: Polish & Version

**Purpose**: Version bump and final validation.

- [x] T024 [P] Update version to `2026.4.0-dev0` in `vss_cli/const.py` and update YAML template headers in `vss_cli/data/template.yaml`, `clone.yaml`, `clib.yaml`, `shell.yaml` to reflect new version string.
- [x] T025 Run `flake8 vss_cli/` and verify zero new warnings. Fix any Black formatting issues (line length 79, single quotes).
- [x] T026 Run full test suite: `python -m unittest tests.test_vm_mk_gpu -v` — verify all 8 tests pass.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Foundational)**: No dependencies — start immediately
- **Phases 2–5 (User Stories)**: All depend on Phase 1 (shared option definition)
  - User Stories 1–3 (P1) can proceed in parallel or sequentially
  - User Story 4 (P2) can proceed in parallel with P1 stories
- **Phase 6 (Dataclasses)**: Depends on Phase 1 only — can run in parallel with Phases 2–5
- **Phase 7 (Polish)**: Depends on all prior phases

### Within Each User Story

- Tests FIRST → ensure they FAIL → then implement
- Decorator + parameter → then payload logic
- YAML template update is independent ([P] tagged)

### Parallel Opportunities

```
Phase 1 (T001)
    ├─► Phase 2: US1 (T002–T008)  ─┐
    ├─► Phase 3: US2 (T009–T011)   │  All can run in
    ├─► Phase 4: US3 (T012–T014)   ├─ parallel after
    ├─► Phase 5: US4 (T015–T020)   │  Phase 1 completes
    └─► Phase 6 (T021–T023)       ─┘
                    │
                    ▼
              Phase 7 (T024–T026)
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Shared option definition
2. Complete Phase 2: User Story 1 (from-template)
3. **STOP and VALIDATE**: Run tests, verify `--gpu-profile` works on `from-template`
4. This alone delivers the highest-value use case

### Incremental Delivery

1. Phase 1 → Foundation ready
2. Phase 2 (US1) → MVP: `from-template` with GPU ✓
3. Phase 3 (US2) → Add `from-clone` with GPU ✓
4. Phase 4 (US3) → Add `from-clib` with GPU ✓ (all P1 complete)
5. Phase 5 (US4) → Add `shell`, `from-image`, `from-spec` ✓ (all P2 complete)
6. Phase 6 → YAML spec `from-file` support ✓
7. Phase 7 → Polish, version, final validation

---

## Notes

- [P] tasks = different files, no dependencies — safe to run in parallel
- [Story] label maps each task to its user story for traceability
- All 6 commands use identical payload logic pattern — copy from US1 implementation
- `from-spec` is slightly different: decorator goes after `@c_so.firmware_nr_opt` (no tpm/vbs on that command)
- Phase 6 (dataclasses) is independent of interactive command work — can be done any time after Phase 1
- Total: 26 tasks across 7 phases

