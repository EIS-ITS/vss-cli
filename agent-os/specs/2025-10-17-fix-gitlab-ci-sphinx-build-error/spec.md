# Specification: Fix GitLab CI Sphinx Build Error

## Goal
Fix the `release-docs-tag-confluence` CI job that fails with "sphinx-build: not found" error by properly activating the Python virtual environment before executing sphinx-build commands.

## User Stories
- As a release manager, I want the Confluence documentation to be published automatically when I create a version tag so that our documentation stays synchronized with releases.
- As a developer, I want the CI pipeline to complete successfully on tagged releases so that all release artifacts are properly deployed without manual intervention.
- As a documentation maintainer, I want the sphinx-build command to be available in the CI environment so that documentation builds can execute reliably.

## Core Requirements

### Functional Requirements
- The `release-docs-tag-confluence` job must successfully execute sphinx-build to publish documentation to Confluence
- The job must run only on version tags matching the pattern `/^v\d+\.\d+\.\d+([abc]\d*)?$/`
- The job must properly activate the Python virtual environment before running any Python commands
- The job must reuse artifacts from the `build-docs-tag` job when available
- Sphinx-build command must be accessible in the activated virtual environment with exit code 0 instead of 127

### Non-Functional Requirements
- Follow existing patterns in the codebase (consistency with `build-docs-tag` job)
- Minimize build time by reusing artifacts where possible
- Maintain proper error handling with meaningful exit codes
- Use the same Docker image as other uv-based jobs for consistency (hub.eis.utoronto.ca/vss/docker/uv:0.7.13-python3.13-alpine)
- Pipeline execution time should remain similar to current duration

## Problem Statement

### Current Behavior
The `release-docs-tag-confluence` job fails with error:
```
/bin/sh: sphinx-build: not found
ERROR: Job failed: exit code 127
```

### Root Cause Analysis
The job configuration at lines 376-385 of `.gitlab-ci.yml` has the following issues:

1. No virtual environment creation before running `uv sync`
2. The virtual environment is not activated before running `sphinx-build`
3. Missing `uv pip install .` step to ensure the package and its dependencies (including sphinx) are properly installed in the activated environment
4. Uses `needs:` but not `dependencies:` to reference build-docs-tag artifacts, missing opportunity for artifact reuse

### Current Failing Configuration
```yaml
release-docs-tag-confluence:
  image: hub.eis.utoronto.ca/vss/docker/uv:$UV_VERSION-python$PYTHON_VERSION-$BASE_LAYER
  stage: release
  script:
    - uv sync --locked --all-extras
    - export CONFLUENCE_DRYRUN= && sphinx-build -b confluence docs docs/_build/confluence -E -a
  only:
    - /^v\d+\.\d+\.\d+([abc]\d*)?$/
  tags:
    - python-3
```

## Reusable Components

### Existing Code to Leverage

**Working Pattern: build-docs-tag job (lines 350-374)**
- Location: `.gitlab-ci.yml`
- Pattern: Complete working implementation of sphinx-build execution with uv
- Components:
  - System dependencies installation: `apk add --update --no-cache git libxml2-dev libxslt-dev gcc python3-dev musl-dev make`
  - Virtual environment setup: `uv venv && source .venv/bin/activate`
  - Package installation: `uv sync --locked --all-extras && uv pip install .`
  - Sphinx-build execution with proper environment activation

**Artifact Reuse Pattern: release-docs-tag job (lines 387-407)**
- Location: `.gitlab-ci.yml`
- Pattern: Uses `dependencies:` key to reuse artifacts from build-docs-tag
- Components:
  - `needs:` declaration for job ordering
  - `dependencies:` declaration for artifact reuse

**Similar Jobs Using Same Pattern:**
- `build-docs-develop` (lines 105-128): Uses identical venv activation pattern
- `build-docs-main` (lines 252-274): Uses identical venv activation pattern

### New Components Required
None - this is a configuration fix using existing patterns.

## Technical Approach

### Environment Details
- Docker Image: `hub.eis.utoronto.ca/vss/docker/uv:0.7.13-python3.13-alpine`
- UV Version: 0.7.13
- Python Version: 3.13
- Base Layer: Alpine Linux
- UV Link Mode: `copy` (due to GitLab CI mountpoint behavior)

