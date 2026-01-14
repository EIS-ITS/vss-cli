# Task Breakdown: Onyx Chat Endpoint Migration

## Overview
Total Tasks: 12

This migration updates the `ask_assistant()` method in `vss_cli/config.py` from the deprecated `/api/chat/send-message` endpoint to the new `/api/chat/send-chat-message` endpoint. The migration must be completed before the February 1st, 2026 deadline.

## Task List

### API Layer

#### Task Group 1: Endpoint Migration
**Dependencies:** None

- [x] 1.0 Complete endpoint migration in ask_assistant()
  - [x] 1.1 Write 4-6 focused tests for endpoint migration
    - Test that requests are sent to `/api/chat/send-chat-message` endpoint
    - Test that payload includes `stream: True` parameter
    - Test that existing payload fields (`chat_session_id`, `message`, `parent_message_id`) are preserved
    - Test that streaming response is properly initiated
    - Mock the requests.post() to verify endpoint URL and payload structure
  - [x] 1.2 Update endpoint URL in ask_assistant() method
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Line 1826: Change from `{self.gpt_server}/api/chat/send-message` to `{self.gpt_server}/api/chat/send-chat-message`
    - No changes to base URL or server configuration
  - [x] 1.3 Add explicit stream parameter to payload
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Add `"stream": True` to the payload dictionary (around line 1816-1820)
    - Payload structure becomes: `chat_session_id`, `message`, `parent_message_id`, `stream`
    - Do NOT add any other optional parameters (llm_override, allowed_tool_ids, etc.)
  - [x] 1.4 Ensure endpoint migration tests pass
    - Run ONLY the 4-6 tests written in 1.1
    - Verify endpoint URL is correct
    - Verify payload structure matches new API requirements

**Acceptance Criteria:**
- The 4-6 tests written in 1.1 pass
- Endpoint URL updated to `/api/chat/send-chat-message`
- Payload includes `stream: True` parameter
- Existing payload fields are preserved unchanged

### Streaming Response Layer

#### Task Group 2: Response Handling Verification
**Dependencies:** Task Group 1

- [x] 2.0 Verify and update streaming response handling
  - [x] 2.1 Write 4-6 focused tests for streaming response handling
    - Test initial packet parsing (`user_message_id`, `reserved_assistant_message_id`)
    - Test `reasoning_start` and `reasoning_delta` event handling
    - Test `message_start` and `message_delta` event handling
    - Test `citation_start` and `citation_delta` event handling
    - Test `section_end` and `stop` event handling
    - Test legacy format fallback (`top_documents`, `answer_piece`)
  - [x] 2.2 Verify SSE parsing compatibility with new endpoint
    - Confirm `response.iter_lines()` loop continues to work
    - Verify JSON parsing with `json.loads(line)` handles new format
    - Ensure indexed objects with `turn_index` and `obj` are properly parsed
  - [x] 2.3 Verify event type handlers work with new endpoint
    - Test `reasoning_start`, `reasoning_delta` events
    - Test `message_start`, `message_delta` events
    - Test `citation_start`, `citation_delta` events
    - Test `internal_search_tool_start`, `internal_search_tool_delta` events
    - Maintain legacy format handling as fallback
  - [x] 2.4 Verify message ID extraction from initial response
    - Confirm `reserved_assistant_message_id` is correctly captured
    - Ensure `assistant_message_id` is returned for feedback submission
    - Verify initial packet format compatibility
  - [x] 2.5 Ensure streaming response tests pass
    - Run ONLY the 4-6 tests written in 2.1
    - Verify all event types are handled correctly
    - Confirm backward compatibility with legacy format

**Acceptance Criteria:**
- The 4-6 tests written in 2.1 pass
- All SSE event types are properly parsed
- Message IDs are correctly extracted
- Legacy format fallback continues to work

### Integration Layer

#### Task Group 3: User Experience Verification
**Dependencies:** Task Group 2

