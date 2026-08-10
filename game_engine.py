import random

class ArmaCombatSim:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.plate_armor = 50  # Plate carrier durability

    def take_hit(self, zone, base_dmg):
        if zone == "Chest" and self.plate_armor > 0:
            absorbed = min(self.plate_armor, base_dmg * 0.7)
            self.plate_armor -= int(absorbed)
            actual_dmg = int(base_dmg - absorbed)
            print(f"{self.name}'s plate carrier absorbed {int(absorbed)} damage! Armor left: {self.plate_armor}")
        elif zone == "Head":
            actual_dmg = base_dmg * 2
            print(f"[CRITICAL] Headshot on {self.name}!")
        else:
            actual_dmg = base_dmg
            print(f"{self.name} took an unarmored hit to the {zone}!")

        self.hp = max(0, self.hp - actual_dmg)
        print(f"{self.name} HP remaining: {self.hp}/100\n")

# Test engagement with armor zones
operator = ArmaCombatSim("Operator Alpha")
hostile = ArmaCombatSim("Opfor AI")

hostile.take_hit("Chest", 40)
operator.take_hit("Head", 30)
