class ArmaMedicalSystem:
    def __init__(self, name):
        self.name = name
        self.hp = 60
        self.is_bleeding = True
        self.bandages = 2

    def apply_bandage(self):
        if self.bandages > 0:
            self.bandages -= 1
            self.is_bleeding = False
            self.hp = min(100, self.hp + 20)
            print(f"{self.name} applied a tourniquet and bandage. Bleeding stopped! HP restored to {self.hp}/100")
        else:
            print(f"{self.name} is out of bandages and still bleeding out!")

medic = ArmaMedic = ArmaMedicalSystem("Operator Delta")
medic.apply_bandage()
