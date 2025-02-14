from src.config import Config
import numpy as np

class PositionManager:
    def __init__(self, account_balance: float):
        self.account_balance = account_balance
        self.open_positions = {}
        
    def calculate_position_size(self, entry_price: float, stop_loss: float) -> float:
        risk_amount = self.account_balance * Config.POSITION_SIZE_PCT
        position_size = risk_amount / (entry_price - stop_loss)
        return position_size
        
    def calculate_dynamic_leverage(self, volatility: float) -> int:
        max_leverage = min(Config.MAX_LEVERAGE, int(1/volatility))
        return max_leverage
        
    # Add other position management methods...