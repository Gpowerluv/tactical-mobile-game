import random

class ArmaOperator:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.stamina = 100
        self.stance = "Standing"
    def change_stance(self, new_stance):
        self.stance = new_stance
        print(f"{self.name} changed stance to [{self.stance}]")
    def engage_target(self, target):
        mod = 1.2 if self.stance == "Prone" else (1.0 if self.stance == "Crouching" else 0.8)
        dmg = int(random.randint(15, 30) * mod)
        target.hp = max(0, target.hp - dmg)
        print(f"{self.name} fires at {target.name} from {self.stance} for {dmg} damage! ({target.name} HP: {target.hp}/100)")

op = ArmaOperator("Operator One")
enemy = ArmaOperator("Opfor AI")
op.change_stance("Prone")
op.engage_target(enemy)
