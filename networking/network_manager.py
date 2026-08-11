class NetworkManager:
    def __init__(self, host="127.0.0.1", port=7777):
        self.host = host
        self.port = port
        self.connected_peers = {}
        self.is_server = False

    def start_host(self):
        self.is_server = True
        print(f"Server started on {self.host}:{self.port}")
        return True

    def register_peer(self, peer_id, username):
        if self.is_server:
            self.connected_peers[peer_id] = {
                "username": username,
                "status": "CONNECTED"
            }
            return True
        return False

    def serialize_game_state(self, player_id, position, action):
        import json
        payload = {
            "peer_id": player_id,
            "pos": position,
            "current_action": action
        }
        return json.dumps(payload)

    def receive_rpc(self, payload_json):
        import json
        data = json.loads(payload_json)
        # Handle remote procedure call synchronization
        return data
