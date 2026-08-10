import random

class ExfilSystem:
    def __init__(self, zone_name, req_item=None):
        self.zone = zone_name
        self.req_item = req_item
        self.timer = 10  # seconds

    def search_container(self, container_type):
        loot_pool = {"Safe": ["Gold Bar", "GPU", "Folder of Intelligence"], "Duffle Bag": ["Bandage", "5.56 Ammo", "Ration Bar"]}
        items = loot_pool.get(container_type, ["Trash"])
        found = random.choice(items)
        print(f"[LOOTING] Searched {container_type}... Found: {found}")
        return found

    def attempt_extract(self, player_inventory):
        if self.req_item and self.req_item not in player_inventory:
            print(f"[EXFIL DENIED] Zone '{self.zone}' requires: {self.req_item}")
            return False
        print(f"[EXFIL SUCCESS] Extraction timer ended ({self.timer}s). Successfully extracted from {self.zone}!")
        return True

print("--- TACTICAL SIMULATION ENGINE: EXTRACTION & LOOTING ---")
raid = ExfilSystem("Cell Tower Exfil", req_item="Red Keycard")
raid.search_container("Safe")
raid.attempt_extract(["Gold Bar"])
raid.attempt_extract(["Gold Bar", "Red Keycard"])
