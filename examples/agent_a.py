import asyncio
import websockets


async def main():

    async with websockets.connect(
        "ws://localhost:9000"
    ) as ws:


        await ws.send(
        """
        {
        type:REQUEST,
        intent:help,
        content:Linux problem
        }
        """
        )


        result=await ws.recv()

        print(result)



asyncio.run(main())
