import random

class ArmaTacticalSim:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.stamina = 100
        self.suppression = 0
        self.stance = "Standing"

    def move(self, sprinting=False):
        cost = 25 if sprinting else 10
        self.stamina = max(0, self.stamina - cost)
        print(f"{self.name} moved (Sprinting: {sprinting}). Stamina: {self.stamina}/100")

    def take_suppressive_fire(self):
        self.suppression = min(100, self.suppression + 40)
        print(f"[SUPPRESSION] {self.name} is pinned down by incoming rounds! Suppression Level: {self.suppression}%")

    def fire_weapon(self, target):
        if self.suppression > 50:
            print(f"{self.name} is too suppressed to aim accurately! Shots went wide.")
            return
        
        damage = random.randint(15, 25)
        target.take_suppressive_fire()
        print(f"{self.name} fires back, applying suppression to {target.name}!")

# Simulate a tactical engagement
op1 = ArmaTacticalSim("Operator Alpha")
op2 = ArmaTacticalSim("Opfor Combatant")

op1.move(sprinting=True)
op1.fire_weapon(op2)
