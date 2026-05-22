import os

from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma



DOCS_PATH = "backend/rag/docs"



all_docs = []



# LOAD ALL PDFs AUTOMATICALLY

for file in os.listdir(DOCS_PATH):



    if file.endswith(".pdf"):



        pdf_path = os.path.join(

            DOCS_PATH,

            file
        )



        print(f"Loading {file}...")



        loader = PyPDFLoader(

            pdf_path
        )



        docs = loader.load()



        all_docs.extend(docs)



# SPLIT DOCUMENTS

splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50
)



chunks = splitter.split_documents(

    all_docs
)



print(f"Total chunks: {len(chunks)}")



# EMBEDDINGS

embedding = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



# CREATE VECTOR DATABASE

db = Chroma.from_documents(

    chunks,

    embedding,

    persist_directory="backend/rag/vector_db"
)



db.persist()



print("RAG VECTOR DATABASE CREATED 😭🔥")