from loguru import logger

def setup_logger():
    logger.add(
        "logs/trading_bot.log",
        rotation="1 day",
        retention="7 days",
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )
    
    return logger