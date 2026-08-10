import random

class RecoilSystem:
    def __init__(self, vertical_recoil, horizontal_recoil, stamina_percent):
        self.vert = vertical_recoil
        self.horiz = horizontal_recoil
        self.stamina = stamina_percent

    def calculate_shot_deviation(self):
        sway_factor = (100 - self.stamina) * 0.05
        vert_offset = self.vert + random.uniform(-0.5, 1.5) + sway_factor
        horiz_offset = random.uniform(-self.horiz, self.horiz) + random.uniform(-sway_factor, sway_factor)
        print(f"[GUNPLAY] Shot Fired | Vertical Kick: +{vert_offset:.2f} MOA | Horizontal Drift: {horiz_offset:.2f} MOA | Stamina Sway Impact: +{sway_factor:.2f}")
        return vert_offset, horiz_offset

print("--- TACTICAL SIMULATION ENGINE: RECOIL & SWAY ---")
gun = RecoilSystem(vertical_recoil=2.5, horizontal_recoil=1.2, stamina_percent=40)
for i in range(3):
    gun.calculate_shot_deviation()