- [x] 3.0 Verify user experience preservation
  - [x] 3.1 Write 2-4 focused integration tests for user experience
    - Test smooth_print() continues to display streaming text
    - Test reasoning spinner appears when show_reasoning=False
    - Test citation and document reference display formatting
    - Test clear_console() and Rich markdown rendering for final output
  - [x] 3.2 Verify streaming text output
    - Confirm `smooth_print()` is called for message deltas
    - Confirm `smooth_print()` is called for reasoning when show_reasoning=True
    - Ensure text accumulation works correctly
  - [x] 3.3 Verify reasoning indicator behavior
    - Confirm spinner starts on `reasoning_start` when show_reasoning=False
    - Confirm spinner stops on `message_start`
    - Verify reasoning text is logged to debug
  - [x] 3.4 Verify document and citation formatting
    - Confirm `final_documents` takes precedence over `top_documents`
    - Verify document URLs and titles are formatted correctly
    - Ensure Rich markdown rendering works for final output
  - [x] 3.5 Ensure user experience tests pass
    - Run ONLY the 2-4 tests written in 3.1
    - Verify all user-facing behavior is preserved

**Acceptance Criteria:**
- The 2-4 tests written in 3.1 pass
- Streaming output displays correctly
- Reasoning spinner behavior is preserved
- Document and citation formatting unchanged

### Testing

#### Task Group 4: Error Handling and Final Verification
**Dependencies:** Task Groups 1-3

- [x] 4.0 Verify error handling and complete final testing
  - [x] 4.1 Review tests from Task Groups 1-3
    - Review the 4-6 tests written for endpoint migration (Task 1.1)
    - Review the 4-6 tests written for streaming response (Task 2.1)
    - Review the 2-4 tests written for user experience (Task 3.1)
    - Total existing tests: approximately 10-16 tests
  - [x] 4.2 Write up to 4 additional tests for error handling
    - Test HTTP 401 (unauthorized) error handling
    - Test HTTP 500/502/503/504 (server error) handling
    - Test malformed response handling
    - Test connection timeout/interruption handling
  - [ ] 4.3 Manual integration testing with live endpoint
    - Test basic query: `vss assist "How do I list VMs?"`
    - Test query with reasoning: `vss assist "Explain VM templates" --show-reasoning`
    - Test feedback flow: verify feedback submission works after response
    - Test error scenarios: invalid session, network issues
  - [x] 4.4 Run all feature-specific tests
    - Run ONLY tests related to this migration (tests from 1.1, 2.1, 3.1, and 4.2)
    - Expected total: approximately 14-20 tests maximum
    - Do NOT run the entire application test suite
    - Verify all tests pass

**Acceptance Criteria:**
- All feature-specific tests pass (approximately 14-20 tests total)
- Error handling works correctly for all HTTP status codes
- Manual integration tests pass with live endpoint
- No regression in existing assistant functionality

## Execution Order

Recommended implementation sequence:

1. **API Layer - Endpoint Migration (Task Group 1)**
   - Update endpoint URL and payload structure
   - This is the core change required for the migration

2. **Streaming Response Layer (Task Group 2)**
   - Verify response parsing works with new endpoint
   - Ensure all event types are handled correctly

3. **Integration Layer - User Experience (Task Group 3)**
   - Verify all user-facing behavior is preserved
   - Confirm spinner, streaming, and formatting work

4. **Error Handling and Final Verification (Task Group 4)**
   - Complete error handling verification
   - Run full integration tests

## Files to Modify

| File | Lines | Change Description |
|------|-------|-------------------|
| `/Users/josem/src/vsscli-ng/vss_cli/config.py` | 1826 | Update endpoint URL |
| `/Users/josem/src/vsscli-ng/vss_cli/config.py` | 1816-1820 | Add `stream: True` to payload |

## Files NOT to Modify (Out of Scope)

- `/Users/josem/src/vsscli-ng/vss_cli/config.py` - `get_new_chat_id()` method (lines 1752-1780)
- `/Users/josem/src/vsscli-ng/vss_cli/config.py` - `provide_assistant_feedback()` method (lines 1969-2034)
- `/Users/josem/src/vsscli-ng/vss_cli/config.py` - `_generate_assistant_api_key()` method
- `/Users/josem/src/vsscli-ng/vss_cli/plugins/assist.py` - Plugin interface
- `/Users/josem/src/vsscli-ng/vss_cli/plugins/mcp.py` - MCP integration

## Timeline

- **Migration Deadline:** February 1st, 2026
- **Risk:** The deprecated `/chat/send-message` endpoint will be removed after this date
- **Priority:** High - service disruption if not completed before deadline
