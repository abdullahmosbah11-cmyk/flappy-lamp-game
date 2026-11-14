# Flappy Lamp

Hihi! This is **Flappy Lamp**.  
So, why a lamp? My name is **Mohamed Abdullah Mosbah**, and *"Mosbah"* in Arabic means **"lamp"**—so that's why I chose the lamp as the main character!

In **Flappy Lamp**, you are trying to avoid obstacles while keeping your lamp lit in the encroaching darkness.

## Game Features
- **Dynamic Lighting:** The player is surrounded by a light source that dims over time; you must collect **Sparks** to illuminate your surroundings and avoid obstacles.
- **Spark Combo:** Collecting multiple sparks in quick succession grants a score combo.
- **Difficulty System:** As you progress, the game speeds up and the gap between obstacles decreases. After the 20th obstacle, the obstacles begin to move vertically.
- **Spark Shop:** You can use collected sparks to purchase and equip various flame skins.

## Gameplay Controls
- **`SPACE`**: Jump / Start Game / Restart
- **`S`**: Open the Spark Shop (from the Start Menu)
- **`1`, `2`, `3`**: Unlock or equip skins (inside the Shop)
- **`M` / `ESC`**: Return to the Start Menu

## How to Play
You can play the game immediately on Windows by downloading the latest `.exe` file from the **[Releases](../../releases)** section.

## Project Structure
```text
flappy-lamp-game/
├── assets/
│   ├── audio/            # Synthesized .wav sound effects (flap, spark, score, crash, zap, buy)
│   └── ...               # Lamp sprites, flame themes, obstacles, and parallax background layers
├── src/
│   ├── assets.py         # PyInstaller-safe resource and sprite loader
│   ├── background.py     # Multi-layer parallax scrolling background
│   ├── lamp.py           # Lamp physics, theme switching, and pixel-perfect collision mask
│   ├── lighting.py       # Dynamic radial darkness and theme-colored light aura
│   ├── obstacles.py      # Stone/iron obstacles, vertical movement, and collectible sparks
│   ├── particles.py      # Theme-colored ember particle system
│   ├── save_manager.py   # Local JSON persistence for high score, sparks, and unlocked skins
│   ├── settings.py       # Game constants, states, and flame theme configurations
│   ├── sound_manager.py  # Low-latency audio playback manager
│   └── ui.py             # Menus, HUD, spark combo counter, and interactive flame shop
├── main.py               # Main game loop and state machine
└── requirements.txt      # Project dependencies (pygame-ce)
