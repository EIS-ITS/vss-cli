<!--
=============================================================================
SYNC IMPACT REPORT
=============================================================================
Version change: 1.0.0 → 1.1.0 (MINOR: materially expanded guidance from
  _docs/ directory — IaC/YAML spec capability added to Principle II, MCP
  added to Principle II and Technology Standards, Google-style docstrings
  and single-quote preference codified in Principle V and Technology
  Standards, bump2version added to Principle V workflow and Technology
  Standards, CSV output format corrected in Principle II, requests.Session
  requirement added to Principle III, sub-plugin entry-point rule added to
  Principle I, WorkerQueue concurrency rule added to Principle IV, Roadmap
  alignment note added to Governance, Mission section added as preamble.)

Modified principles:
  - I. Plugin-First Architecture → I. Plugin-First Architecture
    (added sub-plugin entry-point registration rule)
  - II. CLI Interface Contract → II. CLI Interface Contract
    (added IaC YAML specifications, CSV output format, MCP surface)
  - III. Security & Credential Integrity → III. Security & Credential Integrity
    (added requests.Session/header-level auth rule, explicit precedence order)
  - IV. Observability & Request Transparency → IV. Observability & Request
    Transparency (added WorkerQueue bounded-concurrency rule)
  - V. Simplicity & Calendar Versioning → V. Simplicity & Calendar Versioning
    (added bump2version mandate, single-quote preference, Google docstrings,
    optional extras gate for new dependencies)

Added sections:
  - Mission (new preamble section capturing project purpose and users)

Removed sections: none

Templates reviewed & updated:
  ✅ .specify/templates/plan-template.md — Constitution Check table version
       reference updated to v1.1.0; IaC/MCP gate question added to row II;
       bump2version noted in Technical Context; no structural changes
  ✅ .specify/templates/spec-template.md — no structural changes required;
       existing mandatory sections align with updated principles
  ✅ .specify/templates/tasks-template.md — path conventions already match;
       no changes required
  ✅ .specify/templates/agent-file-template.md — generic template; no
       outdated references

Follow-up TODOs:
  - None. All placeholders resolved.
=============================================================================
-->

# VSS CLI Constitution

## Mission

VSS CLI is a comprehensive command-line interface that helps University of
Toronto researchers, faculty, IT staff, and DevOps engineers manage ITS
Private Cloud resources efficiently. It provides intuitive VM lifecycle
management, Infrastructure as Code capabilities, and AI-powered contextual
assistance.

**Primary users**: Academic institutions (research computing administrators,
faculty researchers) and IT operations teams (DevOps/platform engineers)
managing private cloud infrastructure at the University of Toronto.

**Core differentiators**: Purpose-built for ITS Private Cloud with native
MFA/TOTP, YAML-based Infrastructure as Code for version-controlled
deployments, integrated GPT-powered assistant (UTORcloudy) with
chain-of-thought reasoning, and Model Context Protocol (MCP) support for
AI-agent-driven cloud operations.

## Core Principles

### I. Plugin-First Architecture

Every new command group MUST be implemented as a plugin module under
`vss_cli/plugins/`. Plugins MUST export a top-level `cli` Click group object
so that `VssCli.get_command()` can load them dynamically. No command logic
MUST be placed directly in `vss_cli/cli.py` beyond dispatch and global options.
Shared options MUST live in `vss_cli/rel_opts.py` (global) or a
`rel_opts.py` file co-located with the plugin (plugin-scoped).

Sub-plugin groups (e.g., `compute_plugins/`) MUST be loaded via
`click_plugins.with_plugins()` and registered through `pyproject.toml`
entry points (`vss_cli.contrib.<group>`).

**Rationale**: Dynamic plugin discovery enables independent development,
testing, and optional loading of feature sets without modifying the core
dispatcher. Coupling commands to `cli.py` creates merge conflicts and
undermines the extensibility model.

### II. CLI Interface Contract

All commands MUST follow the text I/O contract:

- **Input**: CLI arguments/options → `stdin` for piped data; YAML/JSON
  specification files for Infrastructure as Code workflows
