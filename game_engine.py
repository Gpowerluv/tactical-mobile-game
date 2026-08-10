import random

class TacticalOperator:
    def __init__(self, name, capacity=30.0):
        self.name = name
        self.capacity = capacity
        self.inventory = {}
        self.hp = 100
        self.stamina = 100
        self.in_cover = False
        self.exposure = 100

    def equip(self, item, weight):
        curr = sum(self.inventory.values())
        if curr + weight <= self.capacity:
            self.inventory[item] = weight
            print(f"[EQUIP] {item} ({weight}kg) | Load: {curr + weight:.1f}/{self.capacity}kg")
        else:
            print(f"[OVERBURDENED] Cannot equip {item}!")

    def enter_cover(self):
        self.in_cover = True
        self.exposure = 20
        print(f"[TACTICS] {self.name} took cover. Exposure: {self.exposure}%")

class MasterSimulation:
    def run_raid_scenario(self):
        print("=== MASTER TACTICAL RAID SIMULATION ===\n")
        op = TacticalOperator("Operator Alpha")
        op.equip("Plate Carrier L4", 8.5)
        op.equip("Suppressed Carbine", 4.2)
        op.equip("Medkit & Ammo", 3.0)
        print("\n--- STAGE 1: INFILTRATION ---")
        op.enter_cover()
        print("[ACOUSTICS] Footstep sound attenuated: 18.4 dB at 30m.")
        print("\n--- STAGE 2: ENGAGEMENT ---")
        print("[COMBAT] Fired 3-round burst. Recoil drift: +1.8 MOA vertical.")
        print("[DAMAGE] Target Thorax Hit | Plate Level 4 BLOCKED penetration | Blunt DMG: 5.2")
        print("\n--- STAGE 3: EXFILTRATION ---")
        print("[LOOT] Searched Tactical Safe: Secured Intelligence Folder.")
        print("[EXFIL] Extraction timer reached 0s. Exfil Successful!\n")

MasterSimulation().run_raid_scenario()
