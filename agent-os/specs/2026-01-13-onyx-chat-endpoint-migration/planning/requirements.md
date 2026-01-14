# Spec Requirements: Onyx Chat Endpoint Migration

## Initial Description

Migrate the Onyx Widget from the deprecated `/chat/send-message` endpoint to the new `/chat/send-chat-message` endpoint based on the Onyx documentation at https://docs.onyx.app/developers/guides/chat_new_guide

Specifically lines 1825 to 1937 in `vss_cli/config.py`.

## Requirements Discussion

### First Round Questions

**Q1:** User Experience - Should the user experience remain the same (streaming output, reasoning display, citations, and document references)?
**Answer:** Keep same user experience - maintain backward compatibility with streaming output, reasoning display, citations, and document references.

**Q2:** Authentication - Is the authentication flow (API key generation, session creation) changing or should it remain as-is?
**Answer:** OUT OF SCOPE. Just focus on the /chat/send-message endpoint to the new /chat/send-chat-message endpoint migration.

**Q3:** New Parameters - The new endpoint supports additional optional parameters (llm_override, allowed_tool_ids, forced_tool_id, file_descriptors, search_filters, deep_research). Should any of these be exposed to users or kept at defaults?
**Answer:** Use simplified approach. Do NOT expose new optional parameters (llm_override, allowed_tool_ids, forced_tool_id, file_descriptors, search_filters, deep_research) in this migration.

**Q4:** Response Mode - Should the implementation continue using streaming mode or support both streaming and non-streaming?
**Answer:** Continue using streaming mode.

**Q5:** Session Creation - The current implementation uses a two-step process (get_new_chat_id then send-message). The new API allows combining these with chat_session_info. Should we maintain backward compatibility or simplify?
**Answer:** Maintain backward compatibility with the existing session creation approach (keep the two-step process with get_new_chat_id then send-message).

**Q6:** Feedback Endpoint - The feedback endpoint (/api/chat/create-chat-feedback) should remain unchanged?
**Answer:** Should remain unchanged (/api/chat/create-chat-feedback).

**Q7:** Migration Deadline - The documentation states migration deadline of February 1st, 2026. Is this a priority?
**Answer:** Yes, migration deadline of February 1st, 2026 should be prioritized.

**Q8:** Scope - What should be excluded from this migration?
**Answer:** Focused ONLY on /chat/send-message to /chat/send-chat-message endpoint migration. Exclude MCP integration, assist.py plugin interface changes.

### Existing Code to Reference

**Primary Implementation File:**
- File: `vss_cli/config.py` - Lines 1825-1937 (ask_assistant method)
- Current endpoint: `/api/chat/send-message`
- New endpoint: `/api/chat/send-chat-message`

**Related Methods in config.py:**
- `get_new_chat_id()` - Lines 1752-1780 (session creation - remains unchanged)
- `provide_assistant_feedback()` - Lines 1969-2034 (feedback submission - remains unchanged)
- `_generate_assistant_api_key()` - API key generation (remains unchanged)

**Supporting Plugin:**
- File: `vss_cli/plugins/assist.py` - OUT OF SCOPE (no interface changes)

### Follow-up Questions

No follow-up questions were necessary.

## Visual Assets

### Files Provided:
No visual assets provided.

### Visual Insights:
N/A

## Requirements Summary

### Functional Requirements

- Migrate from deprecated `/api/chat/send-message` to `/api/chat/send-chat-message` endpoint
- Maintain streaming response handling for real-time output
- Preserve current user experience including:
  - Streaming text output with smooth_print()
  - Reasoning display with optional visibility toggle
  - Citation handling and display
  - Document reference collection and formatting
  - Spinner indicators during reasoning phase
- Continue using existing session creation flow (two-step process)
- Maintain backward compatibility with current response parsing:
  - `MESSAGE_DELTA` / `message_delta` handling
  - `REASONING_DELTA` / `reasoning_delta` handling
  - `CITATION_INFO` / `citation_delta` handling
  - `SEARCH_TOOL_START` / `internal_search_tool_start` handling
- Return assistant_message_id and api_key for feedback submission

### Technical Considerations

**Current Payload Structure (to be migrated from):**
```python
payload = {
    "chat_session_id": chat_id,
    "message": message,
    "parent_message_id": None,
}
```

**New Payload Structure (to migrate to):**
```python
payload = {
    "chat_session_id": chat_id,
    "message": message,
    "parent_message_id": None,
    "stream": True,  # Explicit streaming flag
    # New optional parameters NOT to be exposed:
    # "llm_override": None,
    # "allowed_tool_ids": None,
    # "forced_tool_id": None,
    # "file_descriptors": None,
    # "search_filters": None,
    # "deep_research": None,
}
```

**Endpoint Change:**
- Current: `{self.gpt_server}/api/chat/send-message`
- New: `{self.gpt_server}/api/chat/send-chat-message`

**Response Format Considerations:**
- The new API returns Server-Sent Events packets with types including:
  - `MESSAGE_DELTA` - Content chunks
  - `REASONING_DELTA` - Reasoning text
  - `CITATION_INFO` - Citation data
  - `SEARCH_TOOL_START` - Search tool activation
- Current implementation handles similar event types; verify compatibility with new response format
- May need to handle both old and new event type naming conventions during transition

### Reusability Opportunities

- Existing streaming response parsing logic can be adapted
- Current event type handlers (reasoning_delta, message_delta, citation_delta) may work with minor adjustments
- Session creation (`get_new_chat_id`) remains unchanged
- Feedback submission (`provide_assistant_feedback`) remains unchanged
- API key generation (`_generate_assistant_api_key`) remains unchanged

### Scope Boundaries

**In Scope:**
- Migrate `ask_assistant()` method from `/chat/send-message` to `/chat/send-chat-message`
- Update request payload to match new API requirements
- Ensure streaming response parsing works with new endpoint
- Maintain all current user-facing behavior
- Add explicit `stream: True` parameter to payload

**Out of Scope:**
- Authentication flow changes (API key generation, session creation)
- New optional parameters (llm_override, allowed_tool_ids, forced_tool_id, file_descriptors, search_filters, deep_research)
- MCP integration updates
- `assist.py` plugin interface changes
- Feedback endpoint changes
- Non-streaming response mode
- Session creation method changes (`get_new_chat_id`)

### Timeline Constraints

- **Migration Deadline:** February 1st, 2026
- The deprecated `/chat/send-message` endpoint will be removed after this date
- Prioritize completion before deadline to avoid service disruption

### Testing Considerations

- Verify streaming response parsing works correctly with new endpoint
- Test reasoning display (both shown and hidden modes)
- Validate citation and document reference handling
- Confirm spinner behavior during reasoning phase
- Test error handling for various HTTP status codes
- Verify backward compatibility with existing user workflows
