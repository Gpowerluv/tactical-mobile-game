class AIPatrolSystem:
    def __init__(self, waypoints):
        self.waypoints = waypoints
        self.current_index = 0
        self.alert_state = "PATROL"

    def patrol_step(self):
        target = self.waypoints[self.current_index]
        print(f"[AI PATROL] Unit moving to Waypoint {self.current_index + 1}: {target} | State: {self.alert_state}")
        self.current_index = (self.current_index + 1) % len(self.waypoints)

    def trigger_alert(self, new_state):
        self.alert_state = new_state
        print(f"[AI ALERT] Threat level updated: *** {self.alert_state} ***")

print("--- TACTICAL SIMULATION ENGINE: AI PATROL & ALERT LOOP ---")
ai = AIPatrolSystem(["Sector Alpha", "Sector Bravo", "Main Gate"])
ai.patrol_step()
ai.patrol_step()
ai.trigger_alert("SUSPICIOUS")
ai.patrol_step()
ai.trigger_alert("COMBAT")
