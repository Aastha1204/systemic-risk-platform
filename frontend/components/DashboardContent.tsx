import LiveRiskPanel from "./LiveRiskPanel"

import ContagionPanel from "./ContagionPanel"

import AIChatPanel from "./AIChatPanel"

import AlertsPanel from "./AlertsPanel"

import MarketFeed from "./MarketFeed"

import SystemHealth from "./SystemHealth"

import StressTesting from "./StressTesting"



export default function DashboardContent({

  activeTab

}: {

  activeTab: string

}) {



  if (activeTab === "dashboard") {

    return (

      <div className="grid grid-cols-2 gap-6">

        <LiveRiskPanel />

        <SystemHealth />

        <ContagionPanel />

        <MarketFeed />

      </div>
    )
  }



  if (activeTab === "risk") {

    return (

      <div className="space-y-6">

        <LiveRiskPanel />

        <SystemHealth />

      </div>
    )
  }



  if (activeTab === "contagion") {

    return (

      <div className="space-y-6">

        <ContagionPanel />

      </div>
    )
  }



  if (activeTab === "analyst") {

    return (

      <div className="space-y-6">

        <AIChatPanel />

        <AlertsPanel />

        <StressTesting />

      </div>
    )
  }



  return null
}