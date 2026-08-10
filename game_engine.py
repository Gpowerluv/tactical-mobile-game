class AcousticSystem:
    SURFACE_MODIFIERS = {"Concrete": 1.0, "Wood": 1.3, "Metal": 1.8, "Grass": 0.5}
    MOVEMENT_MODIFIERS = {"Prone": 0.1, "Crouch": 0.4, "Walk": 1.0, "Sprint": 2.2}

    def calculate_footstep_audio(self, movement_state, surface_type, distance_to_ai):
        base_db = 40.0
        move_mult = self.MOVEMENT_MODIFIERS.get(movement_state, 1.0)
        surf_mult = self.SURFACE_MODIFIERS.get(surface_type, 1.0)
        generated_db = base_db * move_mult * surf_mult
        audible_db = max(0.0, generated_db - (distance_to_ai * 0.8))
        detected = audible_db > 15.0
        print(f"[ACOUSTICS] {movement_state} on {surface_type} | Sound: {generated_db:.1f} dB | At AI ({distance_to_ai}m): {audible_db:.1f} dB | Heard: {detected}")
        return detected

print("--- TACTICAL SIMULATION ENGINE: ACOUSTIC SYSTEM ---")
sound = AcousticSystem()
sound.calculate_footstep_audio("Sprint", "Metal", 25)
sound.calculate_footstep_audio("Crouch", "Grass", 25)
