class OperatorMovement:
    def __init__(self, name):
        self.name = name
        self.in_cover = False
        self.lean_state = "Center"
        self.exposure = 100

    def toggle_cover(self):
        self.in_cover = not self.in_cover
        self.exposure = 20 if self.in_cover else 100
        status = "slid into cover" if self.in_cover else "stepped out of cover"
        print(f"[TACTICS] {self.name} {status}. Body Exposure: {self.exposure}%")

    def lean(self, direction):
        if not self.in_cover:
            print(f"[WARNING] {self.name} is in the open and cannot lean!")
            return
        self.lean_state = direction
        if direction in ["Left", "Right"]:
            self.exposure = 45
            print(f"[ACTION] {self.name} leaning {direction}. Slicing the angle (Exposure: {self.exposure}%)")
        else:
            self.exposure = 20
            print(f"[ACTION] {self.name} tucked back into Center. (Exposure: {self.exposure}%)")

print("--- TACTICAL SIMULATION ENGINE: COVER & LEAN ---")
player = OperatorMovement("Operator Alpha")
player.lean("Right")
player.toggle_cover()
player.lean("Right")
player.lean("Center")
