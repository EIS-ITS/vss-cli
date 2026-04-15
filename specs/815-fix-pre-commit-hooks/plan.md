# Implementation Plan: Fix Pre-Commit Hooks

**Branch**: `815-fix-pre-commit-hooks` | **Date**: 2026-04-12 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/815-fix-pre-commit-hooks/spec.md`

## Summary

Update the pre-commit hook configuration to align with the sibling `py-vss` project, resolving version incompatibilities (pyupgrade crash on Python 3.14, deprecated mirror repos), outdated tool versions, missing configuration files (`.yamllint.yml`), and inconsistent linter settings (`setup.cfg` isort/flake8). After configuration updates, run the updated formatters to auto-fix the codebase so all hooks pass cleanly.

## Technical Context

**Language/Version**: Python >=3.10 (3.10 / 3.11 / 3.12 / 3.13 supported; pre-commit runtime is Python 3.14)
**Primary Dependencies**: Click 8.x, pyvss >=2025.2.1, tabulate, ruamel.yaml, rich, jsonpath-ng
**Storage**: N/A (stateless CLI; config in `~/.vss-cli/config.yaml`)
**Testing**: nose (primary), pytest (secondary); mock pyvss via `unittest.mock`
**Target Platform**: macOS, Linux, Windows (Python >=3.10); distributed via PyPI, Homebrew, Docker
**Project Type**: Developer tooling / configuration fix — no new features or plugins
**Performance Goals**: N/A — configuration-only change
**Constraints**: Black line length 79; flake8 clean; single quotes preferred; pre-commit hooks must pass on full codebase
**Scale/Scope**: 4 configuration files modified, 1 new configuration file created, code auto-formatted by updated tools

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify compliance with `.specify/memory/constitution.md` v1.1.0:

| # | Principle | Gate Question | Pass? |
|---|-----------|---------------|-------|
| I | Plugin-First Architecture | New commands placed in `vss_cli/plugins/`? Plugin exports `cli` object? No logic added to `cli.py` dispatcher? Sub-plugin groups use `click_plugins.with_plugins()` and `pyproject.toml` entry points? | ☑ N/A — no new commands or plugins. Configuration-only change. |
| II | CLI Interface Contract | Output via `format_output()` + `COLUMNS_*` in `const.py`? Errors use `VssCliError`? Spinner used for API calls? `--wait` provided for async ops? IaC YAML specs validated before API submission? MCP tools follow same I/O contract? | ☑ N/A — no CLI behavior changes. Only reformatting of existing code by updated tools. |
| III | Security & Credential Integrity | No credentials logged or printed? Config files under `~/.vss-cli/`? `VSS_*` env vars respected (CLI args > env > config > defaults)? HTTPS only? `requests.Session` used with headers at session level? | ☑ N/A — no changes to auth, config, or credential handling. |
| IV | Observability & Request Transparency | Async ops return trackable request ID? `wait_for_request_to()` available? Module-level logger used (no bare `print()`)? Bulk ops use `WorkerQueue`? | ☑ N/A — no changes to request handling or logging. |
| V | Simplicity & Calendar Versioning | No speculative features? Existing stack preferred over new deps (extras gate for new optionals)? `bump2version` used for version bumps? Black + flake8 compliance (single quotes)? Type hints on public functions? Google-style docstrings? | ☑ This change directly enforces Principle V: ensures Black + flake8 compliance passes, updates tooling to match project's Python >=3.10 target, no new dependencies added. |

All five gates pass. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/815-fix-pre-commit-hooks/
├── plan.md              # This file
├── spec.md              # Feature specification
└── checklists/
    └── requirements.md  # Specification quality checklist
```

### Source Code (repository root)

```text
# Files MODIFIED
.pre-commit-config.yaml     # MODIFY: Update all 6 hook versions & repos
setup.cfg                    # MODIFY: Update [flake8] and [isort] sections

# Files CREATED
.yamllint.yml                # CREATE: Relaxed yamllint rules (aligned with py-vss)

# Files AUTO-REFORMATTED (by updated tools — no manual edits)
vss_cli/**/*.py              # black + isort auto-reformatting
tests/**/*.py                # black + isort auto-reformatting
```

**Structure Decision**: No new modules or plugins. This is a configuration alignment change affecting only developer tooling files at the repository root, plus auto-reformatting of existing source files by the updated tools.

## Implementation Details

### Phase 1: Pre-Commit Configuration Update

**File**: `.pre-commit-config.yaml`

Replace the entire file content to align with `py-vss`, adapted for this project's directory names (`vss_cli` instead of `pyvss`):

| Hook | Current | Target | Key Changes |
|------|---------|--------|-------------|
| pyupgrade | v3.15.0, `--py37-plus` | v3.21.2, `--py310-plus` | Fix Python 3.14 crash; target correct min version |
| isort | `pre-commit/mirrors-isort` v5.10.1, no args | `PyCQA/isort` 5.13.2, `--profile black --line-length 79 --multi-line 3 --trailing-comma` | Switch to maintained repo; explicit black-compatible args |
| black | 23.11.0 | 24.10.0 | Python 3.14 compatibility |
| flake8 | 6.1.0, docstrings 1.6.0, pydocstyle 6.1.1 | 7.3.0, docstrings 1.7.0, pydocstyle 6.3.0 | Updated deps |
| yamllint | v1.33.0 | v1.38.0 | Latest version |
| prettier | `prettier/prettier` 2.0.4 | `pre-commit/mirrors-prettier` v3.1.0 | Switch to maintained mirror repo |

