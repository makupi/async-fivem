# async-fivem
Asynchronous FiveM package for retrieving Player and Server infos utilizing the [aiohttp](https://docs.aiohttp.org/en/stable/) package.

## Installation

async-fivem can be installed via pip.

`pip install async-fivem`

## Usage
```python
import asyncio
from fivem import FiveM

ip = "127.0.0.1"
port = 30120

async def main():
    fivem = FiveM(ip=ip, port=port)
    # raw list of players like you get from /players.json
    players = await fivem.get_players_raw()
    # raw json of server-info like you get from /info.json
    info = await fivem.get_info_raw()
    # raw json of server-info like you get from /dynamic.json
    dynamic = await fivem.get_dynamic_raw()
    # parsed list of Player objects 
    players = await fivem.get_players()
    # parsed Server object
    server = await fivem.get_server_info()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Api Reference

### FiveM

*class* FiveM(ip: *str*, port: *int*):
- **await get_players_raw()** -> list: */players.json endpoint - raw list of players*
- **await get_info_raw()** -> dict: */info.json endpoint - raw dict with server-info*
- **await get_dynamic_raw()** -> dict: */dynamic.json endpoint - raw dict with server-info*
- **await get_players()** -> [[Player](#Player)]: *returns parsed list of [Player](#Player) objects*
- **await get_server_info()** -> [Server](#Server): *returns parsed server info [Server](#Server)*

### Player
*class* Player:
- **name**: *player username*
- **id**: *player id*
- **ping**: *current player ping*
- **xbl_id**: *xbl id, None if not available*
- **steam_id**: *steam id, None if not available*
- **discord_id**: *discord id, None if not available*
- **live_id**: *live id, None if not available*
- **license_id**: *license id, None if not available*

### Server
*class* Server:
- **hostname**: *servers hostname*
- **clients**: *current number of clients*
- **max_clients**: *max clients allowed on server*
- **game_type**: *servers game type*
- **map_name**: *servers map name*

# Requirements
- Python >= 3.6
- [aiohttp](https://docs.aiohttp.org/en/stable/)

# Issues and Features
If you're having any issues or want additional features please create an Issue on [github](https://github.com/makupi/async-fivem/issues).

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/A0A015HXK)
