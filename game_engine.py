import random

class TacticalOperator:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.stamina = 100
        self.suppression = 0
        self.plate_armor = 50
        self.stance = "Standing"
        self.bandages = 2
        self.is_bleeding = False

    def change_stance(self, stance):
        self.stance = stance
        print(f"{self.name} shifted stance to [{self.stance}]")

    def take_hit(self, zone, base_dmg):
        if zone == "Chest" and self.plate_armor > 0:
            absorbed = min(self.plate_armor, base_dmg * 0.7)
            self.plate_armor -= int(absorbed)
            actual_dmg = int(base_dmg - absorbed)
            print(f"{self.name}'s plate absorbed {int(absorbed)} dmg! Armor left: {self.plate_armor}")
        elif zone == "Head":
            actual_dmg = base_dmg * 2
            print(f"[CRITICAL] Headshot on {self.name}!")
        else:
            actual_dmg = base_dmg
            print(f"{self.name} took unarmored hit to {zone}!")

        self.hp = max(0, self.hp - actual_dmg)
        if actual_dmg > 15:
            self.is_bleeding = True
        print(f"{self.name} HP: {self.hp}/100 | Bleeding: {self.is_bleeding}")

    def apply_bandage(self):
        if self.bandages > 0 and self.is_bleeding:
            self.bandages -= 1
            self.is_bleeding = False
            self.hp = min(100, self.hp + 15)
            print(f"{self.name} bandaged wounds. Bleeding stopped! HP: {self.hp}/100")
        else:
            print(f"{self.name} cannot bandage right now.")

op1 = TacticalOperator("Alpha")
op2 = TacticalOperator("Bravo")

op1.change_stance("Prone")
op2.take_hit("Chest", 40)
op2.apply_bandage()