Key design decisions:
- **Hook ordering**: Match `py-vss` order (pyupgrade → isort → black → flake8 → yamllint → prettier). This ensures isort runs before black, and both run before flake8 linting
- **`--py310-plus`**: Matches `requires-python = ">=3.10"` in `pyproject.toml` (py-vss uses `--py39-plus` because its minimum is 3.9)
- **isort args inline**: Explicit `--profile black` in pre-commit args ensures consistency regardless of `setup.cfg` config loading behavior
- **Document start marker**: Add `---` at top of file (YAML best practice, matches py-vss)

### Phase 2: Yamllint Configuration

**File**: `.yamllint.yml` (new)

Create at project root, identical to `py-vss`:

```yaml
---
extends: default

rules:
  document-start: disable
  line-length:
    max: 200
  indentation: disable
  truthy:
    allowed-values: ['true', 'false', 'yes', 'no']
```

Design decisions:
- **`document-start: disable`**: Many YAML files in the project (spec files, config templates, agent configs) omit `---`; enforcing it would require touching dozens of non-code files
- **`line-length: max: 200`**: YAML files (especially `clib.yaml`, spec files) contain long description strings; 80-char limit is impractical
- **`indentation: disable`**: Different YAML files use different indentation conventions; strict enforcement would require mass reformatting of non-code YAML

### Phase 3: Setup.cfg Updates

**File**: `setup.cfg`

**3a. `[flake8]` section** — add `per-file-ignores` (consistent with py-vss):

```ini
[flake8]
exclude = .venv,.git,docs,venv,bin,lib,deps,build
ignore = F401,E402,W503
per-file-ignores =
    tests/*:D100,D101,D102,D104
```

This suppresses missing-docstring warnings in test files:
- `D100`: Missing docstring in public module
- `D101`: Missing docstring in public class
- `D102`: Missing docstring in public method
- `D104`: Missing docstring in public package

**3b. `[isort]` section** — replace legacy config with `profile=black` (consistent with py-vss):

```ini
[isort]
profile=black
line_length=79
force_sort_within_sections = true
not_skip = __init__.py
sections = FUTURE,STDLIB,THIRDPARTY,FIRSTPARTY,LOCALFOLDER
default_section = THIRDPARTY
known_first_party = vss_cli,tests
forced_separate = tests
```

Key changes:
- **Added `profile=black`**: Ensures isort output is black-compatible (multi-line mode 3, trailing comma, parentheses)
- **Removed `multi_line_output = 4`**: Replaced by `profile=black` (which uses mode 3)
- **Removed `indent = "    "`**: Handled by the black profile
- **Removed `combine_as_imports = true`**: Handled by the black profile
- **Removed `use_parentheses = true`**: Handled by the black profile
- **Removed `skip = compute.py,request.py`**: These legacy skips are no longer needed with black-compatible output
- **Removed `INBETWEENS` section**: Not a standard isort section; was causing warnings
- **Kept project-specific settings**: `force_sort_within_sections`, `known_first_party`, `forced_separate`, `not_skip` — these are project-specific and not covered by the profile

### Phase 4: Auto-Formatting Pass

After updating configuration, run all hooks to auto-format the codebase:

1. **`pre-commit clean`** — Clear cached hook environments (old versions)
2. **`pre-commit install`** — Reinstall hooks with new config
3. **`pre-commit run pyupgrade --all-files`** — Apply Python 3.10+ upgrades
4. **`pre-commit run isort --all-files`** — Reformat imports (may need 2 passes)
5. **`pre-commit run black --all-files`** — Reformat code
6. **`pre-commit run flake8 --all-files`** — Verify no remaining lint errors
7. **`pre-commit run yamllint --all-files`** — Verify YAML lint passes
8. **`pre-commit run --all-files`** — Final full pass (all hooks, exit code 0)

Expected auto-format changes:
- **pyupgrade**: `tests/test_vss_cli.py`, `vss_cli/utils/threading.py` — Python 3.10+ syntax upgrades (already partially applied by old version before crash)
- **isort**: Multiple files — import reordering to match `profile=black`
- **black**: Multiple files — formatting adjustments for v24.10.0

### Phase 5: Validation

Run the full pre-commit suite and verify:
- All 6 hooks pass (exit code 0)
- No crashes or version-incompatibility errors
- `git diff --stat` shows only expected formatting changes

## Complexity Tracking

No Constitution violations. No complexity to track.

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| black v24.10.0 reformats code differently than v23.11.0 | High | Low | Expected: auto-reformatting is part of this change; review diff for correctness |
| isort profile change reorders imports causing runtime issues | Very Low | Medium | isort `profile=black` is well-tested; run test suite after reformatting |
| Removing `skip = compute.py,request.py` from isort causes import errors | Low | Medium | These files had complex imports; verify with isort + test suite; re-add skip if needed |
| Pre-commit cache stale after version updates | Medium | Low | Document `pre-commit clean` in implementation steps |
| flake8 v7.3.0 reports new warnings not in v6.1.0 | Low | Low | The `ignore` and `per-file-ignores` settings should cover known warnings; address any new ones as they arise |

## Dependency Graph

```
Phase 1 (.pre-commit-config.yaml)
    └─► Phase 4 (auto-formatting) — depends on new hook versions
Phase 2 (.yamllint.yml)
    └─► Phase 4 (auto-formatting) — yamllint needs config before running
Phase 3 (setup.cfg)
    └─► Phase 4 (auto-formatting) — isort/flake8 need updated config
Phase 4 (auto-formatting)
    └─► Phase 5 (validation) — depends on all formatting complete
```

Phases 1, 2, and 3 are independent and can be done in parallel. Phase 4 depends on all three. Phase 5 depends on Phase 4.

