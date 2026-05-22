from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from fastapi import WebSocket

from backend.utils.gemini_engine import ask_gemini

from backend.rag.rag_pipeline import ask_rag

from fastapi import UploadFile, File


import asyncio
import shutil
import random



app = FastAPI()



# FRONTEND CONNECTION

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)



# ROOT API

@app.get("/")

def root():

    return {

        "message": "Systemic Risk Platform Running"
    }



# LIVE RISK API

@app.get("/risk")

def get_risk():

    return {

        "systemic_risk": round(

            random.uniform(0.4, 0.95),

            2
        ),

        "volatility": random.randint(

            30,

            90
        ),

        "liquidity": random.choice(

            ["LOW", "MEDIUM", "HIGH"]

        ),

        "contagion": random.choice(

            ["LOW", "MEDIUM", "HIGH"]

        )
    }

@app.post("/upload-pdf")

async def upload_pdf(

    file: UploadFile = File(...)
):


    # SAVE PATH

    save_path = f"backend/rag/docs/{file.filename}"



    # SAVE PDF

    with open(save_path, "wb") as buffer:

        shutil.copyfileobj(

            file.file,

            buffer
        )



    return {

        "message": f"{file.filename} uploaded successfully 😭🔥"
    }

# AI ANALYST API

@app.get("/ask_ai")

def ask_ai(question: str):

    answer = ask_gemini(question)



    return {

        "response": answer
    }

@app.get("/rag")

def rag_query(question: str):

    answer = ask_rag(question)



    return {

        "response": answer
    }

# LIVE WEBSOCKET

@app.websocket("/ws")

async def websocket_endpoint(

    ws: WebSocket
):

    await ws.accept()



    while True:

        data = {

            "risk": round(

                random.uniform(0.4, 0.95),

                2
            )
        }



        await ws.send_json(data)



        await asyncio.sleep(2)