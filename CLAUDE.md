# VSS CLI - ITS Private Cloud Command Line Interface

**CRITICAL**: This CLI manages production cloud infrastructure. Handle credentials securely and validate all destructive operations.

## 🎯 Project Overview

The VSS CLI (vss-cli) is a Python-based command-line interface for managing virtual machines, storage, and services in the University of Toronto's ITS Private Cloud. Built on Click framework with a plugin architecture, it provides comprehensive cloud resource management capabilities.

**Core Purpose**: Simplify interaction with ITS Private Cloud API for VM lifecycle management, resource provisioning, and service operations.

## 🏗️ Architecture

### Entry Points
- **Main CLI**: `vss_cli/cli.py` - Central command dispatcher using Click
- **Scripts**: `vss-cli` and `vss` commands (defined in pyproject.toml)
- **Configuration**: `vss_cli/config.py` - Handles auth, endpoints, and settings

### Plugin System Architecture
```
vss_cli/plugins/
├── compute.py              # VM/infrastructure management
├── request.py              # Request lifecycle management
├── account.py              # User account operations
├── token.py                # Authentication tokens
├── stor.py                 # Storage (vskey-stor) operations
├── assist.py               # AI assistant (UTORcloudy)
├── mcp.py                  # Model Context Protocol server
├── compute_plugins/        # VM-specific operations
│   ├── vm.py              # Virtual machine CRUD
│   ├── template.py        # VM templates
│   ├── net.py             # Network management
│   ├── folder.py          # Logical folders
│   ├── domain.py          # Compute domains
│   └── inventory.py       # Infrastructure inventory
└── request_plugins/        # Request-specific operations
    ├── new.py             # New VM requests
    ├── change.py          # VM modification requests
    ├── snapshot.py        # Snapshot operations
    └── retirement.py      # VM retirement
```

**Plugin Loading**: Dynamic discovery via `VssCli.list_commands()` and `VssCli.get_command()`

### Core Components

#### 1. Configuration System (`vss_cli/config.py`)
- **Multi-endpoint support**: Manages multiple cloud endpoints
- **Credential management**: Username/password, tokens, MFA/TOTP
- **File-based config**: YAML format in `~/.vss-cli/config.yaml`
- **Environment variables**: `VSS_*` prefixed variables override config

#### 2. API Integration (`pyvss` library)
- **REST API client**: Inherits from `pyvss.manager.VssManager`
- **Authentication**: JWT tokens with MFA support
- **Request handling**: Automatic retry, pagination, filtering

#### 3. Output Formatting
- **Formats**: json, yaml, table, auto, ndjson
- **Table customization**: Custom columns, sorting, filtering
- **Column definitions**: Extensive predefined column sets in `const.py`

## 🔧 Key Features

### Virtual Machine Management
```bash
# VM lifecycle
vss compute vm ls                    # List VMs
vss compute vm mk from-template      # Deploy from template
vss compute vm set power-on          # Power operations
vss compute vm rm                    # Delete VM

# Configuration
vss compute vm set cpu               # Modify CPU/memory
vss compute vm set nic               # Network configuration
vss compute vm set disk              # Storage management
```

### Request Management
- **Asynchronous operations**: All changes via request system
- **Status tracking**: `wait_for_request_to()` with status monitoring
- **Multi-request support**: Parallel processing with `WorkerQueue`

### Storage Integration
- **vskey-stor**: MinIO-based object storage
- **VPN access**: Integrated VPN management for secure access

### AI Assistant
- **UTORcloudy**: GPT-powered assistant for cloud operations
- **Reasoning API**: Supports chain-of-thought responses
- **Context-aware**: Understands ITS Private Cloud specifics

### MCP Support
- **Claude integration**: Model Context Protocol server
- **Tool registration**: Exposes CLI functions as Claude tools

## 🔄 Development Workflow

### 1. Plugin Development
Create plugins in `vss_cli/plugins/` following the pattern:
```python
@click.group('plugin-name')
@pass_context
def cli(ctx: Configuration):
    with ctx.spinner(disable=ctx.debug) as spinner_cls:
        ctx.load_config(spinner_cls=spinner_cls)
```

