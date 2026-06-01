from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from fastapi import WebSocket

from backend.utils.gemini_engine import ask_gemini

from backend.rag.rag_pipeline import ask_rag

from fastapi import UploadFile, File
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


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

    save_path = f"backend/rag/docs/{file.filename}"

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # LOAD PDF
    loader = PyPDFLoader(save_path)
    documents = loader.load()

    # SPLIT INTO CHUNKS
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    # EMBEDDINGS
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # CHROMA DB
    db = Chroma(
        persist_directory="backend/rag/vector_db",
        embedding_function=embedding
    )

    # ADD PDF TO VECTOR DB
    db.add_documents(chunks)

    return {
        "message": f"{file.filename} uploaded and indexed successfully 🚀"
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