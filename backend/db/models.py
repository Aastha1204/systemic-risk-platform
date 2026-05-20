from sqlalchemy import Column, Integer, String, Float

from backend.db.database import Base


class RiskData(Base):

    __tablename__ = "risk_data"

    id = Column(Integer, primary_key=True)

    symbol = Column(String)

    price = Column(Float)

    sentiment = Column(Float)

    inflation = Column(Float)

    risk_score = Column(Float)