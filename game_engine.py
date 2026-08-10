import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
    def attack(self, target):
        dmg = random.randint(10, self.attack_power)
        target.hp = max(0, target.hp - dmg)
        print(f"{self.name} hits {target.name} for {dmg} damage! ({target.name} HP: {target.hp})")

hero = Character("Operator", 100, 25)
enemy = Character("Hostile AI", 80, 20)
hero.attack(enemy)
