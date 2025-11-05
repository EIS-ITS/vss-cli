# Spec Requirements Document

> Spec: Configure Command Keyring Integration
> Created: 2025-10-09

## Overview

Update the `vss-cli configure ls` and `vss-cli configure mk` commands to fully integrate with the secure credential backend system (Keychain, 1Password, encrypted file) implemented in the 2025-10-07-secure-credential-keystore spec. This will provide users with a consistent credential management experience that leverages secure storage backends instead of displaying base64-encoded credentials.

## User Stories

### Configuration Listing with Secure Credentials

As a VSS CLI user, I want to run `vss-cli configure ls` and see my username retrieved from the secure credential backend, so that I can verify my configuration without exposing plaintext credentials in the config file.

**Workflow**: User runs `vss-cli configure ls` → CLI detects credential backend → retrieves username from Keychain/1Password/encrypted storage → displays masked password from backend (not from config file) → shows which backend is storing credentials (e.g., "KeychainBackend", "OnePasswordBackend")

### Endpoint Creation with Backend Storage

As a VSS CLI user, I want to run `vss-cli configure mk` and have my credentials automatically stored in the most secure available backend, so that I don't need to manually migrate credentials later.

**Workflow**: User runs `vss-cli configure mk` → provides username/password → CLI detects best available backend (Keychain → 1Password → Encrypted) → stores credentials in secure backend → creates config entry WITHOUT base64 auth field → confirms storage backend used

### Backend Transparency

As a VSS CLI user, I want to see which credential backend is storing my credentials when I list configurations, so that I can understand where my sensitive data is secured.

**Workflow**: User runs `vss-cli configure ls` → output shows "SOURCE" column indicating backend type (e.g., "KeychainBackend", "EncryptedFileBackend", "config file (legacy)") → user understands migration status at a glance

## Spec Scope

1. **Update `configure ls` command** - Retrieve username from credential backend instead of parsing base64 auth field, display backend source in output
2. **Update `configure mk` command** - Automatically store credentials in detected secure backend during endpoint creation
3. **Backward compatibility** - Handle endpoints with legacy base64 auth gracefully, showing both new and old storage methods
4. **Backend detection display** - Show which credential backend is in use for each endpoint in the listing
5. **Error handling** - Provide clear messages when backend is unavailable or credentials cannot be retrieved

## Out of Scope

- Migration functionality (already implemented in `vss-cli configure migrate-credentials`)
- Support for multiple backends per endpoint (use single auto-detected backend)
- Credential editing/updating commands (will be separate future enhancement)
- Password strength validation or policy enforcement

## Expected Deliverable

1. Running `vss-cli configure ls` shows usernames from credential backends with appropriate source labels
2. Running `vss-cli configure mk` creates new endpoints with credentials stored in secure backends (no base64 auth in config)
3. Backward compatibility maintained - legacy base64 auth credentials still display correctly
