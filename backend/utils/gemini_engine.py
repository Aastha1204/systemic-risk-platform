import ollama



def ask_gemini(question: str):

    prompt = f"""

    You are an enterprise AI financial analyst.



    Analyze:

    - systemic risk

    - contagion spread

    - liquidity crisis

    - financial instability

    - banking collapse

    - interbank exposure



    User Question:

    {question}

    """



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