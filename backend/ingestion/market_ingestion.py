import yfinance as yf
import pandas as pd
from backend.kafka.producer import producer


def fetch_market_data():

    stocks = ["JPM", "GS", "MS", "BAC"]

    all_data = []

    for stock in stocks:

        ticker = yf.Ticker(stock)

        hist = ticker.history(period="5d")

        latest = hist.iloc[-1]

        data = {
            "symbol": stock,
            "price": float(latest["Close"]),
            "volume": float(latest["Volume"])
        }

        all_data.append(data)
        producer.send("market_prices", data)

        print(f"Sent to Kafka: {data}")


    return all_data


if __name__ == "__main__":

    data = fetch_market_data()

    print(data)