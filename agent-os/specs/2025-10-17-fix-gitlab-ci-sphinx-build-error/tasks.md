# Task Breakdown: Fix GitLab CI Sphinx Build Error

## Overview
Total Tasks: 3
Assigned roles: None (Direct implementation - this is a configuration fix, not a feature requiring specialized agents)

## Context

This is a CI/CD configuration fix to resolve a "sphinx-build: not found" error in the `release-docs-tag-confluence` GitLab CI job. The solution involves following the exact pattern from the working `build-docs-tag` job by adding proper virtual environment creation and activation.

Since this is a single-file configuration change (`.gitlab-ci.yml`), it does not require the typical multi-agent workflow with specialized implementers. The task breakdown below is structured for direct implementation.

## Task List

### Configuration Fix

#### Task Group 1: Preparation & Analysis
**Assigned implementer:** Direct implementation (no specialized agent required)
**Dependencies:** None

- [x] 1.0 Complete preparation and analysis
  - [x] 1.1 Review the current failing job configuration
    - Read lines 376-385 of `.gitlab-ci.yml` (the `release-docs-tag-confluence` job)
    - Understand the current script steps and why sphinx-build is not found
  - [x] 1.2 Review the working pattern from build-docs-tag job
    - Read lines 350-374 of `.gitlab-ci.yml` (the `build-docs-tag` job)
    - Identify the key differences in environment setup
    - Note the three-step pattern: apk add, uv venv && source, uv sync && uv pip install
  - [x] 1.3 Review artifact reuse pattern
    - Read lines 387-407 of `.gitlab-ci.yml` (the `release-docs-tag` job)
    - Understand how to add `dependencies:` key for artifact reuse
  - [x] 1.4 Verify consistency with other documentation build jobs
    - Check `build-docs-develop` (lines 105-128) for pattern confirmation
    - Check `build-docs-main` (lines 252-274) for pattern confirmation

**Acceptance Criteria:**
- Understanding of the root cause (missing venv activation)
- Clear picture of the required changes based on working patterns
- Confirmation that the pattern is consistent across multiple jobs

#### Task Group 2: Implementation
**Assigned implementer:** Direct implementation (no specialized agent required)
**Dependencies:** Task Group 1

- [x] 2.0 Complete the CI configuration fix
  - [x] 2.1 Add artifact dependency configuration
    - Add `needs: ["build-docs-tag"]` if not already present
    - Add `dependencies:` key with `- build-docs-tag` to reuse artifacts
  - [x] 2.2 Add system dependencies installation
    - Insert `apk add --update --no-cache git libxml2-dev libxslt-dev gcc python3-dev musl-dev make` as first script step
    - This matches the exact dependency list from build-docs-tag job
  - [x] 2.3 Add virtual environment creation and activation
    - Insert `uv venv && source .venv/bin/activate` as second script step
    - This creates .venv directory and activates it, making Python tools available
  - [x] 2.4 Update dependency installation step
    - Replace `uv sync --locked --all-extras` with `uv sync --locked --all-extras && uv pip install .`
    - The `&& uv pip install .` ensures the package and sphinx are installed in activated environment
  - [x] 2.5 Keep existing sphinx-build command unchanged
    - Verify `export CONFLUENCE_DRYRUN= && sphinx-build -b confluence docs docs/_build/confluence -E -a` remains as-is
    - The empty CONFLUENCE_DRYRUN value enables actual publishing (not dry-run)

**Expected Configuration After Changes:**
```yaml
release-docs-tag-confluence:
  image: hub.eis.utoronto.ca/vss/docker/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
  stage: release
  needs: ["build-docs-tag"]
  dependencies:
    - build-docs-tag
  script:
    - apk add --update --no-cache git libxml2-dev libxslt-dev gcc python3-dev musl-dev make
    - uv venv && source .venv/bin/activate
    - uv sync --locked --all-extras && uv pip install .
    - export CONFLUENCE_DRYRUN= && sphinx-build -b confluence docs docs/_build/confluence -E -a
  only:
    - /^v\d+\.\d+\.\d+([abc]\d*)?$/
  tags:
    - python-3
```

**Acceptance Criteria:**
- All script steps follow the exact pattern from build-docs-tag job
- System dependencies are installed before Python operations
- Virtual environment is created and activated before running any Python commands
- Package installation includes both `uv sync` and `uv pip install .`
- Artifact reuse is configured with dependencies key
- Sphinx-build command remains unchanged
- Configuration matches style and format of other documentation jobs

#### Task Group 3: Verification & Testing
**Assigned implementer:** Direct implementation (no specialized agent required)
**Dependencies:** Task Group 2

