import asyncio
import os

from dotenv import load_dotenv
from fivem import FiveM

load_dotenv(verbose=True)

test_ip = os.getenv("FIVEM_TEST_IP")
test_port = os.getenv("FIVEM_TEST_PORT")


async def main():
    fivem = FiveM(ip=test_ip, port=test_port)
    players = await fivem.get_players_raw()
    info = await fivem.get_info_raw()
    dynamic = await fivem.get_dynamic_raw()
    players = await fivem.get_players()
    server = await fivem.get_server_info()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
