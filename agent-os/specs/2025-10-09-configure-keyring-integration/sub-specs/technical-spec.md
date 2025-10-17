# Technical Specification

This is the technical specification for the spec detailed in @.agent-os/specs/2025-10-09-configure-keyring-integration/spec.md

## Technical Requirements

### 1. Update `configure ls` Command

**File**: `vss_cli/plugins/configure.py` (lines 245-315)

**Changes Required**:

1. **Import credential backend modules** at top of file:
```python
from vss_cli.credentials.base import CredentialType, detect_backend
```

2. **Add backend detection** in `ls()` function after loading config:
```python
backend = detect_backend()
```

3. **Modify credential retrieval logic** (currently lines 258-268):
   - **Current behavior**: Parses base64 `auth` field from config
   - **New behavior**:
     - Try loading from credential backend first
     - Fall back to legacy base64 auth if backend returns None
     - Determine source label based on where credentials came from

4. **Update source column values**:
   - `"KeychainBackend"` - credentials from macOS Keychain
   - `"OnePasswordBackend"` - credentials from 1Password
   - `"EncryptedFileBackend"` - credentials from encrypted fallback
   - `"config file (legacy)"` - credentials from base64 auth field
   - `"env"` - credentials from environment variables (existing)

**Implementation Pattern**:
```python
# For each endpoint:
source = 'config file (legacy)'  # default
user = ''

# Try loading from backend first
if backend.is_available():
    username_value = backend.retrieve_credential(
        endpoint.name, CredentialType.USERNAME
    )
    if username_value:
        user = username_value
        source = backend.__class__.__name__
    else:
        # Fallback to legacy base64 auth
        if endpoint.auth:
            auth_enc = endpoint.auth.encode()
            user, pwd = b64decode(auth_enc).split(b':')
            user = user.decode()
else:
    # Backend unavailable, use legacy
    if endpoint.auth:
        # ... existing base64 parsing ...
```

### 2. Update `configure mk` Command

**File**: `vss_cli/plugins/configure.py` (lines 128-195)

**Current Behavior**:
- Calls `ctx.configure()` which stores credentials with base64 auth in config

**New Behavior**:
- `ctx.configure()` already stores in backend (implemented in config.py:732-831)
- **No changes required** - already integrated via `_create_endpoint_config()`

**Verification**:
- Confirm `ctx.configure()` → `_create_endpoint_config()` flow stores in backend
- Test that new endpoints created with `mk` don't have `auth` field in config
- Verify credentials retrievable via backend after creation

### 3. Backward Compatibility

**Requirements**:
- Endpoints with base64 `auth` field must still display correctly
- `ls` command must handle mixed environments (some endpoints in backend, some in config)
- No breaking changes to existing workflows
- Environment variable credentials (`VSS_*`) continue to work (lines 292-310)

### 4. Error Handling

**Scenarios to Handle**:

1. **Backend unavailable**:
   - `backend.is_available()` returns `False`
   - Fall back to legacy base64 auth gracefully
   - No error messages for normal operation

2. **Credential not found in backend**:
   - `backend.retrieve_credential()` returns `None`
   - Check for legacy auth field
   - Display empty username if both sources fail

3. **Backend retrieval error**:
   - Catch exceptions from backend operations
   - Log debug message
   - Continue with legacy fallback

**Error Handling Pattern**:
```python
try:
    if backend.is_available():
        username_value = backend.retrieve_credential(
            endpoint.name, CredentialType.USERNAME
        )
        # ... use value ...
except Exception as e:
    _LOGGING.debug(f'Could not load from backend: {e}')
    # Fall back to legacy
```

### 5. Testing Requirements

**Unit Tests**:
- Test `ls` with credentials in Keychain backend
- Test `ls` with credentials in encrypted backend
- Test `ls` with legacy base64 auth
- Test `ls` with mixed backends (some endpoints in backend, some in config)
- Test `ls` when backend is unavailable
- Test `mk` creates endpoint without base64 auth field
- Test `mk` stores credentials in detected backend

**Integration Tests**:
- Create endpoint with `mk` → verify with `ls`
- Migrate credentials → verify `ls` shows new backend source
- Mix legacy and new credentials → verify both display correctly

## Implementation Order

1. **Phase 1**: Update `configure ls` command
   - Add backend import
   - Add backend detection
   - Modify credential retrieval logic
   - Update source column display
   - Test with all backend types

2. **Phase 2**: Verify `configure mk` integration
   - Confirm existing `_create_endpoint_config()` integration works
   - Test endpoint creation stores in backend
   - Verify `ls` displays newly created endpoints correctly

3. **Phase 3**: Testing and validation
   - Write unit tests
   - Perform integration testing
   - Test backward compatibility
   - Document behavior changes

## Performance Considerations

- **Caching**: Credential backends already implement 5-minute TTL cache
- **Lazy loading**: Only detect backend when needed (don't pre-load if not used)
- **Efficient retrieval**: Single backend call per endpoint for username
- **No breaking changes**: Maintain fast config file reading for legacy auth

## User Experience Impact

**Before** (legacy):
```
NAME     ENDPOINT              USER      PASS     MFA  TOKEN           SOURCE
vss-api  https://cloud.eis...  jdoe      ******** Yes  Ab12Cd...Yz34  config file
```

**After** (with backend):
```
NAME     ENDPOINT              USER      PASS     MFA  TOKEN           SOURCE
vss-api  https://cloud.eis...  jdoe      ******** Yes  Ab12Cd...Yz34  KeychainBackend
```

**Mixed** (transition):
```
NAME      ENDPOINT              USER      PASS     MFA  TOKEN           SOURCE
vss-api   https://cloud.eis...  jdoe      ******** Yes  Ab12Cd...Yz34  KeychainBackend
vss-dev   https://cloud-dev...  admin     ******** No   Ef56Gh...Wx78  config file (legacy)
```
