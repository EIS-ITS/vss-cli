# VSS CLI Development Guide

## Development Setup

### Prerequisites
- Python >=3.10
- Git
- [uv](https://docs.astral.sh/uv/) package manager (recommended)

### Environment Setup
```bash
# Clone repository
git clone https://gitlab-ee.eis.utoronto.ca/vss/vss-cli.git
cd vss-cli

# Create virtual environment and install dependencies
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"

# Verify installation
vss-cli --version
```

### Development Dependencies
```toml
[tool.uv.dev-dependencies]
flake8 = "7.1.1"          # Code linting
nose = "1.3.7"            # Testing framework
coverage = "7.6.12"       # Coverage reporting
sphinx = "7.2.2"          # Documentation
sphinx-rtd-theme = "1.3.0"  # Documentation theme
bump2version = "1.0.1"    # Version management
```

## Project Structure

```
vss-cli/
├── vss_cli/                    # Main package
│   ├── cli.py                 # CLI entry point
│   ├── config.py              # Configuration management
│   ├── const.py               # Constants and defaults
│   ├── plugins/               # Plugin system
│   │   ├── compute.py         # Infrastructure management
│   │   ├── request.py         # Request management
│   │   ├── compute_plugins/   # VM-specific operations
│   │   └── request_plugins/   # Request-specific operations
│   ├── data/                  # Static data files
│   │   └── config.yaml        # Default configuration
│   ├── utils/                 # Utility modules
│   └── validators.py          # Input validation
├── tests/                     # Test suite
├── docs/                      # Documentation source
├── pyproject.toml            # Project configuration
├── README.md                 # Project documentation
└── CHANGELOG.md              # Version history
```

## Code Style and Standards

### Python Style
- **Line Length**: 79 characters (Black configuration)
- **String Quotes**: Single quotes preferred (skip-string-normalization)
- **Type Hints**: Required for complex functions
- **Docstrings**: Google style for public functions

### Formatting with Black
```bash
# Format code
black vss_cli/

# Check formatting
black --check vss_cli/
```

### Linting with Flake8
```bash
# Run linting
flake8 vss_cli/

# Configuration in pyproject.toml
[tool.black]
line-length = 79
skip-string-normalization = true
```

### Import Organization
```python
# Standard library imports
import os
import sys
from pathlib import Path

# Third-party imports
import click
import requests

# Local imports
from vss_cli.config import Configuration
from vss_cli.exceptions import VssCliError
```

## Plugin Development

### Creating a New Plugin

1. **Create Plugin File**
```python
# vss_cli/plugins/my_plugin.py
"""My plugin for VSS CLI."""
import click
from vss_cli.cli import pass_context
from vss_cli.config import Configuration

@click.group('my-plugin', short_help='My plugin description')
@pass_context
def cli(ctx: Configuration):
    """Detailed plugin description."""
    with ctx.spinner(disable=ctx.debug) as spinner_cls:
        ctx.load_config(spinner_cls=spinner_cls)

@cli.command('action')
@click.option('--param', help='Parameter description')
@pass_context
def action_command(ctx: Configuration, param: str):
    """Action implementation."""
    try:
        result = ctx.api_operation(param)
        ctx.echo(f"Result: {result}")
    except Exception as e:
        raise VssCliError(f"Operation failed: {e}")
```

2. **Add to Plugin Registry**
Plugin is automatically discovered by filename in `vss_cli/plugins/`

3. **Test Plugin**
```bash
vss-cli my-plugin action --param value
```

### Plugin Best Practices

#### Error Handling
```python
from vss_cli.exceptions import VssCliError

try:
    result = ctx.dangerous_operation()
except VssError as e:
    # Handle API errors
    raise VssCliError(f"API error: {e.message}")
except Exception as e:
    # Handle unexpected errors
    raise VssCliError(f"Unexpected error: {e}")
```

#### Output Formatting
```python
from vss_cli.helper import format_output

# Use standard column definitions
from vss_cli.const import COLUMNS_VM
ctx.echo(format_output(ctx, vms, columns=COLUMNS_VM))

# Custom output columns
custom_columns = [
    ('NAME', 'name'),
    ('STATUS', 'power_state'),
    ('CPU', 'cpu_count')
]
ctx.echo(format_output(ctx, data, columns=custom_columns))
```

#### Async Operations
```python
# Submit operation
result = ctx.create_vm(...)

# Wait for completion if requested
if ctx.wait_for_requests:
    success = ctx.wait_for_request_to(
        result,
        required=['PROCESSED', 'SCHEDULED']
    )
    if not success:
        raise VssCliError("Operation failed")
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
    # Config is already available
    vms = ctx.get_vms()
```

## Testing

### Test Structure
```
tests/
├── test_cli.py               # CLI integration tests
├── test_config.py            # Configuration tests
├── test_plugins/             # Plugin-specific tests
│   ├── test_compute.py
│   └── test_request.py
├── fixtures/                 # Test data
└── utils/                    # Test utilities
```

### Unit Testing
```python
import unittest
from unittest.mock import Mock, patch
from vss_cli.config import Configuration

class TestMyPlugin(unittest.TestCase):

    def setUp(self):
        self.ctx = Mock(spec=Configuration)

    @patch('vss_cli.plugins.my_plugin.api_call')
    def test_my_command(self, mock_api):
        mock_api.return_value = {'status': 'success'}

        result = my_command(self.ctx, param='test')

        self.assertEqual(result['status'], 'success')
        mock_api.assert_called_once_with('test')
```

### Integration Testing
```python
from click.testing import CliRunner
from vss_cli.plugins.compute import cli

class TestComputeIntegration(unittest.TestCase):

    def test_vm_list_command(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['vm', 'ls', '--help'])

        self.assertEqual(result.exit_code, 0)
        self.assertIn('List virtual machine', result.output)
```

### Running Tests
```bash
# Run all tests
python -m nose tests/

# Run specific test file
python -m nose tests/test_config.py

# Run with coverage
coverage run -m nose tests/
coverage report
coverage html  # Generate HTML report
```

### Mock API Responses
```python
@patch('vss_cli.config.Configuration.get_vms')
def test_vm_listing(self, mock_get_vms):
    mock_get_vms.return_value = [
        {
            'moref': 'vm-123',
            'name': 'test-vm',
            'power_state': 'POWERED_ON'
        }
    ]

    result = list_vms_command()
    self.assertIn('test-vm', result)
```

## Documentation

### Code Documentation
```python
def complex_function(param1: str, param2: int) -> dict:
    """Perform complex operation.

    Args:
        param1: String parameter description
        param2: Integer parameter description

    Returns:
        Dictionary with operation results

    Raises:
        VssCliError: When operation fails
    """
    pass
```

### Building Documentation
```bash
# Install documentation dependencies
uv pip install -e ".[dev]"

# Build Sphinx documentation
cd docs/
make html

# View documentation
open _build/html/index.html
```

### Documentation Structure
```
docs/
├── conf.py                   # Sphinx configuration
├── index.rst                 # Main documentation
├── api/                      # API reference
├── user-guide/               # User documentation
└── developer/                # Developer documentation
```

## Version Management

### Calendar Versioning
VSS CLI uses Calendar Versioning (CalVer) format: `YYYY.M.PATCH`

### Version Updates
```bash
# Update version
bump2version patch  # 2025.8.0 -> 2025.8.1
bump2version minor  # 2025.8.1 -> 2025.9.0
bump2version major  # 2025.9.0 -> 2026.1.0

# Manual version update
# Edit vss_cli/const.py
__version__ = "2025.9.0"
```

### Release Process
1. **Update CHANGELOG.md** with new features and fixes
2. **Bump version** using bump2version
3. **Run tests** to ensure quality
4. **Build package** `python -m build`
5. **Create git tag** `git tag v2025.9.0`
6. **Push to repository** `git push --tags`

## Contribution Guidelines

### Development Workflow
1. **Fork repository** or create feature branch
2. **Create virtual environment** and install dev dependencies
3. **Implement changes** following code style guidelines
4. **Add tests** for new functionality
5. **Update documentation** if needed
6. **Run test suite** and ensure all tests pass
7. **Create merge request** with clear description

### Code Review Checklist
- [ ] Code follows style guidelines (Black, Flake8)
- [ ] Tests added for new functionality
- [ ] Documentation updated
- [ ] No breaking changes without version bump
- [ ] Error handling implemented
- [ ] CLI help text updated

### Debugging

#### Debug Mode
```bash
# Enable debug logging
vss-cli --debug compute vm ls

# Show exception details
vss-cli -x compute vm get invalid-id

# Verbose output
vss-cli --verbose compute vm mk from-template
```

#### Development Configuration
```bash
# Use development endpoint
export VSS_ENDPOINT=https://dev-api.example.com
export VSS_TOKEN=dev_token

# Use custom config file
export VSS_CONFIG=/path/to/dev-config.yaml
```

#### API Request Debugging
```python
# Enable requests debugging
from vss_cli.helper import debug_requests_on
debug_requests_on()

# Manual API testing
ctx = Configuration()
ctx.debug = True
ctx.load_config()
response = ctx.get_vms()
```

## Performance Considerations

### Plugin Loading
- Plugins loaded lazily (only when accessed)
- Minimize import time in plugin modules
- Use dynamic imports for optional dependencies

### API Optimization
- Use pagination for large datasets
- Implement proper filtering to reduce data transfer
- Cache configuration data appropriately

### Memory Management
- Stream large responses when possible
- Cleanup temporary files
- Limit concurrent operations based on system resources

This development guide provides comprehensive information for contributing to and extending VSS CLI functionality.