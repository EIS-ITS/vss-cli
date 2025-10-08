# Product Roadmap

> Last Updated: 2025-10-05
> Version: 1.0.0
> Status: Production (v2025.9.0) - Active Development

## Phase 0: Already Completed ✓

**Current Production Features (v2025.9.0)**

The following features have been implemented and are in production:

### Core Infrastructure Management
- [x] **VM Lifecycle Management** - Complete CRUD operations for virtual machines with power management `XL`
- [x] **Request System** - Asynchronous operation tracking with status monitoring and parallel processing `L`
- [x] **Network Management** - Network configuration, VLAN support, and IP management `L`
- [x] **Storage Management** - Disk provisioning, resizing, and snapshot operations `L`
- [x] **Template Management** - VM deployment from templates with customization `M`
- [x] **Folder Organization** - Logical folder structure for resource organization `S`

### Security & Authentication
- [x] **Multi-Auth Support** - JWT tokens, username/password, MFA/TOTP authentication `M`
- [x] **Multi-Endpoint Support** - Manage multiple cloud endpoints with separate configurations `M`
- [x] **VPN Integration** - Secure access management for vskey-stor operations `M`
- [x] **Credential Encryption** - Base64 encoded credentials in config files `S`

### Advanced Features
- [x] **VSS CLI Specification** - Infrastructure as Code support with YAML specifications `L`
- [x] **AI Assistant (UTORcloudy)** - GPT-powered contextual help with reasoning API `L`
- [x] **MCP Support** - Model Context Protocol server for Claude integration `M`
- [x] **Object Storage (vskey-stor)** - MinIO-based storage integration `M`
- [x] **Advanced Filtering** - Complex filtering with JSONPath expressions `M`
- [x] **Multiple Output Formats** - JSON, YAML, table, CSV, NDJSON support `S`
- [x] **Plugin Architecture** - Extensible command system with dynamic discovery `M`

### Developer Experience
- [x] **Shell Completion** - Bash/ZSH autocompletion support `S`
- [x] **Interactive Shell** - REPL mode for interactive sessions `S`
- [x] **Comprehensive Documentation** - Sphinx-based docs with examples `M`
- [x] **Package Distribution** - PyPI, Homebrew, Docker deployment options `M`
- [x] **Configuration Management** - YAML-based config with environment variable overrides `S`

## Phase 1: VSS CLI Specification Enhancement (Q4 2025)

**Goal:** Enhance the Infrastructure as Code capabilities to make VSS CLI specifications production-ready with comprehensive validation, testing, and deployment workflows.

**Success Criteria:**
- Users can define complete infrastructure environments in YAML specifications
- Specification validation catches errors before deployment
- Documentation covers all specification features with examples
- CI/CD integration guides available for common scenarios

### Features

- [ ] **Enhanced Specification Validation** - Implement comprehensive schema validation for VSS CLI specs with detailed error messages and suggestions `M`
- [ ] **Specification Testing Framework** - Add dry-run and validation modes for testing specifications before deployment `M`
- [ ] **Specification Templates** - Create reusable templates for common infrastructure patterns (web servers, databases, load balancers) `S`
- [ ] **Specification Documentation** - Comprehensive guides and examples for Infrastructure as Code workflows `M`
- [ ] **Diff and Preview** - Show changes before applying specifications to existing infrastructure `L`
- [ ] **Multi-File Specifications** - Support splitting large infrastructures across multiple specification files with imports `M`
- [ ] **Specification Variables** - Add variable substitution and templating support for environment-specific configurations `M`

### Dependencies

- Current VSS CLI specification implementation
- Enhanced error handling and validation library integration
- Documentation framework (Sphinx)

## Phase 2: Testing & Quality Framework (Q1 2026)

**Goal:** Establish comprehensive testing coverage and quality assurance processes to ensure reliability and maintainability of the CLI.

**Success Criteria:**
- Test coverage above 80% for core functionality
- All plugins have integration tests
- Automated testing in CI/CD pipeline
- Performance benchmarks established

### Features

- [ ] **Unit Test Expansion** - Achieve 80%+ coverage for core modules (cli.py, config.py, plugins) `L`
- [ ] **Integration Test Suite** - Add end-to-end tests for common workflows (VM deployment, request tracking, storage operations) `L`
- [ ] **Mock API Framework** - Implement comprehensive mocking for pyvss API calls to enable offline testing `M`
- [ ] **Performance Testing** - Establish benchmarks for CLI operations and identify optimization opportunities `M`
- [ ] **Error Scenario Testing** - Test edge cases, network failures, and error recovery paths `M`
- [ ] **Assistant Integration Tests** - Automated testing for UTORcloudy assistant responses and feedback collection `S`
- [ ] **CI/CD Pipeline Enhancement** - Automated test execution on merge requests with coverage reporting `S`

