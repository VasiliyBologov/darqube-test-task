import asyncio
import random
import websockets
import json

import conf


async def handler(websocket, path):
    while True:
        data = [{
              "name": name,
              "number": round(random.uniform(50, 99), 2)
        } for name in conf.FLOWS]
        await websocket.send(json.dumps(data))
        await asyncio.sleep(0.1)


def start():
    start_server = websockets.serve(handler, "127.0.0.1", 5006)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

