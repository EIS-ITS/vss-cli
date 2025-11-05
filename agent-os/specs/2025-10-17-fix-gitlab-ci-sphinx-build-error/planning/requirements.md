# Spec Requirements: Fix GitLab CI Sphinx Build Error

## Initial Description
**Description**: Fix GitLab CI error in release-docs-tag-confluence step where sphinx-build command is not found

**Context**:
- The CI pipeline step `release-docs-tag-confluence` is failing with error "sphinx-build: not found"
- The step attempts to run: `sphinx-build -b confluence docs docs/_build/confluence -E -a`
- Error occurs at line 197 with exit code 127 (command not found)
- This is a CI/CD pipeline configuration issue in .gitlab-ci.yml

**Goal**: Fix the missing sphinx-build dependency in the GitLab CI configuration so the Confluence documentation release step can execute successfully.

## Requirements Discussion

### First Round Questions

**Q1:** I assume we should follow the exact pattern from the working `build-docs-tag` job (lines 350-374) which includes:
- Installing system dependencies with apk
- Creating and activating virtual environment: `uv venv && source .venv/bin/activate`
- Installing Python dependencies: `uv sync --locked --all-extras && uv pip install .`
- Then running sphinx-build commands

Is that the correct approach?

**Answer:** Yes - follow the exact pattern from `build-docs-tag` (lines 350-374)

**Q2:** Should we:
- Option A: Keep independent - rebuild everything in release job (current approach)
- Option B: Add dependency: Add `dependencies: - build-docs-tag` to reuse artifacts where possible (follows pattern of `release-docs-tag` job)

**Answer:** Option B - Add dependency: Add `dependencies: - build-docs-tag` to reuse artifacts where possible (follows pattern of `release-docs-tag` job)

### Existing Code to Reference

**Similar Features Identified:**
- Feature: build-docs-tag job - Path: `.gitlab-ci.yml` (lines 350-374)
  - Complete working pattern for sphinx-build execution with uv
  - Shows proper virtual environment setup and activation
  - Demonstrates all necessary system dependencies

- Feature: release-docs-tag job - Path: `.gitlab-ci.yml` (line 387 onwards)
  - Shows pattern of adding `dependencies:` to reuse build artifacts
  - The failing job uses `needs:` (line 377) but should also use `dependencies:`

**Pattern to Follow:**
The `build-docs-tag` job successfully runs sphinx-build by:
1. Installing system dependencies (line 354)
2. Creating and activating virtual environment (line 355)
3. Synchronizing dependencies and installing package (line 356)
4. Running sphinx-build commands (lines 357-359)

### Visual Assets

**Files Provided:**
No visual assets provided.

**Visual Insights:**
N/A - This is a CI/CD configuration fix based on error logs and existing working patterns.

## Requirements Summary

### Problem Statement
The `release-docs-tag-confluence` job fails with "sphinx-build: not found" error (exit code 127) when attempting to publish documentation to Confluence for tagged releases.

### Root Cause Analysis
The job configuration at lines 376-385 has the following issues:
1. No virtual environment creation or activation before running `uv sync`
2. The virtual environment created by `uv sync` is not activated before running `sphinx-build`
3. Missing `uv pip install .` step to ensure the package and its dependencies (including sphinx) are properly installed in the activated environment
4. Uses `needs:` but not `dependencies:` to reference build-docs-tag artifacts

**Current failing configuration (lines 376-385):**
```yaml
release-docs-tag-confluence:
  image: hub.eis.utoronto.ca/vss/docker/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
  stage: release
  needs: ["build-docs-tag"]
  script:
    - uv sync --locked --all-extras
    - export CONFLUENCE_DRYRUN= && sphinx-build -b confluence docs docs/_build/confluence -E -a
  only:
    - /^v\d+\.\d+\.\d+([abc]\d*)?$/
  tags:
    - python-3
```

### Solution Approach
Follow the exact pattern from the working `build-docs-tag` job (lines 350-374) and add artifact dependency similar to `release-docs-tag` job.

