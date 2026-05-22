"use client"

import { useState } from "react"



export default function StressTesting() {

  const [result, setResult] = useState("")



  const runStressTest = () => {

    setResult(

      "⚠ Simulated banking collapse increased contagion by 42%"
    )
  }



  return (

    <div className="bg-black/40 rounded-2xl border border-red-500/10 p-6">

      <h2 className="text-red-400 text-xl font-bold mb-6">

        Stress Testing Engine

      </h2>



      <button

        onClick={runStressTest}

        className="bg-red-500 px-6 py-3 rounded-lg font-bold"
      >

        Run Stress Test

      </button>



      <div className="mt-6 text-red-300">

        {result}

      </div>

    </div>
  )
}