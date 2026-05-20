def check_risk_alert(risk_score):

    if risk_score > 0.75:

        print("🚨 HIGH SYSTEMIC RISK ALERT")

    else:

        print("✅ Risk under control")