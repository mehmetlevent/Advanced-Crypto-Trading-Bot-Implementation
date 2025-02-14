from datetime import datetime, timedelta
import pytz

def get_timestamp(timeframe: str = '1m') -> int:
    """Get timestamp for a given timeframe"""
    timeframe_minutes = {
        '1m': 1,
        '5m': 5,
        '15m': 15,
        '1h': 60
    }
    minutes = timeframe_minutes.get(timeframe, 1)
    dt = datetime.now(pytz.UTC)
    dt = dt - timedelta(minutes=dt.minute % minutes,
                       seconds=dt.second,
                       microseconds=dt.microsecond)
    return int(dt.timestamp() * 1000)