# Feature Specification: Fix Pre-Commit Hooks

**Feature Branch**: `815-fix-pre-commit-hooks`  
**Created**: 2026-04-12  
**Status**: Draft  
**Input**: User description: "pre-commit is failing just as it was in ../py-vss. Use ../py-vss as reference to fix current pre-commits"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Developer Runs Pre-Commit Checks Successfully (Priority: P1)

As a developer contributing to vss-cli, I want all pre-commit hooks to pass on the existing codebase so that I can commit code without being blocked by tooling failures unrelated to my changes.

**Why this priority**: Pre-commit hooks that fail on the existing codebase block all development work. This is a prerequisite for any other contribution.

**Independent Test**: Can be fully tested by running `pre-commit run --all-files` against the current codebase and verifying zero failures.

**Acceptance Scenarios**:

1. **Given** a clean checkout of the develop branch, **When** `pre-commit run --all-files` is executed, **Then** all hooks pass with exit code 0
2. **Given** the pre-commit configuration has been updated, **When** a developer makes a new commit touching Python files, **Then** all pre-commit hooks run without errors

---

### User Story 2 - Hook Versions Aligned with Sibling Project (Priority: P2)

As a project maintainer, I want pre-commit hook versions and configurations to be consistent with the sibling `py-vss` project so that both projects follow the same code quality standards and avoid version-specific bugs.

**Why this priority**: Consistency between projects reduces maintenance burden and prevents the same tooling bugs from recurring across repositories.

**Independent Test**: Can be tested by comparing `.pre-commit-config.yaml` versions and `setup.cfg`/`pyproject.toml` tool configurations between both projects and verifying alignment on key hooks.

**Acceptance Scenarios**:

1. **Given** the updated pre-commit config, **When** comparing hook versions with `py-vss`, **Then** all shared hooks use compatible versions (same major.minor at minimum)
2. **Given** the updated linter/formatter configs, **When** comparing `setup.cfg` tool settings with `py-vss`, **Then** isort profile, flake8 per-file-ignores, and yamllint rules are consistent

---

### User Story 3 - Python Version Target Updated (Priority: P3)

As a developer, I want pre-commit tools configured for the correct minimum Python version (3.10+) so that pyupgrade and other tools apply the right code transformations matching the project's `requires-python` setting.

**Why this priority**: Incorrect Python version targets can cause tools to apply wrong transformations or miss valid modernizations.

**Independent Test**: Can be tested by verifying the pyupgrade `--py3X-plus` argument matches the `requires-python` value in `pyproject.toml`.

**Acceptance Scenarios**:

1. **Given** the project requires Python >=3.10, **When** pyupgrade runs, **Then** it uses `--py310-plus` (or the appropriate flag matching the minimum supported version)

---

### Edge Cases

- What happens when pre-commit cache contains old hook environments? Developer may need to run `pre-commit clean` after config updates.
- How does the system handle YAML files with long lines in non-code directories (e.g., spec files, agent configs)? The yamllint config must use relaxed line-length rules.
- What happens when isort and black disagree on import formatting? The isort `profile=black` setting ensures compatibility.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Pre-commit config MUST update `pyupgrade` to a version compatible with Python 3.14 runtime (v3.21.2 or later) to eliminate the `tokenize.cookie_re` crash
- **FR-002**: Pre-commit config MUST update `pyupgrade` args from `--py37-plus` to `--py310-plus` to match the project's `requires-python = ">=3.10"`
- **FR-003**: Pre-commit config MUST update `black` to v24.10.0 or later for Python 3.14 compatibility
- **FR-004**: Pre-commit config MUST update `flake8` to v7.3.0 or later, along with updated `flake8-docstrings` (1.7.0) and `pydocstyle` (6.3.0) dependencies
- **FR-005**: Pre-commit config MUST switch `isort` from the deprecated `pre-commit/mirrors-isort` repo to `PyCQA/isort` (v5.13.2) with explicit `profile=black` args
- **FR-006**: Pre-commit config MUST update `yamllint` to v1.38.0 or later
- **FR-007**: A `.yamllint.yml` configuration file MUST be created at the project root with relaxed rules (document-start disabled, line-length max 200, indentation disabled) consistent with `py-vss`
- **FR-008**: Pre-commit config MUST switch `prettier` from the deprecated `prettier/prettier` repo to `pre-commit/mirrors-prettier` (v3.1.0)
- **FR-009**: The `setup.cfg` `[flake8]` section MUST add `per-file-ignores` to suppress docstring warnings (D100, D101, D102, D104) in test files
- **FR-010**: The `setup.cfg` `[isort]` section MUST be updated to use `profile=black` for compatibility with the black formatter, replacing the legacy `multi_line_output` configuration
- **FR-011**: All pre-commit hooks MUST pass when run against the full codebase (`pre-commit run --all-files`) after configuration changes

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `pre-commit run --all-files` completes with exit code 0 and zero hook failures on the current codebase
- **SC-002**: All six pre-commit hooks (pyupgrade, black, flake8, isort, yamllint, prettier) execute without crashes or version-incompatibility errors
- **SC-003**: No developer action required beyond `pre-commit clean && pre-commit install` to adopt the updated configuration
- **SC-004**: Hook versions are within one minor version of the corresponding `py-vss` project hooks

## Assumptions

- The `py-vss` project's pre-commit configuration (as of its current state) is the authoritative reference for version and configuration alignment
- Python 3.14 is the runtime being used for pre-commit hook execution (based on the error traces showing `py_env-python3.14`)
- The project's minimum supported Python version remains >=3.10 as specified in `pyproject.toml`
- Existing code formatting differences introduced by updated tools (e.g., black reformatting) are acceptable and will be committed as part of this change
- The `.yamllint.yml` relaxed rules (line-length 200, document-start disabled) are appropriate for this project's YAML files
- The deprecated `pre-commit/mirrors-isort` and `prettier/prettier` repos should be replaced with their maintained alternatives, consistent with `py-vss`

