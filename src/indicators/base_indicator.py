from abc import ABC, abstractmethod
import pandas as pd

class BaseIndicator(ABC):
    @abstractmethod
    def calculate(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate the indicator values"""
        pass
        
    @abstractmethod
    def get_signal(self, df: pd.DataFrame) -> int:
        """Generate trading signal (-1: Sell, 0: Neutral, 1: Buy)"""
        pass