- [x] 3.0 Complete verification and testing
  - [x] 3.1 Review the changes for accuracy
    - Verify the configuration matches the working build-docs-tag pattern exactly
    - Check that all required steps are included in the correct order
    - Ensure no syntax errors in YAML formatting
  - [x] 3.2 Document the testing strategy
    - Note: Actual testing requires pushing to GitLab and triggering the pipeline
    - Testing must be done on a version tag matching `/^v\d+\.\d+\.\d+([abc]\d*)?$/`
    - Recommended: Test with a release candidate tag (e.g., v2025.10.0rc1) before production
  - [x] 3.3 Define verification steps for CI pipeline execution
    - Pipeline will be triggered by creating/pushing a version tag
    - Monitor the `release-docs-tag-confluence` job in the release stage
    - Check job logs for successful execution of each script step
    - Verify sphinx-build is found and executes successfully
    - Confirm exit code is 0 instead of 127
    - Verify Confluence documentation is published (CONFLUENCE_DRYRUN is empty)
  - [x] 3.4 Prepare rollback plan
    - Document current configuration for potential rollback if needed
    - Keep original lines 376-385 available for reference
    - Note: Rollback would involve reverting to simpler script structure

**Expected Job Log Output (Success Indicators):**
```
$ apk add --update --no-cache git libxml2-dev libxslt-dev gcc python3-dev musl-dev make
OK: [package count] MiB in [package count] packages
$ uv venv && source .venv/bin/activate
Using Python 3.13 interpreter at: ...
Creating virtualenv at: .venv
$ uv sync --locked --all-extras && uv pip install .
[dependency installation output]
$ export CONFLUENCE_DRYRUN= && sphinx-build -b confluence docs docs/_build/confluence -E -a
Running Sphinx v7.2.2
[sphinx build output]
build succeeded.
Job succeeded
```

**Acceptance Criteria:**
- Changes are reviewed and match the working pattern
- Testing strategy is documented and clear
- Verification steps are defined for pipeline execution
- Success indicators are identified in job logs
- Rollback plan is available if needed

## Execution Order

Recommended implementation sequence:
1. Preparation & Analysis (Task Group 1) - Understand the problem and solution pattern
2. Implementation (Task Group 2) - Apply the fix to .gitlab-ci.yml
3. Verification & Testing (Task Group 3) - Review changes and prepare for CI testing

## Implementation Notes

### Why This Task Structure?

Unlike typical feature implementations that require database models, API endpoints, UI components, and comprehensive testing, this is a focused CI/CD configuration fix that:

- Modifies a single file (`.gitlab-ci.yml`)
- Follows an existing, proven pattern from the same file
- Requires no new code, only configuration adjustments
- Does not involve application logic, database schemas, or user interfaces
- Can be fully verified through CI pipeline execution

Therefore, specialized implementer agents (database-engineer, api-engineer, ui-designer, testing-engineer) are not needed. The task is structured for direct implementation with clear preparation, implementation, and verification phases.

### Key Technical Context

**Root Cause:** The virtual environment created by `uv sync` is not activated before running `sphinx-build`, causing the command to not be found in PATH (error 127).

**Solution:** Follow the three-step pattern used successfully in all other documentation build jobs:
1. Install system dependencies with `apk add`
2. Create and activate virtual environment with `uv venv && source .venv/bin/activate`
3. Install Python dependencies with `uv sync --locked --all-extras && uv pip install .`

**Critical Details:**
- The `source .venv/bin/activate` command modifies the shell PATH to include the virtual environment's bin directory
- The `uv pip install .` step installs the current package (vss-cli) and all its dependencies, including Sphinx, into the activated environment
- The `dependencies:` key enables artifact reuse from build-docs-tag, improving build efficiency
- The `CONFLUENCE_DRYRUN=` (empty) environment variable enables actual publishing, unlike the dry-run mode used in build jobs

### References to Existing Patterns

**Working Pattern:** `build-docs-tag` job (lines 350-374 in `.gitlab-ci.yml`)
- This job successfully builds documentation using the exact pattern we need to replicate
- All script steps work in the correct order with proper environment activation

**Artifact Reuse Pattern:** `release-docs-tag` job (lines 387+ in `.gitlab-ci.yml`)
- Shows how to use `needs:` and `dependencies:` keys together
- Enables downloading artifacts from build-docs-tag job

**Consistent Pattern:** Also used in:
- `build-docs-develop` (lines 105-128)
- `build-docs-main` (lines 252-274)

### Testing Approach

Since this is CI/CD configuration, testing happens in the GitLab CI environment:

1. **Pre-deployment validation:** Review changes for syntax and pattern accuracy
2. **Test environment:** Use a release candidate tag (e.g., `v2025.10.0rc1`) for initial testing
3. **Success criteria:** Job completes with exit code 0, sphinx-build executes successfully, documentation is published
4. **Production deployment:** Apply to production tags after successful test run

### Alignment with User Standards

This implementation aligns with the user's standards as follows:

- **Coding Style (agent-os/standards/global/coding-style.md):**
  - Follows DRY principle by reusing the proven pattern from build-docs-tag
  - Maintains consistency with existing CI jobs
  - No dead code or unnecessary configuration

- **Tech Stack (agent-os/standards/global/tech-stack.md):**
  - Uses existing CI/CD tools (GitLab CI, uv, Docker)
  - Maintains current Alpine Linux base image
  - No new dependencies or tools introduced

- **Test Writing (agent-os/standards/testing/test-writing.md):**
  - Testing approach focuses on core functionality (CI job execution)
  - Verification is appropriate for infrastructure changes (pipeline execution)
  - No unit tests required for configuration files
