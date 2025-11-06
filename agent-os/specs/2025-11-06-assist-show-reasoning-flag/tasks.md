# Task Breakdown: AI Assistant Reasoning Display Control

## Overview
Total Tasks: 16 sub-tasks across 4 task groups

## Task List

### CLI Layer

#### Task Group 1: Add --show-reasoning Flag to Assist Command
**Dependencies:** None

- [x] 1.0 Complete CLI flag addition
  - [x] 1.1 Write 2-4 focused tests for flag functionality
    - Test default behavior (flag absent = reasoning hidden)
    - Test explicit behavior (flag present = reasoning shown)
    - Test debug mode override (reasoning shown when --debug is active)
    - Skip exhaustive edge case testing
  - [x] 1.2 Add `--show-reasoning` flag to assist command
    - File: `/Users/josem/src/vsscli-ng/vss_cli/plugins/assist.py`
    - Add after line 51 (after `--no-feedback` flag)
    - Pattern: `@click.option('--show-reasoning', is_flag=True, default=False, help='display AI reasoning process')`
    - Position: Before `@click.argument("message", ...)` decorator
  - [x] 1.3 Update CLI function signature
    - File: `/Users/josem/src/vsscli-ng/vss_cli/plugins/assist.py`
    - Update function signature at line 58
    - Add parameter: `show_reasoning: bool`
    - Order: After `no_feedback` parameter
  - [x] 1.4 Pass flag to ask_assistant method call
    - File: `/Users/josem/src/vsscli-ng/vss_cli/plugins/assist.py`
    - Update call at lines 83-85
    - Add parameter: `show_reasoning=show_reasoning`
    - Maintain existing parameters: `spinner_cls`, `message`, `final_message`
  - [x] 1.5 Ensure CLI layer tests pass
    - Run ONLY the 2-4 tests written in 1.1
    - Verify flag is properly parsed and passed through
    - Do NOT run the entire test suite at this stage

**Acceptance Criteria:**
- The 2-4 tests written in 1.1 pass
- `--show-reasoning` flag is recognized by Click
- Flag value is correctly passed to `ask_assistant()` method
- Flag defaults to False when not provided

### API Integration Layer

#### Task Group 2: Update ask_assistant Method Signature
**Dependencies:** Task Group 1

- [x] 2.0 Complete API method signature update
  - [x] 2.1 Write 2-4 focused tests for ask_assistant parameter handling
    - Test method accepts show_reasoning parameter
    - Test debug mode override logic
    - Test reasoning logging regardless of display state
    - Skip exhaustive API response testing
  - [x] 2.2 Add show_reasoning parameter to ask_assistant method
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Update method signature at line 1931
    - Add parameter: `show_reasoning: bool = False`
    - Position: After `final_message` parameter
  - [x] 2.3 Pass show_reasoning to get_new_chat_id method
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Method already has `show_reasoning` parameter at line 1915
    - Ensure parameter is passed when `get_new_chat_id` is called
    - Maintain backward compatibility
  - [x] 2.4 Ensure API layer tests pass
    - Run ONLY the 2-4 tests written in 2.1
    - Verify parameter is correctly accepted
    - Do NOT run the entire test suite at this stage

**Acceptance Criteria:**
- The 2-4 tests written in 2.1 pass
- Method signature includes `show_reasoning` parameter with default value False
- Parameter is properly passed to downstream methods
- No breaking changes to existing API calls

### Reasoning Display Logic

#### Task Group 3: Implement Conditional Reasoning Display
**Dependencies:** Task Group 2

- [x] 3.0 Complete reasoning display implementation
  - [x] 3.1 Write 3-6 focused tests for reasoning display logic
    - Test spinner shows when reasoning is hidden
    - Test reasoning streams when flag is true
    - Test debug mode forces reasoning display
    - Test reasoning text is logged in all cases
    - Test spinner lifecycle (start/stop)
    - Skip exhaustive streaming edge case tests
  - [x] 3.2 Import robot emoji in config.py
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Add import near other emoji imports (if not already present)
    - Import: `from vss_cli.utils.emoji import EMOJI_UNICODE`
    - Define: `ej_ai = EMOJI_UNICODE.get(':robot_face:')`
  - [x] 3.3 Create spinner instance for reasoning indicator
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Initialize in `ask_assistant` method after line 1939
    - Create variable: `reasoning_spinner = None`
    - Store show_reasoning flag and debug state for conditional logic
  - [x] 3.4 Modify reasoning_start event handler
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Location: Around line 2010
    - Add spinner initialization when `show_reasoning=False` and `debug=False`
    - Spinner text: `f"{ej_ai} Thinking..."`
    - Start spinner if not showing reasoning
  - [x] 3.5 Modify reasoning_delta event handler
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Location: Lines 2011-2016
    - Keep reasoning accumulation: `reasoning_text += reasoning_chunk`
    - Add debug logging: `_LOGGING.debug(f"Reasoning: {reasoning_chunk}")`
    - Add conditional display logic:
      ```python
      # Display reasoning if flag is true OR debug mode is active
      if self.debug or show_reasoning:
          self.smooth_print(reasoning_chunk)
      ```
    - Remove unconditional `self.smooth_print(reasoning_chunk)` at line 2016
  - [x] 3.6 Modify message_start event handler
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Location: Around line 2018
    - Stop and clean up reasoning spinner if it exists
    - Add spinner cleanup before message content display
    - Code pattern: `if reasoning_spinner: reasoning_spinner.stop()`
  - [x] 3.7 Add debug mode override check
    - File: `/Users/josem/src/vsscli-ng/vss_cli/config.py`
    - Verify `self.debug` attribute is accessible
    - Ensure debug mode forces reasoning display regardless of flag
    - Logic: `if self.debug or show_reasoning:`
  - [x] 3.8 Ensure reasoning display tests pass
    - Run ONLY the 3-6 tests written in 3.1
    - Verify spinner shows/hides correctly
    - Verify reasoning displays when appropriate
    - Verify debug logging works in all cases
    - Do NOT run the entire test suite at this stage

