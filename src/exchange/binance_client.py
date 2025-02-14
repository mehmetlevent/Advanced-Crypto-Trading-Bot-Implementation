from binance.client import Client
from binance.exceptions import BinanceAPIException
from src.config import Config
import pandas as pd
import asyncio
import logging

class BinanceClient:
    def __init__(self):
        self.client = Client(Config.BINANCE_API_KEY, Config.BINANCE_SECRET_KEY)
        self.logger = logging.getLogger(__name__)
        
    async def get_historical_data(self, symbol: str, interval: str, limit: int = 1000) -> pd.DataFrame:
        try:
            klines = self.client.futures_klines(symbol=symbol, interval=interval, limit=limit)
            df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                             'close_time', 'quote_volume', 'trades', 'taker_buy_base',
                                             'taker_buy_quote', 'ignore'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            for col in ['open', 'high', 'low', 'close', 'volume']:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            return df
        except BinanceAPIException as e:
            self.logger.error(f"Error fetching historical data: {e}")
            raise
            
    async def place_order(self, symbol: str, side: str, quantity: float, order_type: str = 'MARKET'):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
            return order
        except BinanceAPIException as e:
            self.logger.error(f"Error placing order: {e}")
            raise