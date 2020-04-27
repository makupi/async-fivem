class Server:
    def __init__(self, hostname, clients, max_clients, game_type, map_name):
        self.hostname = hostname
        self.clients = clients
        self.max_clients = max_clients
        self.game_type = game_type
        self.map_name = map_name

    def __repr__(self):
        return f"<hostname: {self.hostname}, clients: {self.clients}>"


def parse_server_data(data) -> Server:
    hostname = data.get("hostname")
    clients = data.get("clients")
    max_clients = data.get("sv_maxclients")
    game_type = data.get("gametype")
    map_name = data.get("mapname")
    return Server(hostname, clients, max_clients, game_type, map_name)
