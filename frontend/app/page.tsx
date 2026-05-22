"use client"

import { useState } from "react"

import Navbar from "../components/Navbar"
import Sidebar from "../components/Sidebar"
import DashboardContent from "../components/DashboardContent"
import PDFUpload from "@/components/PDFUpload"



export default function Home() {

  const [activeTab, setActiveTab] = useState(

    "dashboard"
  )



  return (

    <main className="bg-[#050816] min-h-screen text-white">

      {/* NAVBAR */}

      <Navbar />



      {/* MAIN LAYOUT */}

      <div className="flex flex-col lg:flex-row">

        {/* SIDEBAR */}

        <Sidebar

          activeTab={activeTab}

          setActiveTab={setActiveTab}

        />



        {/* CONTENT */}

        <div className="flex-1 p-4 lg:p-6 overflow-y-auto space-y-6">

          {/* DASHBOARD */}

          <DashboardContent

            activeTab={activeTab}

          />



          {/* PDF PANEL */}

          <PDFUpload />

        </div>

      </div>

    </main>
  )
}