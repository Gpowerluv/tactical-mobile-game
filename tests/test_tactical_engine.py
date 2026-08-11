import unittest
from systems.ballistics import BallisticsEngine
from systems.vision import LineOfSightSystem
from systems.command_interface import SquadCommandInterface

class TestTacticalEngine(unittest.TestCase):
    
    def test_ballistics_trajectory(self):
        engine = BallisticsEngine(gravity=9.81)
        path = engine.calculate_projectile_path(initial_velocity=100, angle_deg=45, time_steps=[0, 1, 2])
        self.assertGreater(len(path), 0)
        self.assertEqual(path[0], (0.0, 0.0))

    def test_line_of_sight(self):
        los = LineOfSightSystem(max_range=50.0, fov_angle=90.0)
        # Target directly in front
        visible = los.check_visibility(observer_pos=(0, 0), observer_facing_deg=0, target_pos=(10, 0))
        self.assertTrue(visible)
        
        # Target behind observer
        not_visible = los.check_visibility(observer_pos=(0, 0), observer_facing_deg=0, target_pos=(-10, 0))
        self.assertFalse(not_visible)

    def test_squad_commands(self):
        commander = SquadCommandInterface()
        order = commander.issue_order("alpha_1", "MOVE", (100.0, 200.0))
        self.assertEqual(order["order"], "MOVE")
        self.assertEqual(order["status"], "IN_PROGRESS")

if __name__ == "__main__":
    unittest.main()
