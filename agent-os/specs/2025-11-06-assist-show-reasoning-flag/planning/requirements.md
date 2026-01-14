# Spec Requirements: Add --show-reasoning Flag to vss assist

## Initial Description
Add a `--show-reasoning` flag to the `vss assist` command to control whether the AI assistant's thought/reasoning process is displayed in the terminal.

**Problem:** Currently, when users ask questions to the assistant, the entire thought/reasoning process is shown in the terminal, which can consume the historical buffer and make the terminal difficult to navigate.

**Proposed Solution:** Add a `--show-reasoning` flag (defaults to false if not included). When the flag is NOT provided, display only "Thinking..." as a simple progress indicator. When the flag IS provided, display the current thinking process in a smooth fashion (as it currently works).

**Expected Commands:**
- `vss assist "question"` - Shows only "Thinking..."
- `vss assist --show-reasoning "question"` - Shows full reasoning process

## Requirements Discussion

### First Round Questions

**Q1:** Should the flag be a boolean flag (presence = show reasoning, absence = hide reasoning)?
**Answer:** Yes - boolean flag (presence = show reasoning, absence = hide reasoning)

**Q2:** For the "Thinking..." indicator, should it be:
- A static text message
- A spinner-style indicator (like other CLI operations)
- Include an emoji indicator (like the robot emoji used elsewhere)
**Answer:** A spinner-style indicator (like other CLI operations) AND include an emoji indicator (like the robot emoji used elsewhere)

**Q3:** Should the smooth streaming behavior remain exactly as it currently works when `--show-reasoning` is provided?
**Answer:** Keep the exact smooth streaming behavior as it currently works

**Q4:** Should the "Thinking..." indicator automatically disappear when the actual message content starts streaming?
**Answer:** Automatically disappear when the actual message content starts streaming

**Q5:** Should the scope of this change be limited to reasoning display only, without affecting the message content streaming?
**Answer:** Yes - only affects reasoning display, NOT message content streaming

**Q6:** Should the debug mode (`--debug` flag) automatically show reasoning regardless of the `--show-reasoning` flag?
**Answer:** Yes - when `--debug` is enabled, reasoning should automatically display regardless of the `--show-reasoning` flag

**Q7:** Should debug logs still capture the full reasoning text even when `--show-reasoning` is not provided?
**Answer:** Yes - debug logs should still capture the full reasoning text even when `--show-reasoning` is not provided

**Q8:** Are there any special edge cases to consider (e.g., what happens if reasoning is empty, or if the API doesn't provide reasoning)?
**Answer:** No special edge cases

### Existing Code to Reference

**Similar Features Identified:**
- Flag pattern: `--no-feedback` flag in `vss_cli/plugins/assist.py` (line 51)
- Flag pattern: `--no-load` flag in `vss_cli/plugins/assist.py` (line 48)
- Spinner usage: `ctx.spinner(disable=ctx.debug)` pattern in `vss_cli/plugins/assist.py` (line 60)
- Emoji indicators: Robot emoji usage in `vss_cli/plugins/assist.py` (line 14): `ej_ai = EMOJI_UNICODE.get(':robot_face:')`
- Current reasoning display: `self.smooth_print(reasoning_chunk)` in `vss_cli/config.py` (line 2016)
- Reasoning text accumulation: `reasoning_text += reasoning_chunk` in `vss_cli/config.py` (line 2013)
- Debug logging: `_LOGGING.debug()` pattern used throughout both files

**Backend Logic to Reference:**
- Reasoning streaming handler: Lines 2009-2016 in `vss_cli/config.py`
- Message content streaming handler: Lines 2018-2026 in `vss_cli/config.py`
- Debug mode check: `ctx.debug` boolean available in Configuration context

### Follow-up Questions
No follow-up questions were needed.

## Visual Assets

### Files Provided:
No visual assets provided.

### Visual Insights:
Not applicable - this is a CLI flag feature with no visual UI components.

## Requirements Summary

### Functional Requirements

**Core Functionality:**
- Add a `--show-reasoning` boolean flag to the `vss assist` command
- When flag is NOT present: Display a spinner-style "Thinking..." indicator with emoji during reasoning phase
- When flag IS present: Display full reasoning text in smooth streaming fashion (current behavior)
- Indicator must automatically disappear when actual message content starts streaming
- Message content streaming behavior remains unchanged regardless of flag state

**Debug Mode Integration:**
- When `--debug` flag is active, reasoning should always be displayed regardless of `--show-reasoning` flag
- Debug logs must always capture full reasoning text even when not displayed to user

**Technical Behavior:**
- Flag follows existing boolean flag pattern (`--no-feedback`, `--no-load`)
- Uses existing spinner mechanism with robot emoji indicator
- Preserves current smooth streaming implementation for reasoning display
- Maintains backward compatibility with existing `ask_assistant()` method

### Reusability Opportunities

**Components That Exist:**
- Flag pattern: Reference `--no-feedback` and `--no-load` implementation style
- Spinner mechanism: Reuse `ctx.spinner()` pattern already in assist command
- Emoji indicators: Reuse `ej_ai` (robot emoji) from assist.py
- Smooth printing: Leverage existing `self.smooth_print()` method
- Debug mode checking: Use existing `ctx.debug` boolean

**Backend Patterns to Follow:**
- Reasoning streaming logic at `vss_cli/config.py` lines 2009-2016
- Message content streaming logic at `vss_cli/config.py` lines 2018-2026
- Conditional display pattern based on flag state

### Scope Boundaries

**In Scope:**
- Add `--show-reasoning` flag to assist command
- Implement "Thinking..." spinner indicator with emoji for hidden reasoning mode
- Conditional display of reasoning text based on flag state
- Auto-display reasoning when debug mode is active
- Preserve full reasoning text in debug logs regardless of display state
- Automatic indicator removal when message content starts

**Out of Scope:**
- Changes to message content streaming behavior
- Changes to feedback collection mechanism
- Changes to API communication or response structure
- Changes to smooth printing implementation
- Changes to spinner implementation itself
- Any UI changes beyond reasoning display control

**Future Enhancements Mentioned:**
- None specified

### Technical Considerations

**Integration Points:**
- `vss assist` command in `vss_cli/plugins/assist.py`
- `ask_assistant()` method in `vss_cli/config.py` (will need flag parameter)
- Reasoning streaming handler at line 2016 in `vss_cli/config.py`
- Spinner mechanism already integrated in assist command

**Existing System Constraints:**
- Must maintain smooth streaming behavior when reasoning is shown
- Must not break existing API response handling
- Must preserve debug logging functionality
- Must work with existing emoji system

**Technology Preferences:**
- Use Click framework's boolean flag pattern
- Follow existing spinner usage patterns in codebase
- Maintain consistency with other CLI flags in assist command
- Preserve smooth_print() implementation without modification