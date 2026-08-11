# 🦅 Tactical Mobile Simulation (TMS) Engine

[![Build Status](https://github.com/Gpowerluv/tactical-mobile-game/actions/workflows/ci.yml/badge.svg)](https://github.com/Gpowerluv/tactical-mobile-game/actions)
[![Engine](https://img.shields.io/badge/Godot-4.x-blue.svg)](https://godotengine.org/)
[![Logic](https://img.shields.io/badge/Python-3.10-yellow.svg)](https://python.org)
[![Operational Status](https://img.shields.io/badge/Status-Pre--Alpha-red.svg)]()

## 📌 Mission Brief
**Tactical Mobile Simulation (TMS)** is a rigorous, highly modular command-and-control (C2) tactical game engine engineered for mobile platforms. Emphasizing realism, squad-level autonomy, and hardcore physics, the TMS framework bridges the gap between desktop-grade military simulators and optimized mobile touch interfaces.

Built on the **Godot Engine** with a strictly tested **Python** backend for complex mathematical logic (such as ballistics and advanced trajectory systems), this project serves as the foundational architecture for granular battlefield management.

---

## ⚙️ Systems Architecture & Capabilities

### 1. Command & Control (C2) Interface
Designed for high-stress mobile deployment, the HUD abstracts complex orders into accessible operational primitives:
* **TacticalHUDView:** The primary viewport overlay for battlefield telemetry.
* **Waypointing (`MoveButton`):** Designate exact spatial coordinates for fireteam maneuverability.
* **Stance & Posture (`HoldButton`):** Enforce strict position-hold and defensive overwatch rules of engagement.

### 2. Autonomous Operations (`SquadAIController`)
A dedicated singleton framework governing unit behaviors, line-of-sight tracking, and dynamic pathfinding across the combat theater.

### 3. Ballistics & Kinetic Engine
A heavily decoupled Python logic layer (`systems.ballistics`) handling raw calculations for projectile trajectories, penetration values, and environmental variables, ensuring deterministic and highly realistic combat outcomes.

### 4. Theater Logistics
* **`TacticalAssetManager`:** Dynamic memory pooling and asset provisioning for environments, entities, and ordnance.
* **`TacticalAudioManager`:** Spatial audio rendering for distinct situational awareness (gunfire crack, radio static, footfalls).
* **`SaveManager`:** Persistent state handling for multi-phase operations and campaign telemetry.

---

## 🚀 Deployment & Installation

### Prerequisites
* **Godot Engine 4.x**
* **Python 3.10+** (For core logic testing)
* Target Deployment: Optimized for mobile runtimes (touch interfaces, rigorously tested on hardware including iOS).

### Bootstrapping the Engine
1. **Clone the repository** to your local development environment:
   ```bash
   git clone [https://github.com/your-username/tactical-mobile-game.git](https://github.com/your-username/tactical-mobile-game.git)
