class NetworkSyncManager:
    def __init__(self, node_id):
        self.node_id = node_id
        self.connected_peers = []
        self.packet_queue = []

    def register_peer(self, peer_ip):
        if peer_ip not in self.connected_peers:
            self.connected_peers.append(peer_ip)

    def send_packet(self, destination, data):
        packet = {
            "sender": self.node_id,
            "target": destination,
            "payload": data
        }
        self.packet_queue.append(packet)

    def process_incoming_packets(self):
        processed = self.packet_queue.copy()
        self.packet_queue.clear()
        return processed
