import mlflow

import random


mlflow.set_experiment(

    "Systemic Risk Prediction"
)


with mlflow.start_run():

    risk_score = round(

        random.uniform(0, 1),

        2
    )


    mlflow.log_param(

        "model_type",

        "RiskGNN"
    )


    mlflow.log_metric(

        "risk_score",

        risk_score
    )


    print(

        f"Logged Risk Score: {risk_score}"
    )