import json

import aiohttp

from .player import parse_players_json
from .server import Server, parse_server_data


async def _fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return json.loads(text)


class FiveM:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.url = f"http://{self.ip}:{self.port}"

    async def get_players_raw(self) -> list:
        url = f"{self.url}/players.json"
        players = await _fetch_json(url)
        return players

    async def get_info_raw(self) -> dict:
        url = f"{self.url}/info.json"
        info = await _fetch_json(url)
        return info

    async def get_dynamic_raw(self) -> dict:
        url = f"{self.url}/dynamic.json"
        dynamic = await _fetch_json(url)
        return dynamic

    async def get_players(self) -> list:
        players_data = await self.get_players_raw()
        return parse_players_json(players_data)

    async def get_server_info(self) -> Server:
        server_data = await self.get_dynamic_raw()
        return parse_server_data(server_data)
