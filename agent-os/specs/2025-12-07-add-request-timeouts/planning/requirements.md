# Spec Requirements: Add Request Timeouts

## Initial Description

Add timeout support to HTTP requests in the VSS CLI to prevent indefinite hangs when external services are unresponsive. This includes the main API requests via the `requests` library and external status checks (healthchecks.io, statuspage.io).

## Requirements Discussion

### First Round Questions

**Q1:** What should the timeout value be? Should we use Configuration.timeout (self.timeout from config.py line 73) if set, otherwise fall back to DEFAULT_TIMEOUT?
**Answer:** Yes, use `Configuration.timeout` (self.timeout from config.py line 73) if set, otherwise fall back to `DEFAULT_TIMEOUT` (which is 30 seconds as defined in const.py line 14).

**Q2:** Should streaming requests (like the AI assistant at config.py:1972) have a different timeout handling?
**Answer:** No timeout for streaming requests - avoid timeout entirely for the streaming call at config.py:1972. This makes sense because streaming responses can take varying amounts of time depending on the complexity of the AI response.

**Q3:** Should external status checks (healthchecks.io, statuspage.io) use a different timeout than API calls?
**Answer:** Yes, a shorter timeout (10 seconds) is acceptable for healthchecks.io and statuspage.io. These are non-critical status checks and should fail fast if unresponsive.

**Q4:** Should we add new constants for the timeout values?
**Answer:** No new constants for now - just use existing values. Use `DEFAULT_TIMEOUT` (30 seconds) for main requests and a hardcoded 10 seconds for external status checks.

**Q5:** How should timeout errors be handled? Should we catch requests.exceptions.Timeout and convert to user-friendly error messages?
**Answer:** Yes, catch `requests.exceptions.Timeout` and convert to user-friendly error messages. This will provide clear feedback to users when a request times out.

**Q6:** Are there any exclusions from scope? Retry logic, environment variable configuration?
**Answer:** No exclusions - no retry logic or env variable configuration needed. Keep the implementation simple and focused on adding timeouts.

### Existing Code to Reference

**Similar Features Identified:**
No similar existing features identified for reference. This is a cross-cutting concern that will be applied to existing HTTP request calls.

**Files to Modify:**
- `vss_cli/config.py` - Assistant API requests (lines 1901, 1919, 1972, 2154)
- `vss_cli/hcio.py` - healthchecks.io status check (line 17)
- `vss_cli/sstatus.py` - statuspage.io status checks (lines 25, 49)

### Follow-up Questions

No follow-up questions needed. The user's answers are clear and comprehensive.

## Visual Assets

### Files Provided:
No visual assets provided.

### Visual Insights:
N/A - This is a backend/infrastructure change with no UI components.

## Requirements Summary

### Functional Requirements
- Add timeout parameter to all `requests.get()` and `requests.post()` calls
- Use `Configuration.timeout` if set, otherwise use `DEFAULT_TIMEOUT` (30 seconds) for main API requests
- Use a shorter timeout (10 seconds) for external status checks (healthchecks.io, statuspage.io)
- Exclude streaming requests from timeout (config.py:1972 - AI assistant streaming response)
- Catch `requests.exceptions.Timeout` and convert to user-friendly `VssCliError` messages

### Reusability Opportunities
- The timeout value from `Configuration.timeout` is already part of the configuration system
- `DEFAULT_TIMEOUT` constant already exists in `const.py` (line 14, value: 30)
- `VssCliError` exception class already exists for user-friendly error handling

### Scope Boundaries

**In Scope:**
- Adding `timeout` parameter to `requests.get()` calls in:
  - `vss_cli/hcio.py:17` (healthchecks.io badge check)
  - `vss_cli/sstatus.py:25` (statuspage.io components)
  - `vss_cli/sstatus.py:49` (statuspage.io upcoming maintenance)
- Adding `timeout` parameter to `requests.post()` calls in:
  - `vss_cli/config.py:1901` (generate assistant API key)
  - `vss_cli/config.py:1919` (create chat session)
  - `vss_cli/config.py:2154` (provide assistant feedback)
- Catching `requests.exceptions.Timeout` and raising `VssCliError` with descriptive messages
- NOT adding timeout to streaming request at `config.py:1972`

**Out of Scope:**
- Retry logic for failed requests
- Environment variable configuration for timeouts
- Configuration file options for external status check timeouts
- Any changes to the pyvss library (separate package)
- Modifying the DEFAULT_TIMEOUT constant value

### Technical Considerations
- The `timeout` parameter in requests library accepts either a float (total timeout) or a tuple (connect timeout, read timeout)
- For simplicity, use a single float value for timeout
- The streaming request for AI assistant should not have a timeout since response time varies with query complexity
- External status checks are called from the `vss status` command and should fail gracefully
- Existing exception handling in `hcio.py` and `sstatus.py` catches generic exceptions, so timeout errors will be caught but may need more specific handling

### Error Message Guidelines
- Timeout errors should indicate which service timed out
- Messages should suggest possible causes (network issues, service unavailable)
- Example: "Request to healthchecks.io timed out after 10 seconds. The service may be temporarily unavailable."
