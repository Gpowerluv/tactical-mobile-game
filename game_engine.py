class WeaponProfile:
    def __init__(self, name, caliber, damage, velocity):
        self.name = name
        self.caliber = caliber
        self.damage = damage
        self.velocity = velocity  # m/s

    def calculate_impact(self, distance_meters):
        # Velocity drop-off over distance
        dropoff = max(0.5, 1.0 - (distance_meters / 1000.0))
        effective_dmg = int(self.damage * dropoff)
        print(f"[BALLISTICS] {self.name} ({self.caliber}) fired at {distance_meters}m | Impact Damage: {effective_dmg}")
        return effective_dmg

# Test ballistics profile
rifle = WeaponProfile("HK416", "5.56x45mm", 35, 880)
rifle.calculate_impact(300)
