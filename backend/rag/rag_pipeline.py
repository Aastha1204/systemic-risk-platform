from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

import ollama



# =========================
# LIVE MARKET DATA
# =========================

inflation = 6.1

volatility = "HIGH"

risk_score = 0.83



# =========================
# LOAD EMBEDDINGS
# =========================

embedding = HuggingFaceEmbeddings(

    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



# =========================
# LOAD VECTOR DATABASE
# =========================

db = Chroma(

    persist_directory="backend/rag/vector_db",

    embedding_function=embedding
)



# =========================
# MAIN RAG FUNCTION
# =========================

def ask_rag(question: str):



    # DYNAMIC QUERY

    query = f"""

    Current inflation is {inflation}

    Current market volatility is {volatility}

    Current systemic risk score is {risk_score}



    User Question:

    {question}



    Compare this situation

    to historical financial crises.

    """



    # VECTOR SEARCH

    results = db.similarity_search(

        query,

        k=3
    )



    # BUILD CONTEXT

    context = "\n".join(

        [result.page_content for result in results]
    )



    # FINAL AI PROMPT

    prompt = f"""

    You are an enterprise AI financial analyst.



    Analyze systemic risk,

    banking instability,

    contagion spread,

    and financial crises.



    Use BOTH:

    1. Historical financial documents

    2. Current market conditions



    CURRENT MARKET CONDITIONS:

    Inflation: {inflation}

    Volatility: {volatility}

    Risk Score: {risk_score}



    HISTORICAL DOCUMENT CONTEXT:

    {context}



    USER QUESTION:

    {question}

    """



    # OLLAMA AI RESPONSE

    response = ollama.chat(

        model="llama3",

        messages=[

            {

                "role": "user",

                "content": prompt
            }

        ]
    )



    return response["message"]["content"]