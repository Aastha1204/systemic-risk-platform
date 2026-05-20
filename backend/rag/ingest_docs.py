from langchain.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter


loader = PyPDFLoader(

    "backend/rag/crisis_docs/lehman_report.pdf"
)

docs = loader.load()


splitter = RecursiveCharacterTextSplitter(

    chunk_size=500,

    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

print(chunks[:2])