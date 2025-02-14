from decimal import Decimal
from typing import Union

def calculate_position_size(
    account_balance: float,
    risk_percentage: float,
    entry_price: float,
    stop_loss: float
) -> float:
    """Calculate position size based on risk parameters"""
    risk_amount = account_balance * (risk_percentage / 100)
    position_size = risk_amount / abs(entry_price - stop_loss)
    return position_size

def calculate_risk_reward_ratio(
    entry_price: float,
    take_profit: float,
    stop_loss: float
) -> float:
    """Calculate risk/reward ratio"""
    reward = abs(take_profit - entry_price)
    risk = abs(entry_price - stop_loss)
    return reward / risk if risk != 0 else 0