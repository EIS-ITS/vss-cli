# Specification: Onyx Chat Endpoint Migration

## Goal

Update the `ask_assistant()` method to handle the new streaming response format from the Onyx chat API before the February 1st, 2026 deadline while maintaining full backward compatibility with the existing user experience.

## User Stories

- As a CLI user, I want to continue using the `vss assist` command without any changes to my workflow so that the endpoint migration is transparent to me
- As a developer, I want the streaming response handling to work seamlessly with the new response format so that reasoning display, citations, and document references continue functioning correctly

## Specific Requirements

**Endpoint URL and Payload**
- No changes required to endpoint URL (`/api/chat/send-message`)
- No changes required to request payload structure
- A proxy layer handles translation to the new `/api/chat/send-chat-message` endpoint
- A proxy layer handles adding the `stream` parameter automatically

**Streaming Response Format Update**
- The response format has changed from flat structure to nested `placement` object
- Old format: `{"turn_index": 0, "obj": {...}}`
- New format: `{"placement": {"turn_index": 0, "tab_index": 0, "sub_turn_index": null}, "obj": {...}}`
- Update response parsing to check for `'placement' in data` instead of `'turn_index' in data`
- Access turn_index via `data['placement']['turn_index']` instead of `data['turn_index']`

**Streaming Response Handling**
- Continue using `requests.post()` with `stream=True` parameter
- Maintain existing `response.iter_lines()` loop for SSE parsing
- Keep JSON parsing with `json.loads(line)` for each line
- Verify compatibility with new response packet format

**Malicious Prompt Handling**
- Proxy returns `{"message": "..."}` payload when prompt is flagged as potentially malicious
- Example: `{"message": "I'm unable to process that request. Please try rephrasing your question or asking something else."}`
- Display this message to the user using Rich markdown formatting
- Return `(None, api_key)` tuple since no assistant message ID is generated for blocked prompts

**Event Type Handling Verification**
- Verify `reasoning_start`, `reasoning_delta` events work with new endpoint
- Verify `message_start`, `message_delta` events work with new endpoint
- Verify `citation_start`, `citation_delta` events work with new endpoint
- Verify `internal_search_tool_start`, `internal_search_tool_delta` events work with new endpoint
- Verify `section_end` and `stop` events work with new endpoint
- Maintain legacy format handling for `top_documents` and `answer_piece` as fallback

**Message ID Extraction**
- Continue extracting `reserved_assistant_message_id` from initial response packet
- Ensure `assistant_message_id` is correctly captured for feedback submission
- Verify initial packet containing `user_message_id` and `reserved_assistant_message_id` format remains compatible

**User Experience Preservation**
- Maintain `smooth_print()` for streaming text output
- Keep reasoning spinner (`Thinking...`) when `show_reasoning=False`
- Preserve citation and document reference display formatting
- Continue using `clear_console()` and Rich markdown rendering for final output

**Error Handling**
- Maintain existing HTTP status code handling (401, 403, 500, 502, 503, 504)
- Keep debug logging for all response packets
- Preserve existing exception handling patterns

## Visual Design

No visual assets provided - this is a backend API migration with no UI changes.

## Existing Code to Leverage

**`ask_assistant()` method (lines 1782-1967)**
- Core method to be modified with minimal changes
- Contains complete streaming response parsing logic that can be reused
- Event type handlers (`obj_type` switch statements) remain valid
- Document formatting and Rich markdown rendering code unchanged

**`get_new_chat_id()` method (lines 1752-1780)**
- Session creation flow remains completely unchanged
- Returns `chat_session_id` used in the payload
- No modifications required to this method

**`provide_assistant_feedback()` method (lines 1969-2034)**
- Feedback submission endpoint unchanged (`/api/chat/create-chat-feedback`)
- Continues to receive `assistant_message_id` and `api_key` from `ask_assistant()`
- No modifications required to this method

**`_generate_assistant_api_key()` method**
- API key generation logic remains unchanged
- Authentication flow is out of scope
- No modifications required to this method

**Streaming patterns in `requests.post()`**
- Line 1825-1830 shows existing streaming request pattern
- `stream=True` in request parameters continues to be used
- `response.iter_lines()` iteration pattern remains valid

## Out of Scope

- Endpoint URL changes (handled by proxy layer)
- Request payload changes including `stream` parameter (handled by proxy layer)
- Authentication flow changes (API key generation via `_generate_assistant_api_key()`)
- Session creation method changes (`get_new_chat_id()`)
- Feedback endpoint changes (`provide_assistant_feedback()`)
- New optional parameters: `llm_override`, `allowed_tool_ids`, `forced_tool_id`, `file_descriptors`, `search_filters`, `deep_research`
- Non-streaming response mode support
- MCP integration updates (`vss_cli/plugins/mcp.py`)
- Assist plugin interface changes (`vss_cli/plugins/assist.py`)
- Adding `chat_session_info` parameter (session creation remains two-step process)
- Any changes to spinner, rich console, or formatting utilities
