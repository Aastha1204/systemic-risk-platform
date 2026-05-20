from fastapi import FastAPI, WebSocket
import asyncio

from backend.db.database import engine
from backend.db.models import Base
from backend.api.routes import router



app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)
 
@app.get("/")
def root():
    return {"message": "Systemic Risk Platform Running"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):

    await ws.accept()

    while True:

        await ws.send_text("Live risk update")

        await asyncio.sleep(2)