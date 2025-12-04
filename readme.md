# Snake Game

A simple Snake game implemented in Python using Pygame, including an optional auto-pilot mode. This project is a small, educational implementation suitable for learning game loops, input handling, and basic object-oriented design.

**Status:** Playable locally (requires Python 3 and `pygame`).

**Features**

- **Classic snake gameplay**: move the snake to eat food and grow.
- **Score display**: current score shown on-screen.
- **Restart on game over**: hit Space to restart after losing.
- **Auto-pilot toggle**: press `A` to toggle the snake's auto-pilot (if available).

**Requirements**

- Python 3.8+ (or the system Python 3) installed.
- `pygame` library.

**Quickstart (macOS / zsh)**

1. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install pygame
```

If `pip install pygame` fails, try installing SDL2 dependencies with Homebrew and retry:

```bash
xcode-select --install
brew install sdl2 sdl2_image sdl2_mixer sdl2_ttf
pip install pygame
```

3. Run the game from the project root:

```bash
python3 driver.py
```

**Controls**

- **Arrow keys**: move the snake (Up / Down / Left / Right).
- **A**: toggle auto-pilot for the snake.
- **Space**: when game is over, hit Space to restart.
- **Close window / Cmd-W**: exit the game.

**Project layout**

- `driver.py` - small entry point that starts the game.
- `game.py` - main game loop, drawing, input handling.
- `snake.py` - snake logic and segment management.
- `food.py` - food object and drawing.
- `score.py` - scoreboard and display logic.
- `segments.py` - snake segment definitions.
- `direction.py` - direction enumeration.
- `drawable.py` - base drawable interface/class.
- `constants.py` - all configuration constants (screen size, colors, FPS).
- `auto_pilot.py` - optional auto-pilot behavior for the snake.

**Troubleshooting**

- If the window doesn't open or Pygame raises errors, ensure a compatible Python and Pygame are installed.
- On macOS, installing Xcode Command Line Tools and SDL2 via Homebrew often resolves build issues for Pygame.
