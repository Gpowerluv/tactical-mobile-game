class EnvironmentalBallistics:
    def __init__(self, wind_speed_ms, wind_direction_deg):
        self.wind_speed = wind_speed_ms
        self.wind_direction = wind_direction_deg

    def calculate_wind_drift(self, distance_m, time_of_flight_s):
        # Simplified crosswind deflection formula
        drift_cm = (self.wind_speed * time_of_flight_s) * 100
        print(f"[ENVIRONMENT] Wind: {self.wind_speed} m/s at {self.wind_direction}° | Target Distance: {distance_m}m | Drift Deflection: {drift_cm:.1f} cm")
        return drift_cm

# Test environmental calculation
env = EnvironmentalBallistics(4.5, 90)
env.calculate_wind_drift(500, 0.65)
