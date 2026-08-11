# Tactical Mobile Game

Welcome to the official repository for our tactical mobile game project. This repository contains our core game engine, player controllers, audio management systems, and modular automation tools.

---

## Project Overview

We are building a tactical simulation game optimized for mobile devices, focusing on squad tactical control, smooth touch interactions, and immersive audio-visual feedback.

---

## Project Structure

* **`scripts/player/`**: Contains core player mechanics and controllers:
  * `touch_controller.gd`: Handles touch inputs and mobile gestures.
  * `SquadAIController.cs`: Manages AI decision-making and squad tactical behaviors.
  * `SaveManager.cs`: Handles game state saving and loading.
  * `TacticalAssetManager.cs` & `TacticalAudioManager.cs`: Manage game assets and audio playback.
  * `TacticalHUDView.cs`: Controls the user interface and heads-up display.
* **Core Modules**:
  * `game_engine.py`: Core system simulation and runner.
  * `cache_manager.py`: Manages data caching and state performance.
  * `onboard.py`: Handles player setup and onboarding logic.
* **`audioPool/`**: Stores audio clips, sound effects, and soundscape assets.

---

## Team Workflow & Guidelines

1. **Pull Before Working**: Always run `git pull` before starting new development to ensure you have the latest updates from the team.
2. **Branching**: Create feature-specific branches for new additions rather than pushing directly to `main`.
3. **Clean Commits**: Write clear, descriptive commit messages for your changes.
