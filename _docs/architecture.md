# VSS CLI Architecture

## System Design

VSS CLI follows a modular plugin architecture built on Click framework, designed for extensibility and maintainability.

### Core Architecture Layers

```
┌─────────────────────────────────────┐
│           CLI Entry Point           │
│         (vss_cli/cli.py)           │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│        Configuration Layer          │
│       (vss_cli/config.py)          │
│  • Authentication Management       │
│  • Endpoint Configuration          │
│  • Settings & Preferences          │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│         Plugin System               │
│    Dynamic Loading & Routing       │
│  • VssCli.list_commands()          │
│  • VssCli.get_command()            │
└─────────────────┬───────────────────┘
                  │
┌─────────────────▼───────────────────┐
│          API Integration            │
│       (pyvss.VssManager)           │
│  • REST API Client                 │
│  • Request/Response Handling       │
│  • Authentication & Token Mgmt     │
└─────────────────────────────────────┘
```

### Plugin Loading Mechanism

The CLI uses dynamic plugin discovery through file system scanning:

1. **Discovery**: `VssCli.list_commands()` scans `vss_cli/plugins/` directory
2. **Loading**: `VssCli.get_command()` imports plugins on-demand
3. **Registration**: Plugins register as Click command groups
4. **Sub-plugins**: Nested plugins loaded via `click_plugins.with_plugins()`

### Configuration Architecture

#### Multi-Endpoint Support
```yaml
general:
  default_endpoint_name: "cloud-api"
  output: "auto"
  timeout: 30

endpoints:
  - name: "cloud-api"
    url: "https://cloud-api.eis.utoronto.ca"
    auth: "base64_encoded_credentials"
    token: "jwt_token"
    tf_enabled: true
```

#### Environment Variable Override Hierarchy
1. Command line arguments (highest priority)
2. Environment variables (`VSS_*` prefix)
3. Configuration file
4. Default values (lowest priority)

### API Integration Pattern

VSS CLI extends `pyvss.VssManager` for API interactions:

```python
class Configuration(VssManager):
    def __init__(self):
        super().__init__()
        # CLI-specific extensions
        self.verbose = False
        self.output = "auto"
        # ... other CLI settings
```

**Key Methods**:
- `load_config()`: Initialize authentication and settings
- `get_vm_by_id_or_name()`: Smart VM resolution (moref/uuid/name)
- `wait_for_request_to()`: Async operation monitoring

### Output Formatting System

#### Column Definition Pattern
All output columns defined in `const.py` using JSONPath expressions:

```python
COLUMNS_VM = [
    ("moref",),                    # Direct field access
    ("name", "name.full_name"),    # JSONPath expression
    ("folder.path",),              # Nested field access
    ("power_state",),
    ("ip_address",)
]
```

#### Format Processing Pipeline
1. **Data Retrieval**: API response (JSON)
2. **Column Extraction**: JSONPath evaluation
3. **Format Application**: Table/JSON/YAML rendering
4. **Output**: Formatted string to stdout

### Error Handling Strategy

#### Exception Hierarchy
```
Exception
├── VssCliError (CLI-specific errors)
├── VssError (API errors from pyvss)
└── click.ClickException (Click framework errors)
```

#### Error Propagation
1. **API Errors**: Caught and wrapped with user-friendly messages
2. **Validation Errors**: Click parameter validation with custom validators
3. **Configuration Errors**: Clear guidance for config fixes

### Threading and Concurrency

#### Request Processing
- **Single Request**: `wait_for_request_to()` with spinner
- **Multiple Requests**: `WorkerQueue` for parallel processing
- **Thread Safety**: Configuration shared via Click context

#### Async Operation Pattern
```python
# Submit request
result = ctx.create_vm(...)

# Monitor completion
if ctx.wait_for_requests:
    ctx.wait_for_request_to(result,
                           required=['PROCESSED', 'SCHEDULED'])
```

### Security Architecture

#### Authentication Flow
1. **Credential Input**: CLI args → env vars → config file
2. **Token Generation**: Username/password + MFA → JWT token
3. **Token Persistence**: Encrypted storage in config file
4. **Token Validation**: API whoami check + refresh if needed

#### Multi-Factor Authentication
- **TOTP Support**: Time-based one-time passwords
- **Challenge Flow**: Interactive MFA prompts
- **Enforcement**: Server-side MFA requirement handling

### Extensibility Points

#### Plugin Development
1. **Create Plugin File**: `vss_cli/plugins/my_plugin.py`
2. **Implement CLI Group**: Use `@click.group()` decorator
3. **Add Configuration Loading**: `ctx.load_config()`
4. **Register Sub-commands**: Use Click command decorators

#### Custom Validators
```python
def my_validator(ctx, param, value):
    # Custom validation logic
    return processed_value
```

#### Output Formatters
```python
# Add custom column definitions
COLUMNS_MY_RESOURCE = [
    ("id",),
    ("name",),
    ("custom_field", "nested.custom.field")
]
```

### Performance Considerations

#### Lazy Loading
- **Plugin Loading**: Only import when command accessed
- **API Calls**: Minimize unnecessary requests
- **Configuration**: Load once per command execution

#### Caching Strategy
- **Token Caching**: In-memory during session
- **Config Caching**: File-based with modification time check
- **API Response**: No caching (real-time data required)

#### Pagination Handling
- **Default Limits**: Reasonable page sizes for interactive use
- **Large Datasets**: Support for `--all` flag with progress indication
- **Memory Management**: Stream processing for large responses