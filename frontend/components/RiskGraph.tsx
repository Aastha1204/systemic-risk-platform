"use client"

import dynamic from "next/dynamic"

import { useEffect, useState } from "react"



const ForceGraph3D = dynamic(

  () => import("react-force-graph-3d"),

  {

    ssr: false
  }
)



export default function RiskGraph() {

  const [risk, setRisk] = useState(0.5)



  useEffect(() => {

    const ws = new WebSocket(

      "ws://127.0.0.1:8000/ws"
    )



    ws.onmessage = (event) => {

      const data = JSON.parse(event.data)

      setRisk(data.risk)
    }



    return () => ws.close()

  }, [])



  const graphData = {

    nodes: [

      {

        id: "JPMorgan",

        x: -60,

        y: 20,

        z: 0,

        val: 18
      },

      {

        id: "Goldman Sachs",

        x: 60,

        y: 20,

        z: 0,

        val: 14
      },

      {

        id: "Bank of America",

        x: -40,

        y: -50,

        z: 0,

        val: 12
      },

      {

        id: "Citibank",

        x: 40,

        y: -50,

        z: 0,

        val: 11
      }

    ],



    links: [

      {

        source: "JPMorgan",

        target: "Goldman Sachs"
      },

      {

        source: "JPMorgan",

        target: "Bank of America"
      },

      {

        source: "Goldman Sachs",

        target: "Citibank"
      },

      {

        source: "Bank of America",

        target: "Citibank"
      }

    ]
  }



  return (

    <div className="h-[500px] bg-black/40 rounded-2xl border border-cyan-500/10 overflow-hidden relative">

      <div className="absolute z-10 p-4">

        <h2 className="text-cyan-400 font-bold text-lg">

          Live Contagion Network

        </h2>

        <p className="text-gray-400 text-sm">

          Real-time systemic risk propagation

        </p>

      </div>



      <ForceGraph3D

        graphData={graphData}



        backgroundColor="#050816"



        nodeAutoColorBy="id"



        nodeLabel="id"



        nodeOpacity={0.95}



        nodeResolution={24}



        linkColor={() =>

          risk > 0.7

            ? "#ff004c"

            : "#00ffff"
        }



        linkWidth={2}



        linkOpacity={0.7}



        linkDirectionalParticles={

          risk > 0.7 ? 10 : 4
        }



        linkDirectionalParticleWidth={4}



        linkDirectionalParticleSpeed={0.004}



        cooldownTicks={0}



        d3AlphaDecay={0.01}



        d3VelocityDecay={0.1}



        enableNodeDrag={false}

      />

    </div>
  )
}