import asyncio
import websockets


async def handler(ws):

    async for msg in ws:

        print(
            "Received:",
            msg
        )

        await ws.send(
            "ACP response: I can help"
        )



async def main():

    async with websockets.serve(
        handler,
        "localhost",
        9000
    ):

        await asyncio.Future()


asyncio.run(main())
