# Implementation Plan: Fix All Dependabot Security Vulnerabilities

**Branch**: `814-fix-dependabot-cves` | **Date**: 2026-04-12 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/814-fix-dependabot-cves/spec.md`

## Summary

Raise version constraint floors and unpin hard-pinned dependencies in `pyproject.toml` to eliminate 10 known CVEs across 4 packages: `cryptography` (3 CVEs, HIGH), `jinja2` (3 CVEs, MEDIUM), `wheel` (1 CVE, HIGH), and `mcp[cli]` (3 CVEs, HIGH). Two packages (`cryptography`, `jinja2`) already resolve to safe versions in the lock file but have permissive constraints that allow vulnerable installs; two packages (`wheel`, `mcp`) are actually resolved to vulnerable versions and require both constraint and lock file updates. The change is confined to `pyproject.toml` version specifiers plus lock file regeneration — no source code modifications are needed.

## Technical Context

**Language/Version**: Python >=3.10 (3.10 / 3.11 / 3.12 / 3.13 supported)
**Primary Dependencies**: Click 8.x, pyvss ==2026.4.0, tabulate, ruamel.yaml, rich, jsonpath-ng
**Storage**: N/A (stateless CLI; config in `~/.vss-cli/config.yaml`)
**Testing**: nose (primary), pytest (secondary); mock pyvss via `unittest.mock`
**Target Platform**: macOS, Linux, Windows (Python >=3.10); distributed via PyPI, Homebrew, Docker
**Project Type**: Dependency maintenance — no new features, plugins, or source code changes
**Performance Goals**: No change — dependency version bumps only
**Constraints**: Black line length 79; flake8 clean; HTTPS only; no creds in logs or stdout
**Scale/Scope**: 4 packages × 6 locations in `pyproject.toml`; 10 CVEs total (7 HIGH, 3 MEDIUM)

### Current State Analysis

| Package | Constraint | Lock Resolution | Min Safe | Issue Type |
|---------|-----------|----------------|----------|------------|
| `cryptography` | `>=44.0.0` (main deps) | 46.0.6 ✅ | >=46.0.6 | Constraint floor too low |
| `jinja2` | `>=2.10` (main deps) | 3.1.6 ✅ | >=3.1.5 | Constraint floor too low |
| `wheel` | `==0.45.1` (test, dev, uv) | 0.45.1 ❌ | >=0.46.2 | Hard-pinned to vulnerable version |
| `mcp[cli]` | `>=1.7.1` (mcp extras) | 1.19.0 ❌ | >=1.23.0 | Constraint too low + resolved vulnerable |

### Codebase Impact Assessment

| Package | Direct Imports | Usage | Breaking Risk |
|---------|---------------|-------|---------------|
| `cryptography` | `encrypted.py` L12-15 | `default_backend`, `hashes.SHA256`, `AESGCM`, `PBKDF2HMAC` | None — all APIs stable since cryptography 38.x; `default_backend()` is a no-op since 38.x but still importable |
| `jinja2` | None (transitive only) | Required by Sphinx, pyvss | None — not directly imported |
| `wheel` | None (build tool only) | Build/test dependency | None — only used by pip/uv for wheel building |
| `mcp[cli]` | None (via `mcp-vss`) | `mcp_server_vss.server.create_app` in `plugins/mcp.py` | Low — MCP SDK maintains backward compatibility for server creation APIs |

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

Verify compliance with `.specify/memory/constitution.md` v1.1.0:

| # | Principle | Gate Question | Pass? |
|---|-----------|---------------|-------|
| I | Plugin-First Architecture | New commands placed in `vss_cli/plugins/`? Plugin exports `cli` object? No logic added to `cli.py` dispatcher? Sub-plugin groups use `click_plugins.with_plugins()` and `pyproject.toml` entry points? | ☑ N/A — no new commands or plugins. Only `pyproject.toml` version constraints change. |
| II | CLI Interface Contract | Output via `format_output()` + `COLUMNS_*` in `const.py`? Errors use `VssCliError`? Spinner used for API calls? `--wait` provided for async ops? IaC YAML specs validated before API submission? MCP tools follow same I/O contract? | ☑ N/A — no output, error, or CLI behavior changes. |
| III | Security & Credential Integrity | No credentials logged or printed? Config files under `~/.vss-cli/`? `VSS_*` env vars respected (CLI args > env > config > defaults)? HTTPS only? `requests.Session` used with headers at session level? | ☑ This change directly improves security posture by eliminating known CVEs in `cryptography` (credential encryption) and `mcp` (server transport). |
| IV | Observability & Request Transparency | Async ops return trackable request ID? `wait_for_request_to()` available? Module-level logger used (no bare `print()`)? Bulk ops use `WorkerQueue`? | ☑ N/A — no changes to logging or request handling. |
| V | Simplicity & Calendar Versioning | No speculative features? Existing stack preferred over new deps (extras gate for new optionals)? `bump2version` used for version bumps? Black + flake8 compliance (single quotes)? Type hints on public functions? Google-style docstrings? | ☑ No new dependencies introduced. Existing dependencies raised to safe versions only. No code changes requiring formatting. |

All five gates pass. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/814-fix-dependabot-cves/
├── plan.md              # This file
├── spec.md              # Feature specification (Clarified)
└── checklists/
    └── requirements.md  # Specification quality checklist
```

