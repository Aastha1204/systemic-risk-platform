export default function SystemHealth() {

  const services = [

    "Kafka",

    "FastAPI",

    "Prometheus",

    "Grafana",

    "AI Engine"
  ]



  return (

    <div className="bg-black/40 rounded-2xl border border-green-500/10 p-6">

      <h2 className="text-green-400 text-xl font-bold mb-6">

        System Health

      </h2>



      <div className="space-y-4">

        {services.map((service) => (

          <div

            key={service}

            className="flex justify-between"
          >

            <span className="text-white">

              {service}
            </span>

            <span className="text-green-400">

              ONLINE
            </span>

          </div>
        ))}

      </div>

    </div>
  )
}