# Task Breakdown: Fix SAST Config Complexity - OVF Parser Refactoring

## Overview
Total Tasks: 14
Target: Reduce cyclomatic complexity of `Configuration.parse_ova_or_ovf()` from 60 (rank F) to under 10 per method (rank A/B)

## Task List

### Module Setup

#### Task Group 1: Create OVF Helper Module Foundation
**Dependencies:** None

- [x] 1.0 Complete module foundation
  - [x] 1.1 Create `vss_cli/ovf_helper.py` with module boilerplate
    - Add module docstring following `vss_cli/helper.py` pattern
    - Add imports: `logging`, `tarfile`, `json`, `pathlib.Path`
    - Add imports: `typing` (Union, Dict, List, Any, Optional)
    - Add import: `xmltodict`
    - Add import: `from vss_cli.exceptions import VssCliError`
    - Add module-level logger: `_LOGGING = logging.getLogger(__name__)`
  - [x] 1.2 Implement `get_namespaced_value(data: Dict, key: str, prefix: str = 'ovf') -> Any`
    - Try `{prefix}:{key}` first, fall back to `key`
    - Handle None/missing values gracefully
    - Return `None` if neither key exists
    - Complexity target: under 5

**Acceptance Criteria:**
- Module file exists at `vss_cli/ovf_helper.py`
- Logger configured correctly
- `get_namespaced_value` abstracts dual-key pattern
- Imports follow codebase conventions

### File Extraction Layer

#### Task Group 2: File Extraction Function
**Dependencies:** Task Group 1

- [x] 2.0 Complete file extraction functionality
  - [x] 2.1 Implement `extract_ovf_content(file_path: Union[Path, str]) -> str`
    - Handle `.ovf` files by reading text directly
    - Handle `.ova`, `.zip`, `.tar` files by extracting OVF member from archive
    - Use `tarfile` module for archive extraction
    - Filter archive members for `.ovf` extension
    - Raise `VssCliError('Invalid OVA/OVF format.')` for invalid formats
    - Return OVF content as string
    - Complexity target: under 10

**Acceptance Criteria:**
- Function handles all four file extensions (.ovf, .ova, .zip, .tar)
- Error messages match existing implementation exactly
- Returns OVF content string ready for parsing

### Section Parsers Layer

#### Task Group 3: Strings and References Parsers
**Dependencies:** Task Group 1

- [x] 3.0 Complete strings and references parsing
  - [x] 3.1 Implement `parse_ovf_strings(ovf_dict: Dict) -> Dict`
    - Extract `Strings`/`ovf:Strings` section using `get_namespaced_value`
    - Iterate over `Msg` elements
    - Build lookup dict mapping `@ovf:msgid` to `#text` values
    - Return empty dict if no strings section exists
    - Complexity target: under 6
  - [x] 3.2 Implement `parse_references(ovf_dict: Dict) -> List[Dict]`
    - Extract `References`/`ovf:References` section
    - Get `File`/`ovf:File` content using `get_namespaced_value`
    - Handle both single dict and list inputs (normalize to list)
    - Extract: `href` from `@ovf:href`, `id` from `@ovf:id`, `size` from `@ovf:size`
    - Return list of file dictionaries
    - Complexity target: under 8

**Acceptance Criteria:**
- Strings lookup dict built correctly for msgid resolution
- References parser handles both dict and list File inputs
- Output structure matches current implementation

#### Task Group 4: Disk and Network Section Parsers
**Dependencies:** Task Group 1

