# Technical Stack

> Last Updated: 2025-10-05
> Version: 1.0.0

## Application Framework

- **Framework:** Python
- **Version:** 3.10+
- **CLI Framework:** Click
- **Architecture:** Plugin-based command structure with dynamic discovery

## Database

- **Primary Database:** n/a (API-driven, no local database)
- **API Client:** pyvss (>=2025.2.1) for ITS Private Cloud REST API integration

## JavaScript

- **Framework:** n/a (CLI application)

## Import Strategy

- **Strategy:** n/a (Python package management via uv/pip)

## CSS Framework

- **Framework:** n/a (CLI application)

## UI Component Library

- **Library:** Rich, Tabulate
- **Purpose:** Terminal output formatting, progress indicators, and table rendering
- **Emoji Support:** Interactive feedback indicators for AI assistant responses

## Fonts Provider

- **Provider:** n/a (terminal-based)

## Icon Library

- **Library:** Emoji support for assistant feedback (👍/👎)
- **Unicode Support:** UTF-8 for cross-platform terminal compatibility

## Application Hosting

- **Primary:** PyPI (Python Package Index)
- **Secondary:** Homebrew (macOS package manager)
- **Container:** Docker images for containerized deployments

## Database Hosting

- **Hosting:** n/a (stateless CLI application)
- **Configuration Storage:** Local YAML files (~/.vss-cli/config.yaml)

## Asset Hosting

- **Repository:** GitLab Enterprise Edition
- **URL:** https://gitlab-ee.eis.utoronto.ca/vss/vss-cli
- **Access:** Internal University of Toronto infrastructure

## Deployment Solution

- **Package Distribution:** PyPI package distribution with calendar versioning (YYYY.M.PATCH)
- **Homebrew Formula:** Automated formula generation for macOS installation
- **Version Management:** Git tags with automated release workflows

## Code Repository

- **URL:** https://gitlab-ee.eis.utoronto.ca/vss/vss-cli
- **Branching Strategy:** main (production), develop (integration)
- **Issue Tracking:** GitLab Issues with automated linking

## Additional Technology Components

### API Integration
- **REST Client:** pyvss library for ITS Private Cloud API
- **Authentication:** JWT tokens with MFA/TOTP support
- **Request Handling:** Automatic retry, pagination, and filtering

### Configuration Management
- **Format:** YAML (ruamel.yaml)
- **Storage:** User home directory (~/.vss-cli/)
- **Environment Variables:** VSS_* prefixed overrides

### Data Processing
- **JSON Handling:** jsonpath-ng for nested data extraction
- **YAML Processing:** ruamel.yaml for configuration parsing
- **Table Formatting:** tabulate for structured output

### Storage Integration
- **Object Storage:** MinIO client for vskey-stor integration
- **VPN Support:** Integrated VPN management for secure storage access

### AI Integration
- **Assistant API:** GPT-powered contextual help (UTORcloudy)
- **Reasoning Support:** Chain-of-thought responses for complex queries
- **Authentication:** Session-based API key generation with Bearer tokens

### Testing & Quality
- **Test Framework:** nose for unit and integration testing
- **Code Quality:** flake8 for linting and style enforcement
- **Coverage:** coverage.py for test coverage analysis
- **Documentation:** Sphinx for API documentation generation

### Development Tools
- **Package Manager:** uv (modern Python package installer)
- **Dependency Management:** pyproject.toml with optional feature sets
- **Build System:** setuptools with dynamic versioning

### Model Context Protocol (MCP)
- **Integration:** mcp-vss for Claude AI agent integration
- **Tool Registration:** Exposes CLI functions as Claude-accessible tools
- **Context Sharing:** Standardized protocol for AI-driven cloud operations
