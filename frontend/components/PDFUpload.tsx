"use client"

import { useState } from "react"

export default function PDFUpload() {

  const [file, setFile] = useState<File | null>(null)

  const [loading, setLoading] = useState(false)

  const [message, setMessage] = useState("")



  const uploadPDF = async () => {

    if (!file) return



    setLoading(true)



    const formData = new FormData()

    formData.append("file", file)



    try {

      const response = await fetch(

        "http://127.0.0.1:8000/upload-pdf",

        {

          method: "POST",

          body: formData
        }
      )



      const data = await response.json()



      setMessage(data.message)

    } catch (error) {

      console.log(error)

      setMessage("Upload failed.")
    }



    setLoading(false)
  }



  return (

    <div className="bg-black/40 border border-cyan-500/20 rounded-2xl p-6">

      <h2 className="text-cyan-400 text-2xl font-bold mb-6">

        PDF Intelligence Upload

      </h2>



      <div className="space-y-4">

        <input

          type="file"

          accept=".pdf"

          onChange={(e) => {

            if (e.target.files?.[0]) {

              setFile(e.target.files[0])
            }
          }}

          className="
            w-full
            bg-[#07111f]
            border
            border-cyan-500/20
            rounded-xl
            p-4
            text-white
          "
        />



        <button

          onClick={uploadPDF}

          className="
            bg-cyan-500
            hover:bg-cyan-400
            text-black
            font-bold
            px-6
            py-3
            rounded-xl
          "
        >

          {

            loading

              ? "Processing PDF..."

              : "Upload PDF"
          }

        </button>



        {

          message && (

            <div className="text-cyan-300">

              {message}
            </div>
          )
        }

      </div>

    </div>
  )
}