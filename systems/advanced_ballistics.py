class AdvancedBallistics:
    def __init__(self, gravity=9.81): self.gravity = gravity
    def calculate_trajectory(self, muzzle_velocity, zero_range, wind_speed_mps, distance_m, angle_deg): import math; rad = math.radians(angle_deg); time_of_flight = distance_m / (muzzle_velocity * math.cos(rad)); drop = 0.5 * self.gravity * (time_of_flight ** 2); drift = wind_speed_mps * time_of_flight; return {"distance": distance_m, "drop_m": round(drop, 2), "wind_drift_m": round(drift, 2), "flight_time_s": round(time_of_flight, 3)}
