from prometheus_client import start_http_server

from prometheus_client import Gauge

import random

import time


# CREATE METRIC

risk_metric = Gauge(

    "systemic_risk_score",

    "Current systemic risk score"
)


# START SERVER

start_http_server(8001)

print("✅ Prometheus Metrics Running on Port 8001")


while True:

    risk = round(

        random.uniform(0, 1),

        2
    )


    # UPDATE METRIC

    risk_metric.set(risk)


    print(

        f"📊 Current Risk Score: {risk}"
    )


    time.sleep(5)