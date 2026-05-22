export default function AlertsPanel() {

  return (

    <div className="bg-red-500/10 border border-red-500/20 rounded-2xl p-5 backdrop-blur-xl">

      <h2 className="text-red-400 text-lg font-bold mb-4">

        Critical Alerts

      </h2>

      <div className="space-y-3 text-red-200">

        <p>

          🔴 Systemic risk crossed threshold.

        </p>

        <p>

          🔴 Banking network instability detected.

        </p>

      </div>

    </div>
  )
}