### System Dependencies Required
The following Alpine packages must be installed before building documentation:
- `git` - Version control operations
- `libxml2-dev` - XML processing for Confluence builder
- `libxslt-dev` - XSLT transformations for Confluence builder
- `gcc` - C compiler for building Python extensions
- `python3-dev` - Python development headers
- `musl-dev` - C standard library development files
- `make` - Build automation tool

### Python Dependencies
From `pyproject.toml` dev dependencies:
- `Sphinx==7.2.2` - Documentation generator
- `sphinxcontrib-confluencebuilder==2.10.1` - Confluence publishing extension

### Implementation Steps

1. Add `dependencies:` key to reuse artifacts from `build-docs-tag`
2. Add system dependencies installation as the first script step
3. Add virtual environment creation and activation as the second script step
4. Update dependency installation to include package installation: `uv sync --locked --all-extras && uv pip install .`
5. Keep existing sphinx-build command unchanged

### Expected Configuration After Fix
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

### Key Technical Details
- Virtual environment is created at `.venv` by uv
- Environment variable `CONFLUENCE_DRYRUN` is cleared (empty) to enable actual Confluence publishing, unlike build jobs that set it to `1` for dry-run mode
- The `source .venv/bin/activate` is critical for making sphinx-build available in PATH
- The `uv pip install .` ensures the current package and all its dependencies are installed in the activated environment
- The `needs:` key ensures job ordering (waits for build-docs-tag to complete)
- The `dependencies:` key downloads artifacts from build-docs-tag job

## Out of Scope
- Changes to other CI jobs (unless they have the same issue)
- Modifications to sphinx configuration files in `/docs` directory
- Changes to Confluence publishing logic or API integration
- Updates to documentation content
- Changes to Docker image or base dependencies
- Optimization of pipeline execution time beyond artifact reuse
- Modifications to uv version or Python version
- Changes to the tag pattern matching regex
- Updates to the Confluence dry-run logic

## Success Criteria
- The `release-docs-tag-confluence` job executes successfully on tagged releases matching `/^v\d+\.\d+\.\d+([abc]\d*)?$/`
- The sphinx-build command is found and executable within the activated virtual environment
- Documentation is successfully published to Confluence (not in dry-run mode)
- The CI pipeline completes without errors in this job
- Exit code is 0 on success instead of 127 (command not found)
- Job reuses artifacts from `build-docs-tag` to improve efficiency
- No regression in other CI jobs that use similar patterns

## Verification Steps

### Pre-Implementation Verification
1. Review the current failing job configuration at lines 376-385 in `.gitlab-ci.yml`
2. Review the working `build-docs-tag` job configuration at lines 350-374
3. Review the `release-docs-tag` job artifact reuse pattern at lines 387-407
4. Confirm the pattern is consistent with other documentation build jobs

### Post-Implementation Verification
1. Create or use an existing version tag matching the pattern `/^v\d+\.\d+\.\d+([abc]\d*)?$/`
2. Trigger the CI pipeline for that tag
3. Monitor the `release-docs-tag-confluence` job in the release stage
4. Verify the job completes successfully with exit code 0
5. Check the job log to confirm:
   - System dependencies are installed successfully
   - Virtual environment is created at `.venv`
   - Virtual environment is activated with `source .venv/bin/activate`
   - Dependencies are synchronized with `uv sync --locked --all-extras`
   - Package is installed with `uv pip install .`
   - sphinx-build command is found and executed
   - Confluence documentation is published (CONFLUENCE_DRYRUN is empty)
6. Verify artifacts from `build-docs-tag` are downloaded and available
7. Confirm no regression in other CI jobs (build-docs-tag, release-docs-tag, etc.)
8. Verify the total pipeline execution time is similar to previous runs

### Testing Strategy
Since this is a CI/CD configuration fix, testing will be performed in the GitLab CI environment:
- Test on a development tag first (e.g., `v2025.10.0rc1`) before production tags
- Monitor job logs for any errors or warnings
- Verify Confluence receives the documentation update
- Check that the job execution time is reasonable (should be similar to build-docs-tag job)
