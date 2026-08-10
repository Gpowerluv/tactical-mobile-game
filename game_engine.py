class MuzzleAttachment:
    def __init__(self, muzzle_type="Bare Muzzle"):
        self.muzzle_type = muzzle_type

    def get_stats(self):
        configs = {
            "Bare Muzzle": {"sound_db": 140, "flash_pct": 100, "weight_kg": 0.0, "ergo_penalty": 0},
            "Flash Hider": {"sound_db": 138, "flash_pct": 15, "weight_kg": 0.2, "ergo_penalty": 2},
            "Suppressor": {"sound_db": 88, "flash_pct": 5, "weight_kg": 0.6, "ergo_penalty": 8}
        }
        stats = configs.get(self.muzzle_type, configs["Bare Muzzle"])
        print(f"[ATTACHMENT] Device: {self.muzzle_type} | Sound: {stats['sound_db']}dB | Flash: {stats['flash_pct']}% | Weight: +{stats['weight_kg']}kg | Ergo Penalty: -{stats['ergo_penalty']}")
        return stats

print("--- TACTICAL SIMULATION ENGINE: MUZZLE ATTACHMENTS ---")
for muzzle in ["Bare Muzzle", "Flash Hider", "Suppressor"]:
    dev = MuzzleAttachment(muzzle)
    dev.get_stats()
