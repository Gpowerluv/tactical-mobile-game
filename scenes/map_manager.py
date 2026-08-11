class MapManager:
    def __init__(self, map_name="tactical_valley"):
        self.map_name = map_name
        self.spawn_points = {
            "alpha_team": (0.0, 0.0, 0.0),
            "bravo_team": (50.0, 0.0, 10.0)
        }
        self.cover_nodes = []

    def register_cover_node(self, position, cover_type="full"):
        node = {
            "pos": position,
            "type": cover_type, # e.g., "full", "half", "concealment"
            "occupied": False
        }
        self.cover_nodes.append(node)
        return node

    def get_nearest_cover(self, unit_position):
        if not self.cover_nodes:
            return None
            
        import math
        best_cover = None
        min_dist = float('inf')
        
        for node in self.cover_nodes:
            if node["occupied"]:
                continue
            dist = math.sqrt((node["pos"][0] - unit_position[0])**2 + (node["pos"][1] - unit_position[1])**2)
            if dist < min_dist:
                min_dist = dist
                best_cover = node
                
        return best_cover
