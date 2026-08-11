class SquadCommandInterface:
    def __init__(self):
        self.active_orders = {}

    def issue_order(self, unit_id, order_type, target_position):
        valid_orders = ["MOVE", "HOLD", "BOUND", "FIRE_AT_WILL"]
        if order_type not in valid_orders:
            raise ValueError(f"Invalid order type: {order_type}")
            
        self.active_orders[unit_id] = {
            "order": order_type,
            "target": target_position,
            "status": "IN_PROGRESS"
        }
        return self.active_orders[unit_id]

    def get_unit_status(self, unit_id):
        return self.active_orders.get(unit_id, {"order": "IDLE", "status": "READY"})
