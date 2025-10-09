# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-10-07-secure-credential-keystore/spec.md

> Created: 2025-10-07
> Version: 1.0.0

## Technical Requirements

### Core Architecture

- **Abstract Credential Backend Interface**: Create a pluggable architecture with an abstract base class `CredentialBackend` that all keystore implementations inherit from
- **Backend Auto-Detection**: Implement platform detection logic to automatically select the appropriate credential backend based on OS and available tools
- **Credential Format**: Store credentials as structured data (username, password, token, MFA secrets, API keys) with metadata (creation date, last access)
- **Namespace Convention**: Use hierarchical naming with `vss-cli` prefix followed by endpoint name (e.g., `vss-cli_vss-api`, `vss-cli_vss-api-dev`)

### macOS Keychain Integration

- **Native Security Framework**: Use Python's `keyring` library with macOS backend.
- **Keychain Item Attributes**: Store credentials as Internet passwords with proper service name, account, and server attributes
- **Access Control**: Request Keychain access permission on first use, handle authorization prompts gracefully
- **Credential Operations**: Implement CRUD operations (create, read, update, delete) for Keychain items
- **Error Handling**: Handle locked Keychain scenarios, missing items, and permission denials with clear user messages

### 1Password Integration

- **Integration Methods**: Support both 1Password CLI (`op`) and 1Password Connect SDK for different deployment scenarios
- **Vault Management**: Allow configuration of specific vault for VSS CLI credentials (default to Private vault)
- **Item Structure**: Create structured items with fields for username, password, token, MFA secret, and custom API keys
- **Authentication Flow**: Handle 1Password session management, biometric unlock, and session timeout
- **Team Sharing**: Support shared vaults for team credential management with proper access controls

### Enhanced Fallback Storage

- **Encryption Layer**: Implement AES-256 encryption using `cryptography` library with key derivation from system-specific entropy
- **Key Management**: Derive encryption key from combination of hardware ID, user ID, and optional user-provided passphrase
- **File Permissions**: Set restrictive file permissions (0600) on encrypted credential files
- **Integrity Checks**: Add HMAC for tamper detection and versioning for backward compatibility
- **Warning System**: Display clear security warnings when using fallback storage, recommend secure alternatives

### Migration System

- **Auto-Detection**: Check for existing base64 credentials in config.yaml on startup
- **Migration Prompt**: Interactive prompt with explanation of security benefits and option to defer
- **Batch Migration**: Migrate all endpoints' credentials in single operation with progress feedback
- **Manual Command**: Provide `vss-cli config migrate-credentials` command for controlled migration
- **Rollback Support**: Keep encrypted backup of original credentials until migration is confirmed successful
- **Validation**: Verify migrated credentials work before removing old storage

### Multi-Endpoint Management

- **Credential Isolation**: Store each endpoint's credentials as separate keystore entries
- **Endpoint Metadata**: Include endpoint URL, description, and last-used timestamp with credentials
- **Quick Switching**: Support credential retrieval by endpoint alias or URL pattern matching
- **Bulk Operations**: Enable export/import of all endpoints for backup or migration purposes

### Performance Optimization

- **Credential Caching**: Implement in-memory caching with configurable TTL (default 15 minutes)
- **Lazy Loading**: Only initialize credential backend when authentication is required
- **Async Operations**: Use async I/O for credential operations where supported
- **Connection Pooling**: Reuse 1Password CLI sessions and Keychain connections

### Security Considerations

- **Memory Protection**: Use secure string handling to prevent credentials from being swapped to disk
- **Audit Logging**: Optional audit log for credential access attempts (success and failure)
- **Credential Rotation**: Support for automated credential rotation reminders
- **Zero-Trust Model**: Never store credentials in plaintext, even temporarily

## Approach

### Implementation Phases

#### Phase 1: Abstract Backend Interface
1. Create `vss_cli/security/credential_backend.py` with abstract base class
2. Define interface methods: `store()`, `retrieve()`, `delete()`, `list_endpoints()`
3. Implement backend detection logic in `vss_cli/security/backend_factory.py`
4. Add configuration schema for backend preferences

#### Phase 2: macOS Keychain Backend
1. Implement `vss_cli/security/backends/keychain.py` using `keyring` library
2. Add fallback to `security` CLI tool for advanced features
3. Create permission handling and user authorization flows
4. Implement error recovery for locked Keychain scenarios

#### Phase 3: 1Password Backend
1. Implement `vss_cli/security/backends/onepassword.py` with dual support (CLI/SDK)
2. Add vault configuration and selection logic
3. Implement session management and biometric unlock support
4. Create team vault sharing capabilities

#### Phase 4: Enhanced Fallback Backend
1. Implement `vss_cli/security/backends/encrypted_file.py` with AES-256 encryption
2. Create key derivation function using system entropy
3. Add HMAC integrity checking and versioning
4. Implement security warning system

#### Phase 5: Migration System
1. Create `vss_cli/security/migrator.py` for credential migration
2. Implement auto-detection of legacy base64 credentials
3. Add interactive migration prompts with user education
4. Create `vss-cli config migrate-credentials` command
5. Implement rollback and validation mechanisms

