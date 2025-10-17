# Product Mission

> Last Updated: 2025-10-05
> Version: 1.0.0

## Pitch

VSS CLI is a comprehensive command-line interface that helps University of Toronto researchers, faculty, IT staff, and DevOps engineers manage ITS Private Cloud resources efficiently by providing intuitive VM lifecycle management, Infrastructure as Code capabilities, and AI-powered contextual assistance.

## Users

### Primary Customers

- **Academic Institutions**: University departments and research groups requiring cloud infrastructure for computational workloads, data processing, and collaborative research projects
- **IT Operations Teams**: System administrators and DevOps engineers managing multi-tenant cloud environments with complex provisioning and compliance requirements

### User Personas

**Research Computing Administrator** (30-50 years old)
- **Role:** Senior Systems Administrator / Research Computing Lead
- **Context:** Manages cloud infrastructure for multiple research groups across various departments, handling hundreds of VMs with diverse requirements
- **Pain Points:** Manual VM provisioning is time-consuming, lack of Infrastructure as Code makes it difficult to replicate environments, tracking resource usage across projects is cumbersome
- **Goals:** Automate VM deployment workflows, implement version-controlled infrastructure configurations, simplify resource management for research teams

**DevOps Engineer** (25-40 years old)
- **Role:** Cloud Infrastructure Engineer / Platform Engineer
- **Context:** Responsible for deploying and maintaining development, staging, and production environments for university applications and services
- **Pain Points:** Inconsistent deployment processes, difficulty managing multi-environment configurations, limited programmatic access to cloud resources
- **Goals:** Implement CI/CD pipelines for infrastructure, maintain environment parity, reduce manual intervention in deployment processes

**Faculty Researcher** (35-65 years old)
- **Role:** Principal Investigator / Research Scientist
- **Context:** Runs computational research projects requiring scalable cloud resources with varying compute and storage needs
- **Pain Points:** Complex cloud interfaces requiring technical expertise, difficulty estimating and tracking resource costs, time spent on infrastructure instead of research
- **Goals:** Quickly provision research environments, easily replicate experimental setups, focus on research rather than infrastructure management

## The Problem

### Complex Cloud Management Without Proper Tooling

Managing ITS Private Cloud resources through web interfaces or raw API calls is inefficient and error-prone. University researchers and IT staff spend hours manually provisioning VMs, configuring networks, and tracking requests, reducing time available for core research and development activities.

**Our Solution:** VSS CLI provides a streamlined command-line interface with intelligent filtering, batch operations, and Infrastructure as Code support to automate and simplify cloud resource management.

### Lack of Infrastructure as Code for Private Cloud

While public cloud providers offer mature IaC solutions, private cloud environments often lack standardized, version-controlled infrastructure provisioning. This creates inconsistencies between environments and makes it difficult to replicate research setups or deployment configurations.

**Our Solution:** VSS CLI specifications enable YAML-based infrastructure definitions that can be versioned, shared, and deployed consistently across environments.

### Limited Contextual Assistance for Cloud Operations

Users often struggle with complex API syntax, resource relationships, and best practices for cloud operations. Existing documentation requires extensive searching and doesn't provide contextual guidance for specific use cases.

**Our Solution:** Integrated AI assistant (UTORcloudy) provides intelligent, context-aware help for cloud operations, answering questions about VM deployment, configuration, and troubleshooting in natural language.

### Asynchronous Operations Without Visibility

Cloud operations like VM provisioning, snapshot creation, and resource modifications are asynchronous, leaving users uncertain about operation status and completion. Manual status checking is tedious and interrupts workflows.

**Our Solution:** Built-in request tracking system with automatic status monitoring provides real-time visibility into long-running operations with spinner feedback and wait-for-completion capabilities.

## Differentiators

### Native Private Cloud Integration

Unlike generic cloud CLI tools that focus on public providers, VSS CLI is purpose-built for ITS Private Cloud with deep integration of university-specific workflows, authentication (including MFA/TOTP), and multi-endpoint support. This results in seamless access to private cloud resources without complex authentication workarounds or API translation layers.

### AI-Powered Contextual Assistance

Unlike traditional CLI documentation approaches, VSS CLI includes an integrated GPT-powered assistant (UTORcloudy) with chain-of-thought reasoning capabilities and session-based authentication. This provides interactive, context-aware guidance directly within the CLI workflow, reducing time spent searching documentation by up to 70%.

### Infrastructure as Code for Private Cloud

Unlike web-based cloud consoles that require manual configuration, VSS CLI provides YAML-based specification files for declarative infrastructure management. This enables version-controlled, reproducible infrastructure deployments that can be integrated into CI/CD pipelines, reducing deployment errors and improving environment consistency.

## Key Features

### Core Features

- **VM Lifecycle Management:** Complete control over virtual machine creation, modification, power operations, and deletion with intuitive command syntax
- **Request System Integration:** Automatic tracking and monitoring of asynchronous cloud operations with status visibility and wait-for-completion capabilities
- **Advanced Filtering & Output:** Powerful JSONPath-based filtering with multiple output formats (JSON, YAML, CSV, table) for integration with automation workflows
- **Infrastructure as Code:** YAML-based VSS CLI specifications for declarative infrastructure provisioning with version control support
- **Multi-Endpoint Support:** Seamless management of multiple cloud endpoints with per-endpoint authentication and configuration profiles

### Security & Authentication Features

- **Multi-Factor Authentication:** Native support for TOTP, SMS, and email MFA methods with secure credential storage
- **JWT Token Management:** Automatic token generation, refresh, and expiration handling with environment variable override support
- **Encrypted Configuration:** Base64-encoded credentials in YAML configuration files with secure file permissions

### Integration & Extensibility Features

- **Plugin Architecture:** Extensible command structure allowing custom plugins for specialized workflows and integrations
- **Model Context Protocol (MCP):** Claude integration enabling AI agents to interact with cloud resources through standardized tool interfaces
- **Storage Integration:** Built-in vskey-stor support for MinIO-based object storage with VPN management for secure access
- **AI Assistant (UTORcloudy):** GPT-powered contextual help with reasoning API support, session management, and interactive feedback collection
- **Batch Operations:** Multi-threaded request processing and parallel VM operations for efficient bulk resource management
