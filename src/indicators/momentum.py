import pandas as pd
import pandas_ta as ta
from .base_indicator import BaseIndicator
from src.config import Config

class RSI(BaseIndicator):
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        df['rsi'] = df.ta.rsi(length=Config.RSI_PERIOD)
        return df
    
    def get_signal(self, df: pd.DataFrame) -> int:
        rsi = df['rsi'].iloc[-1]
        if rsi > 70:
            return -1
        elif rsi < 30:
            return 1
        return 0

class MACD(BaseIndicator):
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        macd = df.ta.macd(
            fast=Config.MACD_FAST,
            slow=Config.MACD_SLOW,
            signal=Config.MACD_SIGNAL
        )
        return pd.concat([df, macd], axis=1)
    
    def get_signal(self, df: pd.DataFrame) -> int:
        if df['MACD_12_26_9'].iloc[-1] > df['MACDs_12_26_9'].iloc[-1]:
            return 1
        elif df['MACD_12_26_9'].iloc[-1] < df['MACDs_12_26_9'].iloc[-1]:
            return -1
        return 0