### Source Code (repository root)

```text
pyproject.toml           # MODIFY: Raise version constraints for 4 packages
                         #   across 6 locations (main deps, test, dev, mcp, uv)
uv.lock                  # REGENERATE: `uv lock` after constraint updates
```

**Structure Decision**: No new modules, plugins, or source files. This is a pure dependency maintenance change. Only `pyproject.toml` is edited; the lock file is regenerated by the package manager.

## Implementation Details

### Phase 1: Raise Constraint Floors (Constraint-Only Changes)

**File**: `pyproject.toml`

These two packages already resolve safely in the lock file. The change prevents future resolver regressions by raising the minimum allowed version.

**1a. `cryptography`** — Line 44, `[project] dependencies`:

```diff
-    "cryptography>=44.0.0",
+    "cryptography>=46.0.6",
```

**1b. `jinja2`** — Line 33, `[project] dependencies`:

```diff
-    "jinja2>=2.10",
+    "jinja2>=3.1.5",
```

### Phase 2: Update Hard-Pinned `wheel` (3 Locations)

**File**: `pyproject.toml`

The `wheel` package is hard-pinned with `==` to the vulnerable version in three separate sections. All three must be updated consistently.

**2a.** Line 56, `[project.optional-dependencies] test`:

```diff
-    "wheel==0.45.1",
+    "wheel>=0.46.2",
```

**2b.** Line 64, `[project.optional-dependencies] dev`:

```diff
-    "wheel==0.45.1",
+    "wheel>=0.46.2",
```

**2c.** Line 103, `[tool.uv] dev-dependencies`:

```diff
-    "wheel==0.45.1",
+    "wheel>=0.46.2",
```

### Phase 3: Raise `mcp[cli]` Constraint

**File**: `pyproject.toml`

**3a.** Line 74, `[project.optional-dependencies] mcp`:

```diff
-    "mcp[cli]>=1.7.1",
+    "mcp[cli]>=1.23.0",
```

### Phase 4: Regenerate Lock File

After all constraint changes, regenerate the lock file to resolve updated versions:

```bash
uv lock
```

**Expected outcome**:
- `cryptography` stays at 46.0.6 (already safe, constraint floor raised)
- `jinja2` stays at 3.1.6 (already safe, constraint floor raised)
- `wheel` resolves to >=0.46.2 (was 0.45.1, now must resolve higher)
- `mcp` resolves to >=1.23.0 (was 1.19.0, now must resolve higher)

### Phase 5: Verification

**5a. CVE Scan**: Run dependency security validation to confirm zero CVEs remain.

**5b. Install Check**: Verify clean installation:

```bash
uv pip install -e ".[dev,mcp]"
```

**5c. Test Suite**: Run existing tests to verify no regressions:

```bash
python -m nose tests/
```

**5d. Import Smoke Test**: Verify critical imports still work:

```bash
python -c "from cryptography.hazmat.backends import default_backend; from cryptography.hazmat.primitives.ciphers.aead import AESGCM; from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC; print('cryptography OK')"
python -c "import jinja2; print(f'jinja2 {jinja2.__version__} OK')"
```

## Complexity Tracking

No Constitution violations. No complexity to track.

## Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| `mcp-vss` incompatible with `mcp>=1.23.0` | Medium | Medium | Check `mcp-vss` release notes; if incompatible, may need to bump `mcp-vss` minimum version or coordinate with upstream |
| `cryptography>=46.0.6` drops `default_backend()` | Very Low | Low | `default_backend()` has been a no-op since v38.x but remains importable; can be removed as a follow-up cleanup |
| `wheel>=0.46.2` introduces breaking build behavior | Very Low | Low | `wheel` is only a build/test tool; any issues surface immediately during `uv lock` or `pip install` |
| Lock file regeneration creates resolution conflicts | Low | Medium | Run `uv lock` and inspect output; if conflicts arise, adjust constraints iteratively |
| `pyvss==2026.4.0` requires older `cryptography` or `jinja2` | Very Low | High | Verify `pyvss` metadata doesn't upper-bound these packages; current lock already resolves safely |

## Dependency Graph

```
Phase 1 (cryptography, jinja2 constraints)
    └─► Phase 4 (uv lock) — constraint-only, no resolution change expected

Phase 2 (wheel unpin, 3 locations)
    └─► Phase 4 (uv lock) — will change resolved version

Phase 3 (mcp[cli] constraint)
    └─► Phase 4 (uv lock) — will change resolved version

Phase 4 (uv lock)
    └─► Phase 5 (verification) — depends on successful lock regeneration
```

Phases 1, 2, and 3 are independent of each other and can be applied in any order (or all at once in a single edit). Phase 4 must come after all constraint changes. Phase 5 must come last.

