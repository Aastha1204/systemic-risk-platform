export default function MarketFeed() {

  const news = [

    "Federal Reserve warns about liquidity stress.",

    "Goldman Sachs exposure increased.",

    "Banking volatility spikes globally.",

    "Systemic contagion probability elevated."
  ]



  return (

    <div className="bg-black/40 rounded-2xl border border-white/10 p-6">

      <h2 className="text-cyan-400 text-xl font-bold mb-6">

        Live Market Feed

      </h2>



      <div className="space-y-4">

        {news.map((item, i) => (

          <div

            key={i}

            className="text-gray-300 border-b border-white/10 pb-2"
          >

            {item}

          </div>
        ))}

      </div>

    </div>
  )
}