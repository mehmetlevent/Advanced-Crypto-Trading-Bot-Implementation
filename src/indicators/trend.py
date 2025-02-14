import pandas as pd
import pandas_ta as ta
from .base_indicator import BaseIndicator
from src.config import Config

class Supertrend(BaseIndicator):
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        st = df.ta.supertrend(
            length=Config.SUPERTREND_PERIOD,
            multiplier=Config.SUPERTREND_MULTIPLIER
        )
        return pd.concat([df, st], axis=1)
    
    def get_signal(self, df: pd.DataFrame) -> int:
        if df['SUPERTd_10_3.0'].iloc[-1] == 1:
            return 1
        elif df['SUPERTd_10_3.0'].iloc[-1] == -1:
            return -1
        return 0

class TillsonT3(BaseIndicator):
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        df['t3'] = df.ta.t3(length=8)
        return df
    
    def get_signal(self, df: pd.DataFrame) -> int:
        if df['t3'].iloc[-1] > df['t3'].iloc[-2]:
            return 1
        elif df['t3'].iloc[-1] < df['t3'].iloc[-2]:
            return -1
        return 0