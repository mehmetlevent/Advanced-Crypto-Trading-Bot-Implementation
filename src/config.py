from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # API Configuration
    BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
    BINANCE_SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')
    
    # Trading Parameters
    MAX_POSITIONS = int(os.getenv('MAX_POSITIONS', 3))
    MAX_DAILY_LOSS = float(os.getenv('MAX_DAILY_LOSS', -1000))
    TARGET_DAILY_PROFIT = float(os.getenv('TARGET_DAILY_PROFIT', 1000))
    RISK_REWARD_RATIO = float(os.getenv('RISK_REWARD_RATIO', 3))
    MAX_LEVERAGE = int(os.getenv('MAX_LEVERAGE', 20))
    
    # Database
    DB_PATH = os.getenv('DB_PATH', 'sqlite:///trading_bot.db')
    
    # Timeframes
    TIMEFRAMES = ['1m', '5m', '15m', '1h']
    
    # Technical Indicators
    SUPERTREND_PERIOD = 10
    SUPERTREND_MULTIPLIER = 3
    RSI_PERIOD = 14
    MACD_FAST = 12
    MACD_SLOW = 26
    MACD_SIGNAL = 9
    BB_PERIOD = 20
    BB_STD = 2
    EMA_PERIODS = [9, 21, 55]
    ATR_PERIOD = 14
    
    # Risk Management
    POSITION_SIZE_PCT = 0.02  # 2% of account per trade
    MAX_DRAWDOWN_PCT = 0.15   # 15% max drawdown