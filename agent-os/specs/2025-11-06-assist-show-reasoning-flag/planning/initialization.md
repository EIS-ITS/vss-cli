# Spec Initialization: Add --show-reasoning Flag to vss assist

## Feature Description
Add a `--show-reasoning` flag to the `vss assist` command to control whether the AI assistant's thought/reasoning process is displayed in the terminal.

## Problem
Currently, when users ask questions to the assistant, the entire thought/reasoning process is shown in the terminal, which can consume the historical buffer and make the terminal difficult to navigate.

## Proposed Solution
- Add a `--show-reasoning` flag (defaults to false if not included)
- When `--show-reasoning` is NOT provided: Display only "Thinking..." as a simple progress indicator
- When `--show-reasoning` IS provided: Display the current thinking process in a smooth fashion (as it currently works)

## Expected Commands
- `vss assist "question"` - Shows only "Thinking..."
- `vss assist --show-reasoning "question"` - Shows full reasoning process

## Initialization Date
2025-11-06

## Spec Path
/Users/josem/src/vsscli-ng/agent-os/specs/2025-11-06-assist-show-reasoning-flag