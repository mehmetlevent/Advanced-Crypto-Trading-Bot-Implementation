import pandas as pd
import pandas_ta as ta
from .base_indicator import BaseIndicator

class VolumeProfile(BaseIndicator):
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        df['volume_ema'] = df.ta.ema(df['volume'], length=20)
        df['volume_ratio'] = df['volume'] / df['volume_ema']
        return df
    
    def get_signal(self, df: pd.DataFrame) -> int:
        if df['volume_ratio'].iloc[-1] > 2.0:
            if df['close'].iloc[-1] > df['open'].iloc[-1]:
                return 1
            else:
                return -1
        return 0