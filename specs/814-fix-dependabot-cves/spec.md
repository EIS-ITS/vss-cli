# Feature Specification: Fix All Dependabot Security Vulnerabilities

**Feature Branch**: `814-fix-dependabot-cves`  
**Created**: 2026-04-12  
**Status**: Implemented  
**Input**: User description: "fix all dependabot issues"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Resolve Critical and High Severity CVEs (Priority: P1)

As a project maintainer, I want all high and critical severity CVEs in the project's dependencies to be resolved so that the CLI does not expose users to known security vulnerabilities when installed or operated.

**Why this priority**: High and critical severity vulnerabilities pose the most immediate risk to production infrastructure managed by this CLI. The `cryptography` library has a HIGH severity subgroup attack (CVE-2026-26007), the `wheel` package has a HIGH severity path traversal (CVE-2026-24049), and the `mcp` SDK has three HIGH severity denial-of-service and DNS rebinding issues. These must be addressed first to protect users managing cloud infrastructure.

**Independent Test**: Can be fully tested by upgrading the affected packages (`cryptography`, `wheel`, `mcp`) and verifying that a CVE scanning tool reports zero high/critical findings against the updated dependency list.

**Acceptance Scenarios**:

1. **Given** the project has dependencies with known high/critical CVEs, **When** the dependency version constraints are raised, **Then** a security scan of the project dependencies reports zero high or critical severity vulnerabilities.
2. **Given** `cryptography` constraint is raised to `>=46.0.6`, **When** the CLI is installed, **Then** all cryptographic operations (AES-256-GCM encryption, PBKDF2 key derivation, JWT token handling, HTTPS connections) continue to function correctly.
3. **Given** `wheel` is updated from `==0.45.1` to `>=0.46.2`, **When** the project is built and packaged, **Then** the build process completes successfully without errors.
4. **Given** `mcp[cli]` constraint is raised to `>=1.23.0`, **When** the MCP server is started via `vss mcp run`, **Then** it operates without regressions and is protected against denial-of-service and DNS rebinding attacks.

---

### User Story 2 - Resolve Medium Severity CVEs (Priority: P2)

As a project maintainer, I want all medium severity CVEs in the project's dependencies to be resolved so that the CLI meets security compliance standards and reduces overall attack surface.

**Why this priority**: Medium severity vulnerabilities in `jinja2` (ReDoS, HTML injection, sandbox escape) present a lower but still meaningful risk. Resolving these ensures the project passes security audits and maintains a clean dependency profile.

**Independent Test**: Can be fully tested by upgrading the `jinja2` version constraint to `>=3.1.5` and verifying that the security scan passes cleanly. Note: `jinja2` is not directly imported by the CLI codebase — it is a transitive dependency required by other packages (Sphinx, pyvss). The risk is lower but the constraint should still be raised.

**Acceptance Scenarios**:

1. **Given** `jinja2` is constrained at `>=2.10`, **When** it is updated to `>=3.1.5`, **Then** a security scan reports zero medium severity vulnerabilities for `jinja2`.
2. **Given** `jinja2` has been updated, **When** the CLI is installed and operated, **Then** no import errors or runtime failures occur related to Jinja2 or its dependents.

---

### User Story 3 - Verify No Functional Regressions After Updates (Priority: P3)

As a developer, I want the existing test suite to pass after all dependency updates so that I have confidence the upgrades do not introduce breaking changes.

**Why this priority**: Dependency upgrades can introduce subtle breaking changes in APIs, behaviors, or compatibility. Running the full test suite validates that the CLI remains functional across all its features.

**Independent Test**: Can be fully tested by running the project's existing test suite and confirming all tests pass with zero failures.

**Acceptance Scenarios**:

1. **Given** all vulnerable dependencies have been updated, **When** the test suite is executed, **Then** all existing tests pass without modification.
2. **Given** all vulnerable dependencies have been updated, **When** the CLI is installed from the updated project, **Then** core commands (`vss compute vm ls`, `vss configure ls`, `vss assist`) are accessible without import errors or crashes.
3. **Given** all version constraints have been raised, **When** the lock file is regenerated, **Then** the dependency resolver succeeds without conflicts and all resolved versions meet or exceed the minimum safe versions.

---

### Edge Cases

