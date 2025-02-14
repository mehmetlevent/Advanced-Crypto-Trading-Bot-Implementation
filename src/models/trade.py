from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from .base_model import Base

class Trade(Base):
    __tablename__ = "trades"
    
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    side = Column(String)
    entry_price = Column(Float)
    exit_price = Column(Float)
    quantity = Column(Float)
    pnl = Column(Float)
    entry_time = Column(DateTime, default=datetime.utcnow)
    exit_time = Column(DateTime)
    strategy = Column(String)
    timeframe = Column(String)