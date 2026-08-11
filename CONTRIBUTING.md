# Standard Operating Procedure (SOP): Engine Contributions

Welcome to the development team. To maintain operational readiness, minimize structural regressions, and ensure the absolute stability of the Tactical Mobile Simulation engine, all operators must strictly adhere to the following protocols when deploying new features or patching engine logic.

---

## Tactical Branching Protocols

### 1. Establish an Operational Sector (Feature Branches)
Direct code insertions to the `main` branch are strictly prohibited. All development must occur in isolated, descriptive branches before being cleared for integration.
* **Feature Integration:** `feature/ballistics-update`
* **Vulnerability Mitigation:** `bugfix/touch-controls`
* **Infrastructure/Telemetry:** `net/multiplayer-sync`

### 2. Maintain Synchronization (Syncing)
Operators must continuously pull the latest operational state from `main` into their working branches. Failure to sync regularly leads to critical merge conflicts during final deployment. Keep your local intel up to date.

---

## Engineering Rules of Engagement (ROE)

### Strict Syntax Discipline (Python, C#, & GDScript)
Code clean, code precise. Maintain rigorous architectural discipline across all scripts. Any complex mathematical telemetry—specifically within `systems.ballistics` or `SquadAIController`—must be accompanied by comprehensive inline documentation to allow allied developers to understand the logic.

### Automated Telemetry Validation (Testing)
All submitted payloads must pass the automated GitHub Actions Continuous Integration (CI) pipeline. 
* Add or update Python unit tests for all new core logic.
* If your pull request fails the CI test battery, the insertion will be aborted and sent back for refactoring. Broken builds compromise the entire framework.
