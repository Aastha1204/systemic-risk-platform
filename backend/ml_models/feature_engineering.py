from kafka import KafkaConsumer
import json

from backend.db.database import SessionLocal
from backend.db.models import RiskData
from backend.alerts.alert_engine import check_risk_alert

market_consumer = KafkaConsumer(
    'market_prices',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='market-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

news_consumer = KafkaConsumer(
    'news_sentiment',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='news-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

macro_consumer = KafkaConsumer(
    'macro_indicators',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='macro-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("Feature Engineering Service Running...\n")

while True:

    market_msg = next(market_consumer)
    print("✅ Market topic received")

    news_msg = next(news_consumer)
    print("✅ News topic received")

    macro_msg = next(macro_consumer)
    print("✅ Macro topic received")

    market_data = market_msg.value
  

    news_data = news_msg.value
   

    macro_data = macro_msg.value



    volatility_score = market_data['price'] / 220

    news_score = abs(news_data['sentiment'])

    inflation_score = macro_data['inflation'] / 10


    risk_score = (

        volatility_score * 0.4 +

        news_score * 0.3 +

        inflation_score * 0.3
    )
    db = SessionLocal()

    risk_entry = RiskData(

    symbol=market_data['symbol'],

    price=market_data['price'],

    sentiment=news_data['sentiment'],

    inflation=macro_data['inflation'],

    risk_score=risk_score
)

    db.add(risk_entry)

    db.commit()

    db.close()

    check_risk_alert(risk_score)

    print("\n===== SYSTEMIC RISK INDEX =====")

    print(f"Market Data: {market_data}")

    print(f"News Data: {news_data}")

    print(f"Macro Data: {macro_data}")

    print(f"\nCalculated Risk Score: {risk_score:.2f}")