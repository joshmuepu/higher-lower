# Higher-Lower Follower Game

A command-line game where you guess which account has more followers. Enhanced with replay, history display, tie handling, persistent high score, logging, validation, and unit tests.

## Features

- Random distinct account comparisons
- Tie auto-correct advancement
- Round history with optional display
- Persistent high score stored in `.highscore.json`
- Data validation on startup
- Graceful interruption handling (Ctrl+C / Ctrl+D)
- Logging to `game.log` and console
- Unit tests (`unittest`) for core logic and persistence

## Requirements

No external packages required. Uses Python standard library only.

## Running the Game

```bash
python main.py
```

Follow prompts to guess and replay.

## High Score Persistence

High score saved in `.highscore.json` (created automatically). Delete the file to reset.

## Tests

Run all tests:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

## Project Structure

```
main.py            # Game logic & entry point
art.py             # ASCII art assets
game_data.py       # Account data
.tests/            # Unit tests
README.md          # Documentation
requirements.txt   # (Empty of external deps)
```

## Logging

Game events (new high score, warnings) are logged to `game.log`. Adjust verbosity by changing `logging.basicConfig(level=...)` in `main.py`.

## Extending

Ideas:

- Add difficulty levels (limit follower ranges)
- Add command-line arguments (e.g., `--silent-log`)
- Export full session history to JSON
- Add colorized terminal output

Enjoy!