- [x] 4.0 Complete disk and network parsing
  - [x] 4.1 Implement `parse_disk_section(ovf_dict: Dict) -> List[Dict]`
    - Extract `DiskSection`/`ovf:DiskSection` section
    - Get `Disk`/`ovf:Disk` content using `get_namespaced_value`
    - Handle both single dict and list inputs (normalize to list)
    - Extract: `capacity`, `capacityAllocationUnits`, `diskId`, `fileRef`
    - Include debug logging: `_LOGGING.debug(f'Found Disks: {disks_ref}: type: {type(disks_ref)}')`
    - Complexity target: under 8
  - [x] 4.2 Implement `parse_network_section(ovf_dict: Dict) -> List[Dict]`
    - Extract `NetworkSection`/`ovf:NetworkSection` section
    - Get `Network`/`ovf:Network` content using `get_namespaced_value`
    - Handle both single dict and list inputs (normalize to list)
    - Extract: `name` from `@ovf:name`, `description` from `Description`/`ovf:Description`
    - Include debug logging: `_LOGGING.debug(f'Found Networks: {nets}: type: {type(nets)}')`
    - Complexity target: under 8

**Acceptance Criteria:**
- Disk parser extracts all four attributes correctly
- Network parser handles namespace variations for description
- Debug logging matches existing log messages exactly

#### Task Group 5: Deployment Options Parser
**Dependencies:** Task Group 1, Task Group 3 (parse_ovf_strings)

- [x] 5.0 Complete deployment options parsing
  - [x] 5.1 Implement `parse_deployment_options(ovf_dict: Dict, ovf_strings: Dict) -> List[Dict]`
    - Extract `DeploymentOptionSection`/`ovf:DeploymentOptionSection` section
    - Get `Configuration`/`ovf:Configuration` content
    - For each configuration item:
      - Extract `id` from `@ovf:id`
      - Extract `description` from `Description`/`ovf:Description`
      - Extract `label` from `Label`/`ovf:Label`
      - If description/label is dict with `@ovf:msgid`, resolve from `ovf_strings`
    - Return list of deployment option dictionaries
    - Complexity target: under 10

**Acceptance Criteria:**
- Handles both string and dict-based descriptions/labels
- Correctly resolves `@ovf:msgid` references to strings
- Output structure: `[{'id': ..., 'description': ..., 'label': ...}, ...]`

#### Task Group 6: Virtual System Parser
**Dependencies:** Task Group 1

- [x] 6.0 Complete virtual system parsing
  - [x] 6.1 Implement `parse_virtual_system(value: Dict, ovf_strings: Dict) -> Dict`
    - Extract `Name` from `ovf:Name`/`Name`
    - Extract `ProductSection`/`ovf:ProductSection`
    - Handle ProductSection as both list and dict:
      - List: iterate items for Product, Vendor, Property
      - Dict: extract Product, Version from section
    - Extract user-configurable PropertyParams where `@ovf:userConfigurable == 'true'`
    - For each configurable property, extract: `key`, `type`, `description`, `default`
    - Return dict with: Name, Product, Version, Vendor, PropertyParams
    - Complexity target: under 10

**Acceptance Criteria:**
- Handles both list and dict ProductSection formats
- Correctly identifies user-configurable properties
- PropertyParams structure matches current implementation

### Integration Layer

#### Task Group 7: Main Orchestrator and API Integration
**Dependencies:** Task Groups 1-6

- [x] 7.0 Complete main orchestrator and integration
  - [x] 7.1 Implement `parse_ovf(file_path: Union[Path, str]) -> Dict` orchestrator function
    - Call `extract_ovf_content()` to get OVF string
    - Parse with `xmltodict.parse()` and convert to dict via JSON round-trip
    - Add debug logging: `_LOGGING.debug(f'Parsed OVF and found keys: {data_dict.keys()}')`
    - Validate `Envelope`/`ovf:Envelope` exists, raise `VssCliError` if missing
    - Call `parse_ovf_strings()` to build strings lookup
    - Iterate over ovf_dict items and dispatch to appropriate section parsers:
      - `References`/`ovf:References` -> `parse_references()`
      - `DiskSection`/`ovf:DiskSection` -> `parse_disk_section()`
      - `NetworkSection`/`ovf:NetworkSection` -> `parse_network_section()`
      - `DeploymentOptionSection`/`ovf:DeploymentOptionSection` -> `parse_deployment_options()`
      - `VirtualSystem`/`ovf:VirtualSystem` -> `parse_virtual_system()`
    - Assemble and return output dict with keys: Files, Disks, Networks, DeploymentOptionParams, Name, Product, Version, Vendor, PropertyParams
    - Complexity target: under 10
  - [x] 7.2 Update `Configuration.parse_ova_or_ovf()` in `vss_cli/config.py`
    - Add import: `from vss_cli.ovf_helper import parse_ovf`
    - Replace method body with delegation: `return parse_ovf(file_path)`
    - Preserve `@staticmethod` decorator
    - Preserve method signature: `(file_path: Union[Path, str]) -> Dict`
    - Preserve docstring: `"""Parse ova or ovf."""`
  - [x] 7.3 Verify import in `vss_cli/plugins/ovf.py` remains functional
    - Confirm `ctx.parse_ova_or_ovf(file_path)` call still works
    - Confirm `ctx.ovf_dict.get('PropertyParams', [])` returns expected structure
    - Confirm `ctx.ovf_dict.get('DeploymentOptionParams', [])` returns expected structure

