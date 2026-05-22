"use client"

import { useEffect, useState } from "react"



export default function MetricsCards() {

  const [data, setData] = useState<any>(null)



  useEffect(() => {

    fetch("http://127.0.0.1:8000/risk")

      .then((res) => res.json())

      .then((data) => setData(data))

  }, [])



  if (!data) {

    return <div className="text-white">

      Loading...

    </div>
  }



  const cards = [

    {

      title: "Systemic Risk",

      value: data.systemic_risk,

      color: "text-red-400"
    },

    {

      title: "Volatility",

      value: `${data.volatility}%`,

      color: "text-yellow-400"
    },

    {

      title: "Liquidity",

      value: data.liquidity,

      color: "text-orange-400"
    },

    {

      title: "Contagion",

      value: data.contagion,

      color: "text-red-500"
    }

  ]



  return (

    <div className="grid grid-cols-4 gap-4">

      {cards.map((card) => (

        <div

          key={card.title}

          className="bg-black/40 border border-white/10 rounded-2xl p-5"
        >

          <p className="text-gray-400 text-sm">

            {card.title}

          </p>

          <h2 className={`text-3xl font-bold ${card.color}`}>

            {card.value}

          </h2>

        </div>
      ))}

    </div>
  )
}