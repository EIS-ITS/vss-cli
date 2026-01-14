# Specification: Fix SAST Config Complexity - OVF Parser Refactoring

## Goal
Reduce the cyclomatic complexity of `Configuration.parse_ova_or_ovf()` from 60 (rank F) to under 10 per method (rank A/B) by extracting parsing logic into a dedicated `vss_cli/ovf_helper.py` module while maintaining 100% backward compatibility.

## User Stories
- As a developer, I want the OVF parsing code to be modular and maintainable so that future enhancements and bug fixes are easier to implement
- As a security engineer, I want the codebase to pass SAST scans with acceptable complexity scores so that critical security findings are resolved

## Specific Requirements

**Create New Module `vss_cli/ovf_helper.py`**
- Module should contain all OVF/OVA parsing logic extracted from `Configuration.parse_ova_or_ovf()`
- Follow existing helper module patterns (e.g., `vss_cli/helper.py`) for consistency
- Include module-level logger `_LOGGING = logging.getLogger(__name__)`
- Use type hints consistent with codebase style (Union, Dict, List, Optional from typing)
- Import dependencies: `tarfile`, `xmltodict`, `json`, `pathlib.Path`, `logging`

**Namespace Utility Function**
- Create `get_namespaced_value(data: Dict, key: str, prefix: str = 'ovf') -> Any` utility
- Abstracts the dual-key pattern: tries `prefix:key` first, falls back to `key`
- Should handle None/missing values gracefully
- Reduces repetitive conditional logic throughout parsing code

**File Extraction Function**
- Create `extract_ovf_content(file_path: Union[Path, str]) -> str`
- Handles `.ovf` files by reading text directly
- Handles `.ova`, `.zip`, `.tar` files by extracting OVF member from archive
- Raises `VssCliError` for invalid formats
- Complexity target: under 10

**References Section Parser**
- Create `parse_references(ovf_dict: Dict) -> List[Dict]`
- Extracts file references with href, id, size attributes
- Handles both single dict and list inputs for `File`/`ovf:File`
- Returns list of file dictionaries

**Disk Section Parser**
- Create `parse_disk_section(ovf_dict: Dict) -> List[Dict]`
- Extracts disk information: capacity, capacityAllocationUnits, diskId, fileRef
- Handles both single dict and list inputs for `Disk`/`ovf:Disk`
- Include debug logging for found disks

**Network Section Parser**
- Create `parse_network_section(ovf_dict: Dict) -> List[Dict]`
- Extracts network information: name, description
- Handles both single dict and list inputs for `Network`/`ovf:Network`
- Include debug logging for found networks

**Deployment Option Section Parser**
- Create `parse_deployment_options(ovf_dict: Dict, ovf_strings: Dict) -> List[Dict]`
- Extracts deployment configuration parameters: id, description, label
- Handles `@ovf:msgid` references to `ovf_strings` lookup table
- Supports both dict-based and string-based descriptions/labels

**Virtual System Parser**
- Create `parse_virtual_system(value: Dict, ovf_strings: Dict) -> Dict`
- Extracts Name, Product, Version, Vendor information
- Handles `ProductSection`/`ovf:ProductSection` (both list and dict forms)
- Extracts user-configurable PropertyParams where `@ovf:userConfigurable == 'true'`

**Strings Section Parser**
- Create `parse_ovf_strings(ovf_dict: Dict) -> Dict`
- Extracts Msg elements from `Strings`/`ovf:Strings` section
- Builds lookup dictionary mapping `@ovf:msgid` to `#text` values
- Used by deployment options and virtual system parsers

**Public API Preservation**
- `Configuration.parse_ova_or_ovf()` must remain as the public static method
- Method signature unchanged: `(file_path: Union[Path, str]) -> Dict`
- Internally delegates to new `ovf_helper` module functions
- Return value structure must be identical to current implementation

## Visual Design
No visual assets provided - this is a code refactoring task with no visual components.

## Existing Code to Leverage

**`vss_cli/helper.py` - Module Pattern**
- Use same logging setup pattern with `_LOGGING = logging.getLogger(__name__)`
- Follow same import style and type hint conventions
- Reference for creating standalone helper modules in this codebase

**`vss_cli/plugins/ovf.py` - OVF Plugin Consumer**
- Primary consumer of `Configuration.parse_ova_or_ovf()`
- Accesses returned dict keys: `PropertyParams`, `DeploymentOptionParams`
- Validates return structure must include these keys when data exists

**`vss_cli/config.py` - Current Implementation (lines 1520-1692)**
- Source function to refactor at `Configuration.parse_ova_or_ovf()`
- Uses `VssCliError` for error handling - import from `vss_cli.exceptions`
- Existing debug logging patterns should be preserved in new module

**`vss_cli/exceptions.py` - Error Handling**
- Import `VssCliError` for raising parsing errors
- Maintain same error messages for backward compatibility

**`vss_cli/utils/` - Utils Pattern**
- Alternative location consideration, but `vss_cli/ovf_helper.py` at root level is preferred per requirements

## Out of Scope
- Changing the public API signature of `Configuration.parse_ova_or_ovf()`
- Adding unit tests (no existing tests; tests not requested in this spec)
- Fixing unreported bugs in OVF parsing logic
- Modifying logging output format or log levels beyond extraction needs
- Performance optimizations beyond natural refactoring improvements
- Adding new OVF parsing features or supporting additional OVF versions
- Modifying the `vss_cli/plugins/ovf.py` plugin beyond any necessary import changes
- Creating documentation files for the new module
- Changing error messages or exception types
- Supporting additional archive formats beyond .ova, .ovf, .zip, .tar