**Acceptance Criteria:**
- `Configuration.parse_ova_or_ovf()` remains the public API
- All calls from `vss_cli/plugins/ovf.py` continue to work
- Return value structure is identical to current implementation
- Error messages unchanged

### Validation

#### Task Group 8: Final Validation
**Dependencies:** Task Group 7

- [x] 8.0 Complete validation
  - [x] 8.1 Verify complexity scores
    - Each function in `vss_cli/ovf_helper.py` should have complexity under 10
    - `Configuration.parse_ova_or_ovf()` should have complexity of 1-2 (delegation only)
    - Run complexity analysis tool if available (radon, flake8-cognitive-complexity)
  - [x] 8.2 Verify backward compatibility
    - Test with sample OVF file (if available)
    - Test with sample OVA file (if available)
    - Confirm output structure matches expected keys:
      - `Files`, `Disks`, `Networks`, `DeploymentOptionParams`
      - `Name`, `Product`, `Version`, `Vendor`, `PropertyParams`
  - [x] 8.3 Code quality checks
    - Run `flake8 vss_cli/ovf_helper.py` for linting
    - Verify type hints are consistent with codebase style
    - Verify logging statements match existing patterns

**Acceptance Criteria:**
- All functions have complexity under 10 (rank A/B)
- Original `parse_ova_or_ovf` SAST finding resolved
- No linting errors
- Backward compatibility maintained

## Execution Order

Recommended implementation sequence:

1. **Task Group 1: Module Foundation** - Create module and utility function
2. **Task Group 2: File Extraction** - Implement file reading/extraction
3. **Task Group 3: Strings and References** - Basic section parsers
4. **Task Group 4: Disk and Network** - Additional section parsers
5. **Task Group 5: Deployment Options** - Complex section parser with string resolution
6. **Task Group 6: Virtual System** - Complex section parser with property extraction
7. **Task Group 7: Integration** - Orchestrator and API update
8. **Task Group 8: Validation** - Verify complexity and compatibility

## File Summary

| File | Action |
|------|--------|
| `vss_cli/ovf_helper.py` | Create new (Task Groups 1-7) |
| `vss_cli/config.py` | Modify (Task 7.2 only) |
| `vss_cli/plugins/ovf.py` | Verify only (Task 7.3) |

## Function Summary

| Function | Location | Complexity Target |
|----------|----------|-------------------|
| `get_namespaced_value()` | ovf_helper.py | < 5 |
| `extract_ovf_content()` | ovf_helper.py | < 10 |
| `parse_ovf_strings()` | ovf_helper.py | < 6 |
| `parse_references()` | ovf_helper.py | < 8 |
| `parse_disk_section()` | ovf_helper.py | < 8 |
| `parse_network_section()` | ovf_helper.py | < 8 |
| `parse_deployment_options()` | ovf_helper.py | < 10 |
| `parse_virtual_system()` | ovf_helper.py | < 10 |
| `parse_ovf()` | ovf_helper.py | < 10 |
| `Configuration.parse_ova_or_ovf()` | config.py | 1-2 (delegation) |
