class DamageSystem:
    HITBOX_MULTIPLIERS = {"Head": 2.5, "Thorax": 1.0, "Stomach": 0.85, "Legs": 0.6}

    def __init__(self, armor_level, armor_durability):
        self.armor_level = armor_level
        self.durability = armor_durability

    def process_hit(self, hitbox, base_damage, bullet_pen_class):
        multiplier = self.HITBOX_MULTIPLIERS.get(hitbox, 1.0)
        raw_dmg = base_damage * multiplier

        if hitbox == "Thorax" and self.durability > 0:
            if bullet_pen_class >= self.armor_level:
                actual_dmg = raw_dmg
                self.durability = max(0, self.durability - 15)
                result = f"PENETRATION! Armor durability down to {self.durability}"
            else:
                actual_dmg = raw_dmg * 0.15
                self.durability = max(0, self.durability - 5)
                result = f"BLOCKED by Level {self.armor_level} Plate! Blunt damage applied."
        else:
            actual_dmg = raw_dmg
            result = "UNARMED HIT"

        print(f"[DAMAGE] Hitbox: {hitbox} | Raw: {raw_dmg:.1f} | Result: {result} | Final Damage: {actual_dmg:.1f}")
        return actual_dmg

print("--- TACTICAL SIMULATION ENGINE: ARMOR & HITBOX SYSTEM ---")
target = DamageSystem(armor_level=4, armor_durability=50)
target.process_hit("Head", 35, bullet_pen_class=3)
target.process_hit("Thorax", 35, bullet_pen_class=3)
target.process_hit("Thorax", 35, bullet_pen_class=4)
