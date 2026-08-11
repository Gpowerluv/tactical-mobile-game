# Changelog

## [Unreleased]
### Added
- **Scenes (`/scenes`)**: Added `main.tscn` to configure the primary Node3D map environment, directional lighting, camera, and HUD attachment points.
- **Scenes (`/scenes`)**: Added `unit.tscn` as the base CharacterBody3D template for tactical squad members linked to the squad AI controller.
- **Networking (`/networking`)**: Added `sync_manager.py` to handle peer-to-peer state tracking, packet queuing, and multi-client position synchronization.
- **Configurations (`/configs`)**: Added `vehicle_stats.json` defining comprehensive stats for both land transport (APCs, offroads) and air vehicles including transport helicopters and recon drones.
