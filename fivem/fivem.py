import json

import aiohttp

from .player import parse_players_json


async def _fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            return json.loads(text)


class FiveM:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.url = f"http://{self.ip}:{self.port}"

    async def get_players_raw(self) -> dict:
        url = f"{self.url}/players.json"
        players = await _fetch_json(url)
        return players

    async def get_info_raw(self):
        url = f"{self.url}/info.json"
        info = await _fetch_json(url)
        return info

    async def get_dynamic_raw(self):
        url = f"{self.url}/dynamic.json"
        dynamic = await _fetch_json(url)
        return dynamic

    async def players(self):
        players_data = await self.get_players_raw()
        parse_players_json(players_data)
