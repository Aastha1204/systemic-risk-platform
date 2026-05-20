from kafka import KafkaProducer
import json
import random
import time


producer = KafkaProducer(

    bootstrap_servers='localhost:9092',

    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


while True:

    market_data = {

        "symbol": "JPM",

        "price": round(random.uniform(100, 300), 2),

        "volume": random.randint(100000, 500000)
    }


    news_data = {

        "headline": "Market crash fears rising",

        "sentiment": random.uniform(-1, 1)
    }


    macro_data = {

        "inflation": round(random.uniform(2, 10), 2),

        "interest_rate": round(random.uniform(1, 8), 2)
    }


    producer.send("market_prices", market_data)

    print("✅ Market sent")


    producer.send("news_sentiment", news_data)

    print("✅ News sent")


    producer.send("macro_indicators", macro_data)

    print("✅ Macro sent")


    producer.flush()


    print("Data sent to Kafka topics")

    time.sleep(3)