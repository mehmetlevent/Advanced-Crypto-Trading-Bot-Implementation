import pandas as pd
from typing import List
from .base_indicator import BaseIndicator
from . import Supertrend, TillsonT3, RSI, MACD, BollingerBands, ATR, VolumeProfile

class TechnicalIndicators:
    def __init__(self):
        self.indicators: List[BaseIndicator] = [
            Supertrend(),
            TillsonT3(),
            RSI(),
            MACD(),
            BollingerBands(),
            ATR(),
            VolumeProfile()
        ]
    
    def add_all_indicators(self, df: pd.DataFrame) -> pd.DataFrame:
        for indicator in self.indicators:
            df = indicator.calculate(df)
        return df
    
    def get_signals(self, df: pd.DataFrame) -> dict:
        signals = {}
        for indicator in self.indicators:
            indicator_name = indicator.__class__.__name__
            signals[indicator_name] = indicator.get_signal(df)
        return signals