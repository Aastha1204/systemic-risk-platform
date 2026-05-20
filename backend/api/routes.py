from fastapi import APIRouter

router = APIRouter()


@router.get("/risk")

def get_risk():

    return {
        "risk_level": "HIGH",
         "risk_score": 0.83
    }