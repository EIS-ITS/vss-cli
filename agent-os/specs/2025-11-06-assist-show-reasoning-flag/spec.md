# Specification: AI Assistant Reasoning Display Control

## Goal
Add a `--show-reasoning` flag to the `vss assist` command to control whether the AI's thought process is displayed, replacing verbose streaming with a compact "Thinking..." spinner indicator by default to improve terminal readability.

## User Stories
- As a CLI user, I want to see only essential output when asking the assistant questions so that my terminal history remains clean and navigable
- As a power user or developer, I want the option to view the full reasoning process when debugging or understanding how the assistant arrived at its answer

## Specific Requirements

**Add --show-reasoning Boolean Flag**
- Add new Click boolean flag option to assist command following existing pattern from `--no-feedback` and `--no-load`
- Flag presence enables full reasoning display
- Flag absence (default) hides reasoning and shows spinner indicator
- Flag name: `--show-reasoning`
- Default value: False (reasoning hidden by default)

**Implement Spinner Indicator for Hidden Reasoning**
- Display spinner-style "Thinking..." indicator with robot emoji when reasoning is hidden
- Use existing `click_spinner.Spinner` class already imported in config.py
- Reuse robot emoji `ej_ai` already defined in assist.py
- Indicator text format: `"🤖 Thinking..."`
- Spinner must start when `reasoning_start` event is received
- Spinner must automatically stop when `message_start` event is received

**Pass Flag to ask_assistant Method**
- Add `show_reasoning: bool = False` parameter to `ask_assistant()` method signature in config.py
- Pass flag value from assist.py CLI command to ask_assistant() call
- Method should accept flag and control display logic accordingly

**Implement Conditional Reasoning Display Logic**
- When `show_reasoning=False`: Display spinner indicator instead of streaming reasoning text
- When `show_reasoning=True`: Display full reasoning using existing `smooth_print()` method
- Reasoning display decision point: `reasoning_delta` event handler at line 2011-2016 in config.py
- Always accumulate reasoning text in `reasoning_text` variable regardless of display state
- Always log reasoning to debug logs using `_LOGGING.debug()` regardless of display state

**Debug Mode Override**
- When `ctx.debug=True`, automatically display reasoning regardless of `--show-reasoning` flag value
- Check `self.debug` attribute in Configuration class to determine debug state
- Override logic: `if self.debug or show_reasoning: display_reasoning()`
- Ensures developers always see reasoning when debugging

**Spinner Lifecycle Management**
- Create spinner instance when `reasoning_start` event is detected
- Start spinner before first reasoning chunk arrives
- Stop spinner when `message_start` event is detected (reasoning complete)
- Ensure spinner cleanup even if error occurs during streaming
- Reuse existing `spinner_cls` pattern from assist command if available

**Preserve Existing Smooth Streaming**
- When reasoning is shown, maintain exact current behavior with `smooth_print()` method
- No changes to message content streaming (lines 2022-2026)
- No changes to delay or character-by-character printing logic
- No changes to other streaming events (citations, internal search)

**Maintain Debug Logging**
- Always log full reasoning text to debug logs regardless of display state
- Use existing `_LOGGING.debug()` pattern for reasoning text capture
- Log format: `_LOGGING.debug(f"Reasoning: {reasoning_chunk}")`
- Preserve existing debug logging for reasoning_start and message_start events

## Visual Design
Not applicable - CLI flag feature with no visual mockups required.

## Existing Code to Leverage

**Flag Pattern from assist.py (lines 48-51)**
- Reuse Click boolean flag pattern: `@click.option('--show-reasoning', is_flag=True, default=False, help='display AI reasoning process')`
- Follow naming convention of existing flags in assist command
- Position flag option before message argument

**Spinner Usage from assist.py (lines 60, 70-81)**
- Leverage `ctx.spinner(disable=ctx.debug)` context manager pattern
- Reuse spinner start/stop methods: `spinner_cls.stop()` and `spinner_cls.start()`
- Follow pattern of stopping spinner before user interaction and restarting after

**Robot Emoji from assist.py (line 14)**
- Reuse existing `ej_ai = EMOJI_UNICODE.get(':robot_face:')` variable
- Already imported and available in assist.py scope
- Consistent with existing assistant branding

**Reasoning Streaming Handler in config.py (lines 2009-2016)**
- Modify existing `reasoning_delta` event handler to conditionally display
- Keep reasoning text accumulation: `reasoning_text += reasoning_chunk`
- Replace unconditional `self.smooth_print(reasoning_chunk)` with conditional logic
- Add spinner start on `reasoning_start` and stop on `message_start`

**smooth_print Method in config.py (lines 1859-1863)**
- Reuse existing static method for character-by-character printing
- No modifications needed to method itself
- Called conditionally based on flag state

## Out of Scope
- Changes to message content streaming behavior or display
- Modifications to feedback collection mechanism
- Changes to API communication protocol or response structure
- Modifications to smooth_print() implementation internals
- Changes to spinner implementation itself or visual style
- Any changes to citation display or internal search tool display
- Configuration file options for default reasoning display preference
- Per-session or persistent user preference storage
- Changes to debug logging format or verbosity levels
- Modifications to legacy format handling (answer_piece)