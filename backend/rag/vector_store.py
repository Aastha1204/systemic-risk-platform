from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings


loader = PyPDFLoader(

    "backend/rag/crisis_docs/lehman_report.pdf"
)

docs = loader.load()


splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50
)

chunks = splitter.split_documents(docs)


embedding = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


db = Chroma.from_documents(

    chunks,

    embedding,

    persist_directory="backend/rag/vector_db"
)


print("✅ Vector Database Created")