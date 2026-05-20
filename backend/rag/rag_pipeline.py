from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings


# MARKET DATA

inflation = 6.1

volatility = "HIGH"

risk_score = 0.83


# EMBEDDINGS

embedding = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# VECTOR DATABASE

db = Chroma(

    persist_directory="backend/rag/vector_db",

    embedding_function=embedding
)


# QUERY

query = f"""

Current inflation is {inflation}

Current market volatility is {volatility}

Risk score is {risk_score}

Compare this situation
to historical financial crises.
"""


# SEARCH

results = db.similarity_search(

    query,

    k=3
)


# OUTPUT

print("\n===== AI RISK ANALYST =====\n")


for i, result in enumerate(results, 1):

    print(f"\n🔹 RESULT {i}\n")

    print(result.page_content)

    print("\n-------------------------\n")