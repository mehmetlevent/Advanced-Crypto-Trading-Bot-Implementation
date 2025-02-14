import pandas as pd
import pandas_ta as ta
from .base_indicator import BaseIndicator
from src.config import Config

class BollingerBands(BaseIndicator):
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        bb = df.ta.bbands(
            length=Config.BB_PERIOD,
            std=Config.BB_STD
        )
        return pd.concat([df, bb], axis=1)
    
    def get_signal(self, df: pd.DataFrame) -> int:
        if df['close'].iloc[-1] < df['BBL_20_2.0'].iloc[-1]:
            return 1
        elif df['close'].iloc[-1] > df['BBU_20_2.0'].iloc[-1]:
            return -1
        return 0

class ATR(BaseIndicator):
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        df['atr'] = df.ta.atr(length=Config.ATR_PERIOD)
        return df
    
    def get_signal(self, df: pd.DataFrame) -> float:
        return df['atr'].iloc[-1]