- **Output**: structured data to `stdout` via `format_output()` with
  predefined `COLUMNS_*` constants defined in `vss_cli/const.py`
- **Output formats** supported MUST include: `json`, `yaml`, `table`,
  `auto`, `ndjson`; `csv` MUST be supported where bulk data export is
  relevant
- **Errors**: user-facing messages to `stderr` via `VssCliError`; raw
  stack traces or API internals MUST NOT be exposed to end users
- **Long-running operations** MUST use `ctx.spinner()` with
  `disable=ctx.debug` and report status via the request tracking system
  (`ctx.wait_for_request_to()`)
- **Infrastructure as Code**: YAML-based VSS CLI specification files MUST
  be supported for declarative, version-controlled provisioning of cloud
  resources; spec files MUST be validated before submission to the API
- **MCP integration**: CLI functions exposed as Model Context Protocol tools
  (via `vss_cli/plugins/mcp.py`) MUST follow the same I/O contract and
  MUST NOT introduce separate authentication or output paths

**Rationale**: A predictable I/O contract enables scripting, CI/CD
integration, IaC workflows, and AI-agent access through MCP — all with
consistent UX. Spinner suppression in debug mode preserves log readability.

### III. Security & Credential Integrity

- Credentials (tokens, passwords, API keys) MUST never be logged, printed
  to `stdout`, or committed to version control
- Configuration files MUST be stored under `~/.vss-cli/` with restricted
  file-system permissions
- Environment variables (`VSS_*` prefix) MUST override file-based config
  and MUST take precedence in CI/CD contexts; precedence order is:
  CLI arguments > environment variables > config file > defaults
- MFA/TOTP MUST be supported and MUST NOT be bypassed programmatically
  without explicit user consent
- AI assistant sessions MUST use ephemeral, per-session API keys generated
  via `_generate_assistant_api_key()`; keys MUST NOT be persisted after
  session end
- All API communication MUST use HTTPS; plaintext HTTP endpoints MUST be
  rejected
- `requests.Session` MUST be used for persistent connections; `User-Agent`
  and `Authorization` headers MUST be set at session level, not per-request

**Rationale**: VSS CLI operates against production cloud infrastructure at
the University of Toronto. A single credential leak can expose multi-tenant
resources. Security constraints are non-negotiable and take precedence over
developer convenience.

### IV. Observability & Request Transparency

- All asynchronous cloud operations MUST be submitted via the ITS Private
  Cloud request system and MUST return a trackable request ID
- The CLI MUST provide `--wait` / `wait_for_request_to()` semantics so
  users can block until an operation completes
- Module-level loggers (`logging.getLogger(__name__)`) MUST be used;
  ad-hoc `print()` debugging MUST NOT appear in committed code
- Spinner feedback (`ctx.spinner()`) MUST be used for all operations that
  invoke the remote API, so users receive visual confirmation of activity
- Bulk / parallel operations MUST use `WorkerQueue` for concurrent
  request processing with bounded concurrency

**Rationale**: Cloud operations are inherently asynchronous. Transparent
request tracking prevents users from re-issuing duplicate operations and
enables audit trails. Structured logging supports debugging without
polluting normal output.

### V. Simplicity & Calendar Versioning

- Calendar versioning (`YYYY.M.PATCH`) MUST be used for all releases;
  semantic versioning MUST NOT be introduced
- Version bumps MUST be performed with `bump2version` (patch/minor/major);
  manual edits to version strings MUST NOT be made in isolation
- New dependencies MUST be justified; prefer the existing stack (Click,
  pyvss, tabulate, ruamel.yaml, rich) before adding third-party libraries;
  optional feature sets MUST be gated behind `pyproject.toml` extras
- Python `>=3.10` MUST be the minimum runtime target; no backports for
  older versions MUST be added
- Code MUST be formatted with Black (line length 79, `skip-string-
  normalization = true` — single quotes preferred) and pass `flake8`
  linting before merging
- Type hints MUST be used for all new public functions and configuration
  methods; inline `Any` casts MUST be documented with a rationale comment
