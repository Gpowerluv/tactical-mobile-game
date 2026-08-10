class OpticsSystem:
    def __init__(self, mode="Naked Eye"):
        self.mode = mode

    def render_view(self, ambient_light_lux, target_temp_c):
        if self.mode == "NVG":
            gain = max(0, 100 - ambient_light_lux * 10)
            print(f"[OPTICS - NVG] Green Phosphor Active | Image Gain: {gain}% | Ambient Lux: {ambient_light_lux}")
        elif self.mode == "Thermal":
            contrast = "HIGH HEAT SIGNATURE" if target_temp_c > 35 else "COLD ENVIRONMENT"
            print(f"[OPTICS - THERMAL] White-Hot Mode | Target Temp: {target_temp_c}°C | Status: {contrast}")
        else:
            print(f"[OPTICS - VISUAL] Standard Optical Sight | Light Level: {ambient_light_lux} lux")

print("--- TACTICAL SIMULATION ENGINE: OPTICS & SENSORS ---")
optic = OpticsSystem()
optic.render_view(ambient_light_lux=5, target_temp_c=37)
optic.mode = "NVG"
optic.render_view(ambient_light_lux=2, target_temp_c=37)
optic.mode = "Thermal"
optic.render_view(ambient_light_lux=2, target_temp_c=37)
