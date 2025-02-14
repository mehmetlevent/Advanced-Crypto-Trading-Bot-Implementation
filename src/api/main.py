from fastapi import FastAPI, HTTPException
from src.models.base_model import SessionLocal
from src.models.trade import Trade
from typing import List
import uvicorn

app = FastAPI()

@app.get("/metrics")
async def get_metrics():
    db = SessionLocal()
    try:
        trades = db.query(Trade).all()
        total_pnl = sum(trade.pnl for trade in trades)
        win_rate = len([t for t in trades if t.pnl > 0]) / len(trades) if trades else 0
        return {
            "total_pnl": total_pnl,
            "win_rate": win_rate,
            "total_trades": len(trades)
        }
    finally:
        db.close()

# Add other API endpoints...