import {

  LayoutDashboard,

  Activity,

  AlertTriangle,

  BrainCircuit

} from "lucide-react"



interface SidebarProps {

  activeTab: string

  setActiveTab: React.Dispatch<React.SetStateAction<string>>
}



export default function Sidebar({

  activeTab,

  setActiveTab

}: SidebarProps) {

  return (

    <div className="w-64 min-h-screen bg-black/50 border-r border-white/10 backdrop-blur-xl p-4">

      <h2 className="text-cyan-400 text-2xl font-bold mb-10">

        Risk OS

      </h2>



      <div className="space-y-4">

        {/* DASHBOARD */}

        <button

          onClick={() => setActiveTab("dashboard")}

          className={`

            flex items-center gap-3

            w-full

            p-3

            rounded-xl

            transition-all duration-300

            ${

              activeTab === "dashboard"

                ? "bg-cyan-500/20 text-cyan-400 border border-cyan-500/30"

                : "text-white hover:bg-white/5"

            }

          `}
        >

          <LayoutDashboard size={20} />

          Dashboard

        </button>



        {/* LIVE RISK */}

        <button

          onClick={() => setActiveTab("risk")}

          className={`

            flex items-center gap-3

            w-full

            p-3

            rounded-xl

            transition-all duration-300

            ${

              activeTab === "risk"

                ? "bg-cyan-500/20 text-cyan-400 border border-cyan-500/30"

                : "text-white hover:bg-white/5"

            }

          `}
        >

          <Activity size={20} />

          Live Risk

        </button>



        {/* CONTAGION */}

        <button

          onClick={() => setActiveTab("contagion")}

          className={`

            flex items-center gap-3

            w-full

            p-3

            rounded-xl

            transition-all duration-300

            ${

              activeTab === "contagion"

                ? "bg-cyan-500/20 text-cyan-400 border border-cyan-500/30"

                : "text-white hover:bg-white/5"

            }

          `}
        >

          <AlertTriangle size={20} />

          Contagion

        </button>



        {/* AI ANALYST */}

        <button

          onClick={() => setActiveTab("analyst")}

          className={`

            flex items-center gap-3

            w-full

            p-3

            rounded-xl

            transition-all duration-300

            ${

              activeTab === "analyst"

                ? "bg-cyan-500/20 text-cyan-400 border border-cyan-500/30"

                : "text-white hover:bg-white/5"

            }

          `}
        >

          <BrainCircuit size={20} />

          AI Analyst

        </button>

      </div>

    </div>
  )
}