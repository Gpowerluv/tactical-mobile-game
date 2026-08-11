class LineOfSightSystem:
    def __init__(self, max_range=100.0, fov_angle=90.0):
        self.max_range = max_range
        self.fov_angle = fov_angle

    def check_visibility(self, observer_pos, observer_facing_deg, target_pos):
        import math
        
        # Calculate distance
        dx = target_pos[0] - observer_pos[0]
        dy = target_pos[1] - observer_pos[1]
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance > self.max_range:
            return False
            
        # Calculate angle
        target_angle = math.degrees(math.atan2(dy, dx))
        angle_diff = (target_angle - observer_facing_deg + 180) % 360 - 180
        
        return abs(angle_diff) <= (self.fov_angle / 2)
