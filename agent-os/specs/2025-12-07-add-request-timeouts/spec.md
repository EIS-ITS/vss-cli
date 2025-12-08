# Specification: Add Request Timeouts (Bandit B113 Security Fix)

## Goal
Address Bandit B113 security warnings by adding timeout parameters to all `requests` library HTTP calls, preventing indefinite hangs when external services are unresponsive.

## User Stories
- As a CLI user, I want HTTP requests to fail gracefully with a timeout so that the CLI does not hang indefinitely when services are unavailable
- As a security auditor, I want all HTTP requests to have explicit timeouts so that Bandit B113 security warnings are resolved

## Specific Requirements

**Add timeout to assistant API key generation (config.py:1901)**
- Add `timeout` parameter to `requests.post()` call in `_generate_assistant_api_key()` method
- Use `self.timeout` if set, otherwise fall back to `DEFAULT_TIMEOUT` (30 seconds)
- Wrap call in try/except to catch `requests.exceptions.Timeout`
- Raise `VssCliError` with message: "Request to generate assistant API key timed out. The service may be temporarily unavailable."

**Add timeout to chat session creation (config.py:1919)**
- Add `timeout` parameter to `requests.post()` call in `get_new_chat_id()` method
- Use `self.timeout` if set, otherwise fall back to `DEFAULT_TIMEOUT` (30 seconds)
- Wrap call in try/except to catch `requests.exceptions.Timeout`
- Raise `VssCliError` with message: "Request to create chat session timed out. The service may be temporarily unavailable."

**No timeout for streaming assistant request (config.py:1972)**
- Do NOT add timeout to the streaming `requests.post()` call in `ask_assistant()` method
- Streaming responses have variable duration based on AI response complexity
- This call already uses `stream=True` parameter and processes response iteratively

**Add timeout to feedback submission (config.py:2154)**
- Add `timeout` parameter to `requests.post()` call in `provide_assistant_feedback()` method
- Use `self.timeout` if set, otherwise fall back to `DEFAULT_TIMEOUT` (30 seconds)
- Existing try/except block already catches generic exceptions; add specific handling for `requests.exceptions.Timeout`
- Log warning and return `False` on timeout (consistent with current error handling pattern)

**Add timeout to healthchecks.io status check (hcio.py:17)**
- Add `timeout=10` parameter to `requests.get()` call in `check_status()` function
- Use hardcoded 10-second timeout for external status checks
- Existing try/except block catches generic exceptions; timeout will be logged and status returns "unknown"

**Add timeout to statuspage.io component check (sstatus.py:25)**
- Add `timeout=10` parameter to `requests.get()` call in `get_component()` function
- Use hardcoded 10-second timeout for external status checks
- Wrap call in try/except to catch `requests.exceptions.Timeout` and `requests.exceptions.RequestException`
- Return `None` on timeout to allow graceful degradation

**Add timeout to statuspage.io maintenance check (sstatus.py:49)**
- Add `timeout=10` parameter to `requests.get()` call in `get_upcoming_maintenance_by_service()` function
- Use hardcoded 10-second timeout for external status checks
- Wrap call in try/except to catch `requests.exceptions.Timeout` and `requests.exceptions.RequestException`
- Return empty list on timeout to allow graceful degradation

**Import requests.exceptions where needed**
- Ensure `requests.exceptions.Timeout` is importable in files that need to catch it
- The `requests` library is already imported in all affected files

## Visual Design
No visual assets provided. This is a backend/infrastructure change with no UI components.

## Existing Code to Leverage

**DEFAULT_TIMEOUT constant (const.py:14)**
- Already defined as `DEFAULT_TIMEOUT = 30` (30 seconds)
- Import from `vss_cli.const` in config.py (already imported)
- Use as fallback when `self.timeout` is not set

**Configuration.timeout attribute (config.py:74)**
- Already exists as `self.timeout = None` with type `Optional[int]`
- Can be set via configuration or command line
- Use pattern: `timeout=self.timeout or const.DEFAULT_TIMEOUT`

**VssCliError exception (exceptions.py:5)**
- Already imported in config.py for user-friendly error messages
- Use for timeout errors in assistant API methods
- Provides consistent error handling pattern across CLI

**Existing exception handling in hcio.py**
- Generic `except Exception` block already exists (line 25-26)
- Logs warning and returns "unknown" status
- Timeout errors will be caught by existing handler

**Existing exception handling in sstatus.py**
- No try/except blocks currently exist in `get_component()` or `get_upcoming_maintenance_by_service()`
- Need to add exception handling for timeout and request errors
- Follow pattern from hcio.py for graceful degradation

## Out of Scope
- Retry logic for failed or timed-out requests
- Environment variable configuration for timeout values
- Configuration file options for external status check timeouts
- Changes to the pyvss library (separate package handling core API requests)
- Modifying the DEFAULT_TIMEOUT constant value
- Adding timeout to streaming requests (config.py:1972)
- Custom timeout values per endpoint or request type
- Exponential backoff or circuit breaker patterns
- Timeout configuration in config.yaml template
- Unit tests (will be addressed separately)
