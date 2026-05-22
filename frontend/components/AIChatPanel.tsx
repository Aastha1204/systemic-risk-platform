"use client"

import { useState } from "react"

type Message = {
  role: "user" | "ai"
  content: string
}

export default function AIChatPanel() {

  const [question, setQuestion] = useState("")

  const [messages, setMessages] = useState<Message[]>([])

  const [loading, setLoading] = useState(false)



  const askAI = async () => {

    if (!question.trim()) return

    const userQuestion = question



    // USER MESSAGE

    setMessages((prev) => [

      ...prev,

      {

        role: "user",

        content: userQuestion
      }
    ])



    setQuestion("")

    setLoading(true)



    try {

      // FASTAPI RAG API

      const response = await fetch(

        `http://localhost:8000/rag?question=${encodeURIComponent(userQuestion)}`
      )



      const data = await response.json()



      // AI MESSAGE

      setMessages((prev) => [

        ...prev,

        {

          role: "ai",

          content: data.response
        }
      ])

    } catch (error) {

      console.log(error)



      setMessages((prev) => [

        ...prev,

        {

          role: "ai",

          content: "AI engine connection failed."
        }
      ])
    }



    setLoading(false)
  }



  return (

    <div className="bg-black/40 border border-cyan-500/20 rounded-2xl p-6 h-full flex flex-col">

      {/* HEADER */}

      <h2 className="text-cyan-400 text-2xl font-bold mb-6">

        AI Financial Analyst

      </h2>



      {/* CHAT AREA */}

      <div className="flex-1 overflow-y-auto space-y-4 mb-6 h-[400px] pr-2">

        {

          messages.map((msg, index) => (

            <div

              key={index}

              className={`rounded-2xl p-4 whitespace-pre-wrap leading-relaxed border ${

                msg.role === "user"

                  ? "bg-cyan-500/10 border-cyan-500/20 text-cyan-300"

                  : "bg-white/5 border-white/10 text-white"

              }`}
            >

              <div className="font-bold mb-2">

                {

                  msg.role === "user"

                    ? "You"

                    : "AI Analyst"
                }

              </div>



              {msg.content}

            </div>
          ))
        }



        {

          loading && (

            <div className="text-cyan-400 animate-pulse">

              AI analyzing systemic risk...
            </div>
          )
        }

      </div>



      {/* INPUT SECTION */}

      <div className="flex gap-3 items-center">

        <input

          value={question}

          onChange={(e) =>

            setQuestion(e.target.value)
          }

          placeholder="Ask about systemic risk..."

          className="
            flex-1
            bg-[#07111f]
            border
            border-cyan-500/10
            rounded-xl
            p-4
            text-white
            placeholder:text-gray-500
            outline-none
            focus:outline-none
            focus:ring-0
            focus:border-cyan-400
            shadow-none
          "
        />



        <button

          onClick={askAI}

          className="
            bg-cyan-500
            hover:bg-cyan-400
            text-black
            font-bold
            px-6
            py-4
            rounded-xl
            transition-all
            duration-300
          "
        >

          Ask

        </button>

      </div>

    </div>
  )
}