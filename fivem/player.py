def parse_players_json(data) -> list:
    players = list()
    for p in data:
        name = p.get("name")
        _id = p.get("id")
        identifiers = p.get("identifiers")
        ping = p.get("ping")
        player = Player(name, _id, identifiers, ping)
        players.append(player)
    return players


def parse_identifier(identifier):
    service, _id = identifier.split(":")
    return service, _id


class Player:
    def __init__(self, name, _id, identifiers, ping):
        self.name = name
        self.id = _id
        self.ping = ping
        self.xbl_id = None
        self.steam_id = None
        self.discord_id = None
        self.live_id = None
        self.license_id = None
        if identifiers is not None:
            for identifier in identifiers:
                service, _id = parse_identifier(identifier)
                if service == "xbl":
                    self.xbl_id = _id
                elif service == "steam":
                    self.steam_id = _id
                elif service == "discord":
                    self.discord_id = _id
                elif service == "live":
                    self.live_id = _id
                elif service == "license":
                    self.license_id = _id

    def __repr__(self):
        return f"<Player: {self.name}, id: {self.id}, ping: {self.ping}>"