**Acceptance Criteria:**
- The 3-6 tests written in 3.1 pass
- Spinner displays when reasoning is hidden (default behavior)
- Reasoning streams when `--show-reasoning` flag is present
- Debug mode overrides flag and always shows reasoning
- Debug logs capture full reasoning text in all cases
- Spinner automatically stops when message content starts
- No changes to message content streaming behavior

### Testing & Integration

#### Task Group 4: Test Review & Integration Verification
**Dependencies:** Task Groups 1-3

- [x] 4.0 Review existing tests and verify integration
  - [x] 4.1 Review tests from Task Groups 1-3
    - Review the 2-4 tests from CLI layer (Task 1.1)
    - Review the 2-4 tests from API layer (Task 2.1)
    - Review the 3-6 tests from reasoning display layer (Task 3.1)
    - Total existing tests: approximately 7-14 tests
  - [x] 4.2 Analyze test coverage gaps for this feature
    - Identify critical user workflows that lack test coverage
    - Focus on end-to-end scenarios: CLI -> API -> Display
    - Prioritize integration between flag, debug mode, and display logic
    - Do NOT assess entire application test coverage
  - [x] 4.3 Write up to 5 additional integration tests maximum
    - Test complete workflow: flag passed from CLI through to display
    - Test debug mode override in complete workflow
    - Test spinner lifecycle in real streaming scenario
    - Test backward compatibility (no flag provided)
    - Test feedback collection still works with new flag
    - Do NOT write comprehensive coverage for all edge cases
  - [x] 4.4 Run feature-specific tests only
    - Run ONLY tests related to this feature (tests from 1.1, 2.1, 3.1, and 4.3)
    - Expected total: approximately 12-19 tests maximum
    - Do NOT run the entire application test suite
    - Verify all critical workflows pass
  - [x] 4.5 Manual testing verification
    - Test command: `vss assist "test question"` (default, reasoning hidden)
    - Test command: `vss assist --show-reasoning "test question"` (reasoning shown)
    - Test command: `vss --debug assist "test question"` (debug override)
    - Test command: `vss assist --show-reasoning --no-feedback "test"` (multiple flags)
    - Verify emoji spinner appears correctly
    - Verify smooth streaming works when reasoning is shown
    - Verify feedback collection still works

**Acceptance Criteria:**
- All feature-specific tests pass (approximately 12-19 tests total)
- No more than 5 additional tests added for integration gaps
- Manual testing confirms expected behavior in all scenarios
- Backward compatibility maintained (existing commands work unchanged)
- No regression in feedback collection or other assist features

## Execution Order

Recommended implementation sequence:
1. CLI Layer (Task Group 1) - Add flag to assist command
2. API Integration Layer (Task Group 2) - Update method signatures
3. Reasoning Display Logic (Task Group 3) - Implement conditional display and spinner
4. Testing & Integration (Task Group 4) - Verify end-to-end functionality

## Key Implementation Notes

### File Locations
- **CLI flag**: `/Users/josem/src/vsscli-ng/vss_cli/plugins/assist.py` (lines 46-58)
- **API method**: `/Users/josem/src/vsscli-ng/vss_cli/config.py` (line 1931)
- **Reasoning handlers**: `/Users/josem/src/vsscli-ng/vss_cli/config.py` (lines 2009-2026)

### Existing Patterns to Reuse
- **Flag pattern**: `--no-feedback` and `--no-load` flags (assist.py lines 48-51)
- **Spinner pattern**: `ctx.spinner(disable=ctx.debug)` (assist.py line 60)
- **Robot emoji**: `ej_ai = EMOJI_UNICODE.get(':robot_face:')` (assist.py line 14)
- **Smooth print**: `self.smooth_print(reasoning_chunk)` (config.py line 2016)

### Critical Behaviors to Preserve
- **Message streaming**: No changes to message_delta handler (lines 2022-2026)
- **Feedback collection**: No changes to feedback mechanism (assist.py lines 87-156)
- **Debug logging**: Always log reasoning text regardless of display state
- **Citations and search**: No changes to citation_delta or internal_search handlers
