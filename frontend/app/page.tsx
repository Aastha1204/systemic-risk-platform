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

      {/* TOP NAVBAR */}

      <Navbar />



      <div className="flex flex-col lg:flex-row">

        {/* SIDEBAR */}

        <Sidebar

          activeTab={activeTab}

          setActiveTab={setActiveTab}

        />



        {/* MAIN CONTENT */}

        <div className="flex-1 p-4 lg:p-6 overflow-y-auto space-y-6">

          {/* DASHBOARD CONTENT */}

          <DashboardContent

            activeTab={activeTab}

          />



          {/* PDF UPLOAD PANEL */}

          <PDFUpload />

        </div>

      </div>

    </main>
  )
}