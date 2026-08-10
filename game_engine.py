class MedicalSystem:
    def __init__(self):
        self.hp = 100
        self.heavy_bleeding = False
        self.fractured_leg = False

    def receive_injury(self, injury_type):
        if injury_type == "bleeding":
            self.heavy_bleeding = True
            print("[INJURY] Heavy bleeding sustained! HP will drain rapidly.")
        elif injury_type == "fracture":
            self.fractured_leg = True
            print("[INJURY] Fractured leg sustained! Sprinting disabled.")

    def apply_treatment(self, medical_item):
        if medical_item == "Tourniquet" and self.heavy_bleeding:
            self.heavy_bleeding = False
            print("[MEDICAL] Tourniquet applied. Heavy bleeding stopped.")
        elif medical_item == "Surgical Kit" and self.fractured_leg:
            self.fractured_leg = False
            print("[MEDICAL] Surgical kit used. Fracture repaired.")
        else:
            print(f"[MEDICAL] Used {medical_item}.")

print("--- TACTICAL SIMULATION ENGINE: MEDICAL SYSTEM ---")
med = MedicalSystem()
med.receive_injury("bleeding")
med.receive_injury("fracture")
med.apply_treatment("Tourniquet")
med.apply_treatment("Surgical Kit")
