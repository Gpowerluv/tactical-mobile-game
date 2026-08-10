class InventoryManager:
    def __init__(self, capacity_kg=30.0):
        self.capacity = capacity_kg
        self.items = {}

    def add_item(self, name, weight_kg):
        current_weight = sum(self.items.values())
        if current_weight + weight_kg > self.capacity:
            print(f"[OVERBURDENED] Cannot add {name} ({weight_kg}kg)! Weight capacity exceeded.")
            return False
        self.items[name] = weight_kg
        total = current_weight + weight_kg
        mobility_penalty = (total / self.capacity) * 40  # Max 40% speed drop at full load
        print(f"[INVENTORY] Added {name} ({weight_kg}kg) | Load: {total:.1f}/{self.capacity}kg | Movement Speed: -{mobility_penalty:.1f}%")
        return True

# Test inventory load
loadout = InventoryManager(30.0)
loadout.add_item("Plate Carrier & Plates", 8.5)
loadout.add_item("HK416 Rifle + Ammo", 6.2)
loadout.add_item("First Aid Kit", 1.5)
loadout.add_item("Tactical Backpack", 15.0)
