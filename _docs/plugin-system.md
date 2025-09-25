# VSS CLI Plugin System

## Plugin Architecture Overview

The VSS CLI plugin system enables modular command organization through dynamic loading and Click's plugin mechanism.

## Core Plugin Components

### 1. Main Plugin Groups

#### `vss_cli/plugins/compute.py`
**Purpose**: Infrastructure and VM management
**Sub-plugins**: Loaded via `click_plugins.with_plugins()`
```python
@with_plugins(ilm.entry_points(group='vss_cli.contrib.compute'))
@click.group('compute')
```

**Sub-command Structure**:
- `vm` - Virtual machine operations
- `template` - VM template management
- `net` - Network configuration
- `folder` - Logical folder organization
- `domain` - Compute domain management
- `inventory` - Infrastructure inventory

#### `vss_cli/plugins/request.py`
**Purpose**: Request lifecycle management
**Key Operations**: Create, monitor, approve requests

#### `vss_cli/plugins/account.py`
**Purpose**: User account management
**Features**: Profile, MFA, preferences

### 2. Compute Sub-Plugins

#### VM Plugin (`compute_plugins/vm.py`)
**Core Commands**:
```bash
vss compute vm ls                    # List VMs
vss compute vm mk from-template      # Deploy from template
vss compute vm mk from-spec          # Deploy from specification
vss compute vm set power-on          # Power operations
vss compute vm set cpu               # Modify CPU/memory
vss compute vm rm                    # Delete VM
```

**Advanced Features**:
- **Smart VM Resolution**: By moref, UUID, or name
- **Bulk Operations**: Multi-VM commands with parallel processing
- **Template Deployment**: OVF/OVA and template-based provisioning

#### Template Plugin (`compute_plugins/template.py`)
**Template Operations**:
```bash
vss compute template ls              # List templates
vss compute template get             # Template details
vss compute template set             # Modify template properties
```

#### Network Plugin (`compute_plugins/net.py`)
**Network Management**:
```bash
vss compute net ls                   # List networks
vss compute net get                  # Network details
vss compute net set                  # Modify network properties
```

### 3. Request Sub-Plugins

#### New VM Requests (`request_plugins/new.py`)
**VM Provisioning Workflow**:
1. **Specification**: Define VM requirements
2. **Validation**: Check quotas and permissions
3. **Submission**: Create provisioning request
4. **Monitoring**: Track request status

#### Change Requests (`request_plugins/change.py`)
**VM Modification Workflow**:
- CPU/Memory changes
- Storage modifications
- Network configuration updates
- Power state changes

#### Snapshot Management (`request_plugins/snapshot.py`)
**Snapshot Operations**:
```bash
vss request snapshot mk              # Create snapshot
vss request snapshot rm              # Remove snapshot
vss request snapshot revert          # Revert to snapshot
```

## Plugin Development Patterns

### 1. Basic Plugin Structure

```python
"""My plugin for VSS CLI."""
import click
from vss_cli.cli import pass_context
from vss_cli.config import Configuration

@click.group('my-plugin')
@pass_context
def cli(ctx: Configuration):
    """My plugin description."""
    # Load configuration and authenticate
    with ctx.spinner(disable=ctx.debug) as spinner_cls:
        ctx.load_config(spinner_cls=spinner_cls)

@cli.command('sub-command')
@click.option('--param', help='Parameter description')
@pass_context
def sub_command(ctx: Configuration, param: str):
    """Sub-command implementation."""
    result = ctx.some_api_call(param)
    ctx.echo(f"Result: {result}")
```

### 2. Plugin Registration

#### File-based Discovery
- Place plugin in `vss_cli/plugins/`
- File name becomes command name (without `.py`)
- Must expose `cli` function as Click group/command

#### Entry Point Registration
For external plugins via `pyproject.toml`:
```toml
[project.entry-points."vss_cli.contrib.compute"]
my-plugin = "my_package.plugin:cli"
```

### 3. Configuration Integration

#### Context Usage
```python
@pass_context
def my_command(ctx: Configuration, ...):
    # Access API methods
    vms = ctx.get_vms()

    # Use output formatting
    ctx.echo(format_output(ctx, vms, columns=COLUMNS_VM))

    # Handle async operations
    if ctx.wait_for_requests:
        ctx.wait_for_request_to(result)
```

