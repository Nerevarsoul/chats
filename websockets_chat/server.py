import asyncio
import websockets


connected = set()


async def handler(websocket, path):
    connected.add(websocket)
    try:
        async for message in websocket:
            for ws in connected:
                if ws != websocket:
                    await ws.send(message)
    finally:
        connected.remove(websocket)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(websockets.serve(handler, 'localhost', 8765))
    loop.run_forever()


if name == 'main':
    main()