### 2. Testing Approach
```bash
# Install dev dependencies
uv pip install -e ".[dev]"

# Run tests
python -m nose tests/

# Code quality
flake8 vss_cli/
```

### 3. Configuration Management
- **Development**: Use environment variables for testing
- **Production**: YAML configuration files with encrypted credentials

## 🛠️ Technical Patterns

### Error Handling
- **VssCliError**: Custom exceptions for CLI-specific errors
- **API errors**: Wrapped pyvss exceptions with user-friendly messages
- **Validation**: Click parameter validation with custom validators

### Data Processing
- **JSON/YAML input**: Supports file and inline parameter input
- **Column formatting**: JSONPath expressions for nested data access
- **Output customization**: Configurable table formats and column selection

### Async Operations
- **Request polling**: Monitors long-running operations
- **Spinner integration**: Visual feedback during operations
- **Parallel execution**: Multi-threaded request processing

## 📦 Dependencies

### Core Dependencies
- **click**: CLI framework and command structure
- **pyvss**: ITS Private Cloud API client (>=2025.2.1)
- **tabulate**: Table formatting for output
- **ruamel.yaml**: YAML configuration handling
- **jsonpath-ng**: JSONPath for data extraction

### Optional Features
- **stor**: `minio` for storage operations
- **mcp**: `mcp-vss` for Model Context Protocol
- **dev**: Sphinx, coverage, testing tools

## 🚀 Common Operations

### Authentication Setup
```bash
# Configure credentials
vss-cli configure mk

# Use environment variables
export VSS_USER=username
export VSS_USER_PASS=password
# or
export VSS_TOKEN=jwt_token
```

### VM Operations
```bash
# Deploy new VM
vss compute vm mk from-template \
  --source "Ubuntu-22.04" \
  --description "Development server" \
  --custom-spec '{"hostname": "dev01"}'

# Monitor requests
vss request ls -f status=pending
vss request get REQUEST_ID --wait
```

### Bulk Operations
```bash
# List with filters and custom output
vss compute vm ls \
  -f "folder.path=prod" \
  --columns "VM=name,CPU=cpu_count,MEM=memory_gb" \
  --output table
```

## 🔒 Security Considerations

### Credential Management
- **Token encryption**: Base64 encoded credentials in config
- **MFA enforcement**: Supports TOTP, SMS, email methods
- **Environment isolation**: Separate configs per endpoint

### API Security
- **JWT tokens**: Time-limited authentication tokens
- **HTTPS only**: All API communication encrypted
- **Permission model**: Role-based access control

## 📁 Important Files

### Core Files
- `vss_cli/cli.py` - Main CLI entry point and command dispatcher
- `vss_cli/config.py` - Configuration management and API integration
- `vss_cli/const.py` - Constants, defaults, and column definitions
- `pyproject.toml` - Project metadata and dependencies

### Plugin Structure
- `vss_cli/plugins/compute.py` - Compute resource management entry
- `vss_cli/plugins/compute_plugins/vm.py` - VM-specific operations
- `vss_cli/plugins/request.py` - Request lifecycle management
- `vss_cli/plugins/assist.py` - AI assistant integration

### Configuration Templates
- `vss_cli/data/config.yaml` - Default configuration template

## 🎯 Development Guidelines

### Code Style
- **Black formatting**: Line length 79 characters
- **Type hints**: Use typing annotations for complex functions
- **Logging**: Use module-level loggers with appropriate levels

### Plugin Guidelines
- **Inherit context**: Always use `@pass_context` decorator
- **Load config**: Call `ctx.load_config()` in group commands
- **Error handling**: Use `VssCliError` for user-facing errors
- **Async operations**: Use `ctx.wait_for_request_to()` for long operations

### Testing Patterns
- **Mock API calls**: Use test fixtures for pyvss integration
- **Config isolation**: Test with temporary configuration files
- **Output validation**: Test table formatting and JSON output

---

**Version**: 2025.9.0-dev0
**Python**: >=3.10
**Calendar Versioning**: YYYY.M.PATCH format