**Required changes:**
1. Add system dependencies installation: `apk add --update --no-cache git libxml2-dev libxslt-dev gcc python3-dev musl-dev make`
2. Add virtual environment creation and activation: `uv venv && source .venv/bin/activate`
3. Update dependency installation: `uv sync --locked --all-extras && uv pip install .`
4. Add `dependencies: - build-docs-tag` to reuse artifacts from the build stage
5. Keep existing sphinx-build command: `export CONFLUENCE_DRYRUN= && sphinx-build -b confluence docs docs/_build/confluence -E -a`

### Functional Requirements
- The `release-docs-tag-confluence` job must successfully execute sphinx-build to publish documentation to Confluence
- The job must run only on version tags matching the pattern `/^v\d+\.\d+\.\d+([abc]\d*)?$/`
- The job must properly activate the virtual environment before running any Python commands
- The job must reuse artifacts from the `build-docs-tag` job when available
- Sphinx-build command must be accessible in the activated virtual environment

### Non-Functional Requirements
- Follow existing patterns in the codebase (consistency with `build-docs-tag` job)
- Minimize build time by reusing artifacts where possible
- Maintain proper error handling (exit codes should be meaningful)
- Use the same Docker image as other uv-based jobs for consistency
- Pipeline execution time should remain similar to current duration

### Reusability Opportunities
- The `build-docs-tag` job (lines 350-374) provides the complete working pattern
- The `release-docs-tag` job (line 387 onwards) demonstrates the `dependencies:` pattern
- The `build-docs-develop` job (lines 105-128) shows a similar pattern for the develop branch
- All documentation build jobs use the same venv activation approach

### Scope Boundaries

**In Scope:**
- Fix the `release-docs-tag-confluence` job configuration in `.gitlab-ci.yml`
- Add proper virtual environment setup and activation
- Add system dependencies installation
- Update dependency installation command
- Add artifacts dependency declaration

**Out of Scope:**
- Changes to other CI jobs (unless they have the same issue)
- Modifications to sphinx configuration
- Changes to Confluence publishing logic or API integration
- Updates to documentation content
- Changes to Docker image or base dependencies
- Optimization of pipeline execution time beyond artifact reuse
- Modifications to uv version or Python version

### Technical Considerations

**File to Modify:**
- `.gitlab-ci.yml` (lines 376-385)

**Environment Details:**
- Docker Image: `hub.eis.utoronto.ca/vss/docker/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER`
- UV Version: 0.7.13
- Python Version: 3.13
- Base Layer: Alpine
- UV Link Mode: `copy` (due to GitLab CI mountpoint behavior)

**System Dependencies Required:**
- git
- libxml2-dev
- libxslt-dev
- gcc
- python3-dev
- musl-dev
- make

**Specific Changes Required:**
1. Add `dependencies:` key with `- build-docs-tag` (after or replacing `needs:`)
2. Add system dependencies installation as first script step
3. Add virtual environment creation and activation as second script step
4. Update `uv sync` command to include `&& uv pip install .`
5. Keep existing sphinx-build command unchanged

**Expected Job Configuration After Fix:**
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

**Key Technical Notes:**
- Virtual environment is created at `.venv` by uv
- Environment variable `CONFLUENCE_DRYRUN` is cleared (empty) to enable actual Confluence publishing, unlike build jobs that set it to `1` for dry-run mode
- The `source .venv/bin/activate` is critical for making sphinx-build available in PATH
- The `uv pip install .` ensures the current package and all its dependencies are installed in the activated environment

### Expected Outcome
- The `release-docs-tag-confluence` job should execute successfully on tagged releases
- The sphinx-build command should be found and executable within the activated virtual environment
- Documentation should be successfully published to Confluence (not in dry-run mode)
- The CI pipeline should complete without errors in this job
- Exit code should be 0 on success instead of 127 (command not found)
- Job should reuse artifacts from `build-docs-tag` when available to improve efficiency

### Verification Steps
1. Trigger the CI pipeline on a version tag matching `/^v\d+\.\d+\.\d+([abc]\d*)?$/`
2. Verify the `release-docs-tag-confluence` job completes successfully
3. Confirm sphinx-build command is found and executed
4. Verify Confluence documentation is published correctly (not in dry-run mode)
5. Check that the job reuses artifacts from `build-docs-tag`
6. Confirm exit code is 0 instead of 127
7. Verify no regression in other CI jobs
