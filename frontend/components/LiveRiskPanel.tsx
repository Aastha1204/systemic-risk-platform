"use client"

import { useEffect, useState } from "react"



export default function LiveRiskPanel() {

  const [riskData, setRiskData] = useState<any>(null)



  useEffect(() => {

    const fetchData = async () => {

      const res = await fetch(

        "http://localhost:8000/risk"
      )



      const data = await res.json()



      setRiskData(data)
    }



    fetchData()



    const interval = setInterval(

      fetchData,

      3000
    )



    return () => clearInterval(interval)

  }, [])



  if (!riskData) {

    return <div className="text-white">

      Loading...

    </div>
  }



  return (

    <div className="bg-black/40 rounded-2xl border border-cyan-500/10 p-6">

      <h2 className="text-cyan-400 text-xl font-bold mb-6">

        Live Risk Engine

      </h2>



      <div className="grid grid-cols-2 gap-6">

        <div>

          <p className="text-gray-400">

            Systemic Risk
          </p>

          <h1 className="text-5xl text-red-400 font-bold">

            {riskData.systemic_risk}
          </h1>

        </div>



        <div>

          <p className="text-gray-400">

            Volatility
          </p>

          <h1 className="text-5xl text-yellow-400 font-bold">

            {riskData.volatility}%
          </h1>

        </div>

      </div>

    </div>
  )
}