#### Phase 6: Integration and Testing
1. Update `vss_cli/config.py` to use new credential backends
2. Modify existing authentication flows to leverage keystore
3. Create comprehensive test suite with mocked keystores
4. Add integration tests for each backend type

### Code Structure

```
vss_cli/
├── security/
│   ├── __init__.py
│   ├── credential_backend.py      # Abstract base class
│   ├── backend_factory.py         # Platform detection and backend selection
│   ├── migrator.py                # Credential migration system
│   ├── cache.py                   # In-memory credential caching
│   └── backends/
│       ├── __init__.py
│       ├── keychain.py            # macOS Keychain implementation
│       ├── onepassword.py         # 1Password CLI/SDK implementation
│       └── encrypted_file.py      # Enhanced fallback storage
├── config.py                      # Updated to use credential backends
└── plugins/
    └── configure.py               # Add migrate-credentials command
```

### Configuration Schema Updates

```yaml
# ~/.vss-cli/config.yaml
credential_storage:
  backend: "auto"  # auto, keychain, onepassword, encrypted_file
  cache_ttl: 900   # seconds (15 minutes)
  onepassword:
    vault: "Private"
    use_sdk: false
  encrypted_file:
    require_passphrase: false
  audit_log: false

endpoints:
  vss-api:
    url: https://vss-api.eis.utoronto.ca
    # Credentials now stored in keystore, not in config
    credential_namespace: "vss-cli_vss-api"
```

### Migration Flow

```
1. User runs vss-cli (any command requiring auth)
2. System detects base64 credentials in config.yaml
3. Display migration prompt:
   "Your credentials are currently stored in base64 encoding.
    Would you like to migrate to secure keystore? [Y/n/later]"
4. If yes:
   a. Detect available backend (Keychain, 1Password, or encrypted file)
   b. Display selected backend and security benefits
   c. Migrate all endpoint credentials
   d. Backup original config.yaml
   e. Validate migrated credentials
   f. Update config.yaml to remove base64 credentials
   g. Display success message with rollback instructions
5. If later:
   a. Set "migration_deferred: true" in config
   b. Don't prompt again for 7 days
```

### Error Handling Strategy

- **Keychain Locked**: Prompt user to unlock Keychain, provide retry mechanism
- **1Password Not Authenticated**: Guide user through `op signin` process
- **Missing Backend**: Fall back to next available backend with user notification
- **Credential Not Found**: Provide clear error with setup instructions
- **Migration Failure**: Automatic rollback to original config, preserve backup
- **Permission Denied**: Display platform-specific instructions for granting access

## External Dependencies

### Production Dependencies

- **keyring** (>=23.0.0) - Python library for cross-platform keystore access
  - **Justification:** Provides unified interface to OS-specific credential stores with fallback support
  - **License:** MIT
  - **Installation:** Required dependency in `[project.dependencies]`

- **cryptography** (>=41.0.0) - Modern cryptographic library for Python
  - **Justification:** Required for AES-256 encryption in enhanced fallback storage, FIPS-compliant
  - **License:** Apache 2.0 / BSD
  - **Installation:** Required dependency in `[project.dependencies]`

- **onepassword-sdk** (>=0.1.0) - Official 1Password Python SDK (optional)
  - **Justification:** Provides native Python integration with 1Password Connect for enterprise deployments
  - **License:** MIT
  - **Installation:** Optional dependency in `[project.optional-dependencies]` under `onepassword` group

- **pyobjc-framework-Security** (>=9.0.0) - Python-ObjC bridge for macOS Security framework (macOS only)
  - **Justification:** Direct access to macOS Keychain APIs for advanced features not available in keyring
  - **License:** MIT
  - **Installation:** Optional dependency in `[project.optional-dependencies]` under `keychain` group, macOS only

### Development Dependencies

- **pytest-mock** (>=3.10.0) - Mocking framework for testing credential operations
  - **Justification:** Required to test credential backends without actual keystore access
  - **License:** MIT
  - **Installation:** Development dependency in `[project.optional-dependencies.dev]`

- **fakeredis** (>=2.10.0) - In-memory Redis for testing caching layer
  - **Justification:** Enables testing of credential caching without Redis infrastructure
  - **License:** BSD
  - **Installation:** Development dependency in `[project.optional-dependencies.dev]`

### System Dependencies

- **1Password CLI (`op`)** - Command-line tool for 1Password access (optional)
  - **Justification:** Required for 1Password backend when SDK is not used
  - **Installation:** User-installed via Homebrew (`brew install 1password-cli`) or official installer
  - **Documentation:** https://developer.1password.com/docs/cli

- **macOS Security Framework** - System library for Keychain access (macOS only)
  - **Justification:** Native credential storage on macOS
  - **Installation:** Included with macOS, no installation required
  - **Documentation:** Apple Security Framework documentation

### Dependency Installation Groups

```toml
[project.dependencies]
keyring = ">=23.0.0"
cryptography = ">=41.0.0"

[project.optional-dependencies]
onepassword = [
    "onepassword-sdk>=0.1.0"
]
keychain = [
    "pyobjc-framework-Security>=9.0.0; sys_platform == 'darwin'"
]
dev = [
    "pytest-mock>=3.10.0",
    "fakeredis>=2.10.0"
]
```