- What happens when an updated dependency has a conflicting version requirement with another pinned dependency (e.g., `pyvss==2026.4.0` requiring an older `cryptography`)?
- How does the system handle a case where the minimum safe version of a dependency drops support for Python 3.10 (the project's minimum)?
- What happens if the `mcp-vss>=2025.6.1.dev5` package is not yet compatible with `mcp[cli]>=1.23.0`?
- Does raising the `wheel` minimum version affect the `test` and `dev` dependency groups differently than expected?
- What if the lock file regeneration resolves `mcp` to a version between 1.19.0 and 1.23.0 due to constraints from `mcp-vss`?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The project MUST raise the `cryptography` version constraint from `>=44.0.0` to `>=46.0.6` to resolve CVE-2024-12797 (LOW), CVE-2026-26007 (HIGH), and CVE-2026-34073 (LOW). The current lock file already resolves to 46.0.6, so only the constraint floor needs updating.
- **FR-002**: The project MUST raise the `jinja2` version constraint from `>=2.10` to `>=3.1.5` to resolve CVE-2020-28493 (MEDIUM), CVE-2024-22195 (MEDIUM), and CVE-2024-56326 (MEDIUM). The current lock file already resolves to 3.1.6, so only the constraint floor needs updating.
- **FR-003**: The project MUST update `wheel` from `==0.45.1` to `>=0.46.2` in all three locations where it appears (test optional-dependencies, dev optional-dependencies, uv dev-dependencies) to resolve CVE-2026-24049 (HIGH). This is a hard-pinned version that currently resolves to the vulnerable version.
- **FR-004**: The project MUST raise the `mcp[cli]` version constraint from `>=1.7.1` to `>=1.23.0` in the MCP optional dependency group to resolve CVE-2025-53365 (HIGH), CVE-2025-53366 (HIGH), and CVE-2025-66416 (HIGH). The current lock file resolves to 1.19.0 which is still vulnerable.
- **FR-005**: The project MUST maintain compatibility with Python >=3.10 after all dependency updates.
- **FR-006**: All dependency version changes MUST be reflected consistently across all locations in the dependency manifest where the package appears (main dependencies, optional-dependencies groups, and tool-specific dev-dependencies).
- **FR-007**: The lock file MUST be regenerated after constraint updates to ensure all resolved versions meet or exceed the minimum safe versions.
- **FR-008**: The project MUST have zero known high, critical, or medium severity CVEs in its dependency tree after the updates are applied.

### Key Entities

- **Dependency Manifest**: The central configuration defining all project dependencies and their version constraints. Contains main dependencies, optional dependency groups (stor, test, dev, mcp), and tool-specific dev-dependencies. The `wheel` package appears in 3 locations; `cryptography` and `jinja2` in 1 location each; `mcp[cli]` in 1 location.
- **Lock File**: The resolved dependency tree that must be regenerated after version constraint changes. Currently resolves `cryptography` to 46.0.6 (safe), `jinja2` to 3.1.6 (safe), `wheel` to 0.45.1 (vulnerable), and `mcp` to 1.19.0 (vulnerable).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A dependency security scan of the updated project reports zero known CVEs of any severity across all declared dependencies.
- **SC-002**: The project's existing test suite passes with 100% of previously passing tests still passing after dependency updates.
- **SC-003**: The CLI installs successfully in a clean environment with the updated dependencies without any dependency resolution conflicts.
- **SC-004**: All four affected packages (`cryptography`, `jinja2`, `wheel`, `mcp`) have version constraints at or above their minimum safe versions: `cryptography>=46.0.6`, `jinja2>=3.1.5`, `wheel>=0.46.2`, `mcp[cli]>=1.23.0`.
- **SC-005**: The regenerated lock file resolves all four packages to versions at or above the minimum safe thresholds.

## Assumptions

- The updated dependency versions maintain backward compatibility with the project's existing usage patterns. Specifically:
  - `cryptography>=46.0.6` remains compatible with the AES-256-GCM, PBKDF2HMAC, and AESGCM APIs used in the encrypted credential backend.
  - `jinja2>=3.1.5` remains compatible as a transitive dependency (not directly imported by CLI code).
  - `wheel>=0.46.2` remains compatible as a build/test tool dependency.
  - `mcp[cli]>=1.23.0` remains compatible with `mcp-vss>=2025.6.1.dev5` and the `mcp_server_vss.server.create_app` API used in the MCP plugin.
- Python >=3.10 remains supported by all updated dependency versions.
- The `pyvss==2026.4.0` package is compatible with `cryptography>=46.0.6` and `jinja2>=3.1.5`.
- The lock file can be successfully regenerated with the updated constraints without conflicting transitive dependency requirements.
- No additional CVEs beyond those identified (10 total across 4 packages) exist in the current dependency set.
