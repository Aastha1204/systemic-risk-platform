from fastapi import WebSocket
import asyncio


async def send_live_updates(ws: WebSocket):

    await ws.accept()

    while True:

        await ws.send_text(

            "🚨 Live systemic risk update"
        )

        await asyncio.sleep(2)