### Dependencies

- Mock framework for API calls (pytest-mock or responses library)
- CI/CD infrastructure access
- Performance profiling tools

## Phase 3: Async & Performance Optimization (Q2 2026)

**Goal:** Modernize the codebase with async support for improved performance and responsiveness, especially for bulk operations and long-running tasks.

**Success Criteria:**
- Async API calls reduce latency by 50%+ for bulk operations
- Concurrent request handling improves throughput
- Progress reporting for all long-running operations
- Backward compatibility maintained

### Features

- [ ] **Async API Client** - Migrate pyvss integration to async/await pattern using aiohttp `XL`
- [ ] **Concurrent Request Processing** - Implement async batch operations for parallel VM management `L`
- [ ] **Progress Indicators** - Enhanced progress bars and status updates for long-running operations `M`
- [ ] **Caching Layer** - Add intelligent caching for frequently accessed data (templates, folders, networks) `M`
- [ ] **Connection Pooling** - Optimize API connection reuse for better performance `S`
- [ ] **Lazy Loading** - Defer expensive operations until needed for faster command startup `M`
- [ ] **Streaming Output** - Support streaming large result sets for memory efficiency `M`

### Dependencies

- aiohttp library integration
- Rich library for enhanced progress displays
- Caching library (diskcache or aiocache)

## Phase 4: Advanced Features & Integrations (Q3 2026)

**Goal:** Expand CLI capabilities with advanced features that enhance workflow automation and integration with external tools.

**Success Criteria:**
- Users can automate complex multi-step workflows
- Integration with popular DevOps tools (Ansible, Terraform)
- Enhanced MCP capabilities for AI-driven operations
- Plugin marketplace or catalog established

### Features

- [ ] **Workflow Automation** - Define multi-step workflows in YAML with conditional logic and error handling `XL`
- [ ] **Terraform Provider** - Enable Terraform integration for VSS CLI specifications `L`
- [ ] **Ansible Module** - Official Ansible collection for ITS Private Cloud management `L`
- [ ] **Enhanced MCP Tools** - Expand Model Context Protocol capabilities with more granular operations `M`
- [ ] **Plugin Marketplace** - Community plugin registry with discovery and installation support `M`
- [ ] **Webhooks & Events** - Support webhook notifications for request status changes and events `M`
- [ ] **Resource Tagging** - Add comprehensive tagging support for resource organization and cost tracking `S`

### Dependencies

- Terraform SDK for provider development
- Ansible Galaxy for module distribution
- Webhook infrastructure setup
- Plugin repository hosting

## Phase 5: Enterprise & Scale Features (Q4 2026)

**Goal:** Add enterprise-grade features for large-scale deployments, governance, and compliance.

**Success Criteria:**
- Support for multi-tenant environments with RBAC
- Audit logging meets compliance requirements
- Cost reporting and optimization features available
- High availability and disaster recovery workflows supported

### Features

- [ ] **Role-Based Access Control** - Granular permission management for team environments `L`
- [ ] **Audit Logging** - Comprehensive audit trails for all CLI operations with compliance reporting `M`
- [ ] **Cost Management** - Resource cost tracking, budgeting, and optimization recommendations `L`
- [ ] **Resource Quotas** - Enforce limits on resource consumption per user/team/project `M`
- [ ] **Backup & DR Workflows** - Automated backup orchestration and disaster recovery procedures `L`
- [ ] **Multi-Region Support** - Manage resources across multiple data centers with unified interface `M`
- [ ] **Advanced Reporting** - Customizable dashboards and reports for resource utilization and trends `M`
- [ ] **SSO Integration** - Support SAML/OAuth for enterprise authentication `M`

### Dependencies

- Enhanced API endpoints for RBAC and audit features
- Integration with university SSO infrastructure
- Reporting database or analytics platform
- Multi-region API infrastructure

## Future Considerations

### Under Evaluation
- **GUI Companion Tool** - Optional web interface for visual infrastructure management
- **Mobile Companion App** - Basic monitoring and alert management on mobile devices
- **GraphQL API** - Alternative API interface for flexible data queries
- **Resource Dependency Graphs** - Visual representation of infrastructure relationships
- **Smart Recommendations** - ML-based suggestions for resource optimization and cost savings

### Community Requests
- Tracking user feature requests and prioritizing based on community feedback
- Regular survey of user pain points and workflow improvements
- Open contribution guidelines for community plugin development