- Docstrings for public functions MUST follow Google style
- YAGNI: features MUST NOT be built speculatively; every addition requires
  a concrete user story or issue reference

**Rationale**: Calendar versioning communicates release cadence directly.
Strict style enforcement (Black + flake8, single quotes, Google docstrings)
and a stable dependency set reduce cognitive overhead for contributors and
maintainers across Python versions.

## Technology Standards

**Runtime**: Python >=3.10 (CPython; 3.10, 3.11, 3.12, 3.13 tested)
**CLI Framework**: Click 8.x — groups, commands, options, decorators
**API Client**: pyvss >=2025.2.1 — inherits `VssManager` in `config.py`
**Package Manager**: uv (development); pip-compatible via `pyproject.toml`
**Output Formatting**: tabulate, rich (progress/spinners), jsonpath-ng
**Configuration**: ruamel.yaml — YAML files under `~/.vss-cli/`
**Testing**: nose (primary), pytest (secondary); mocks via `unittest.mock`
**Linting/Formatting**: flake8 + Black (line length 79, single quotes)
**Documentation**: Sphinx (Google-style docstrings) — source in `docs/`
**Version Management**: bump2version — `bump2version patch|minor|major`
**Distribution**: PyPI, Homebrew formula (`scripts/update_homebrew_formula.py`), Docker image
**MCP Integration**: mcp-vss (optional extra) — exposes CLI as Claude tools
**Repository**: GitLab EE — `main` (production), `develop` (integration)
**CI/CD**: GitLab CI pipelines with SAST and coverage reporting

Deviations from this stack MUST be proposed as a constitution amendment and
MUST include: dependency justification, security review, and migration plan.

## Development Workflow

1. **Branch from `develop`** using the naming convention
   `YYYY-MM-DD-<kebab-slug>`
2. **Create or update spec** in `specs/<branch>/` before writing code
3. **Constitution Check** (see plan-template.md): verify the implementation
   plan passes all five principle gates before Phase 0 research begins
4. **Implement** in the plugin directory (`vss_cli/plugins/`) following the
   plugin entry-point pattern
5. **Test**: add or update tests under `tests/`; at minimum cover the
   primary user flow; mock all `pyvss` API calls via `unittest.mock`
6. **Lint & format**: `flake8 vss_cli/` and `black --line-length 79 vss_cli/`
   MUST pass with zero errors
7. **Merge request**: reference the issue/spec; reviewers MUST verify
   constitution compliance before approval
8. **Release**: run `uvx bump2version patch|minor|major` to update version
   strings; tag `YYYY.M.PATCH` on `main` after MR merge; update
   `CHANGELOG.md` and Homebrew formula via
   `scripts/update_homebrew_formula.py`

All PRs/reviews MUST include a Constitution Check comment confirming
compliance or documenting justified exceptions.

## Governance

- This constitution supersedes all other development practices and informal
  conventions for the VSS CLI project
- **Amendment procedure**: open a merge request against `develop` modifying
  `.specify/memory/constitution.md`; increment `CONSTITUTION_VERSION` per
  the versioning rules below; obtain at least one maintainer approval; run
  the `speckit.constitution` agent to propagate changes to all dependent
  templates
- **Versioning policy**:
  - MAJOR: removal or backward-incompatible redefinition of a principle
  - MINOR: new principle or section added, or materially expanded guidance
  - PATCH: clarifications, wording improvements, typo fixes
- **Compliance review**: all code reviews MUST verify adherence to the five
  Core Principles; violations MUST be noted and either corrected before
  merge or logged as a justified exception with a follow-up issue
- **Roadmap alignment**: active development phases (Testing & Quality
  Q1 2026, Async & Performance Q2 2026, Advanced Integrations Q3 2026)
  MUST be reviewed at the start of each phase to confirm no constitution
  amendments are required before work begins
- **Runtime guidance**: consult `CLAUDE.md` / `AGENTS.md` for AI-agent
  development context; `_docs/` for architecture, API integration, plugin
  system, and product mission details; this constitution for governance
  authority

**Version**: 1.1.0 | **Ratified**: 2026-04-06 | **Last Amended**: 2026-04-06