#### Configuration Loading
```python
# In group commands - load config once
@click.group()
@pass_context
def cli(ctx: Configuration):
    with ctx.spinner(disable=ctx.debug) as spinner_cls:
        ctx.load_config(spinner_cls=spinner_cls)

# In leaf commands - config already loaded
@cli.command()
@pass_context
def leaf_command(ctx: Configuration):
    # Config is already loaded from parent group
    pass
```

## Advanced Plugin Features

### 1. Sub-Plugin Loading

For plugins with many sub-commands:

```python
@with_plugins(ilm.entry_points(group='vss_cli.contrib.my_plugin'))
@click.group('my-plugin')
```

Create entry points in separate modules:
```python
# my_plugin_sub.py
@click.command('sub')
def sub_command():
    pass

# Register in pyproject.toml
[project.entry-points."vss_cli.contrib.my_plugin"]
sub = "my_plugin.sub:sub_command"
```

### 2. Shared Utilities

#### Reusable Options (`rel_opts.py`)
```python
# Common options for reuse
filter_opt = click.option(
    '-f', '--filter',
    help='Filter expression'
)

page_opt = click.option(
    '--page-size',
    type=int,
    help='Items per page'
)
```

#### Shared Arguments (`rel_args.py`)
```python
# Common arguments
vm_argument = click.argument('vm_id', shell_complete=vm_completion)
```

#### Helper Functions (`helper.py`)
```python
def process_vm_operation(ctx, vm_id, operation):
    """Common VM operation processing."""
    vm = ctx.get_vm_by_id_or_name(vm_id)
    result = operation(vm)

    if ctx.wait_for_requests:
        ctx.wait_for_request_to(result)

    return result
```

### 3. Custom Validators

```python
from vss_cli.validators import validate_vm_moref

@click.option('--vm', callback=validate_vm_moref)
def command_with_validation(vm):
    pass
```

### 4. Auto-completion

```python
import vss_cli.autocompletion as auto

@click.option('--template', shell_complete=auto.template_completion)
def deploy_command(template):
    pass
```

## Plugin Best Practices

### 1. Error Handling

```python
from vss_cli.exceptions import VssCliError

try:
    result = ctx.api_operation()
except Exception as e:
    raise VssCliError(f"Operation failed: {e}")
```

### 2. Output Formatting

```python
from vss_cli.helper import format_output
from vss_cli.const import COLUMNS_VM

# Use predefined columns
ctx.echo(format_output(ctx, vms, columns=COLUMNS_VM))

# Custom columns
custom_cols = [('NAME', 'name'), ('STATE', 'power_state')]
ctx.echo(format_output(ctx, vms, columns=custom_cols))
```

### 3. Progress Indication

```python
# Short operations
with ctx.spinner(disable=ctx.debug):
    result = ctx.quick_operation()

# Long operations
result = ctx.long_operation()
if ctx.wait_for_requests:
    ctx.wait_for_request_to(result)
```

### 4. Configuration Consistency

```python
# Respect user output preferences
ctx.auto_output('table')  # Default to table for data

# Support common options
@so.filter_opt          # Standard filter option
@so.all_opt            # Show all results option
@so.sort_opt           # Sorting option
```

## Plugin Testing

### 1. Mock Configuration

```python
from unittest.mock import Mock
from vss_cli.config import Configuration

def test_my_command():
    ctx = Mock(spec=Configuration)
    ctx.get_vms.return_value = [...]

    # Test plugin command
    result = my_command(ctx, param='test')
    assert result == expected
```

### 2. Integration Testing

```python
from click.testing import CliRunner
from vss_cli.plugins.my_plugin import cli

def test_cli_integration():
    runner = CliRunner()
    result = runner.invoke(cli, ['sub-command', '--param', 'value'])
    assert result.exit_code == 0
```

## Plugin Discovery Process

1. **Startup**: CLI scans `vss_cli/plugins/` directory
2. **Command Matching**: User input matched to plugin name
3. **Dynamic Import**: Plugin module imported on first access
4. **Click Integration**: Plugin commands added to CLI tree
5. **Execution**: Plugin command executed with context

This lazy loading approach ensures fast CLI startup while supporting extensive functionality.