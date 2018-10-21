import asyncio

import websockets
from aioconsole import ainput


async def send_message(ws):
    while True:
        await asyncio.sleep(0)
        message = await ainput("> ")
        await ws.send(message)


async def receive_message(ws):
    while True:
        await asyncio.sleep(1)
        async for res in ws:
            print(res)


async def connect(uri):
    async with websockets.connect(uri) as ws:
        await asyncio.gather(*[send_message(ws), receive_message(ws)])


def main():
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(connect('ws://localhost:8765'))
    loop.run_forever()


if name == 'main':
    main()
 
