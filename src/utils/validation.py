from decimal import Decimal
from typing import Union

def validate_price(price: Union[float, str, Decimal]) -> bool:
    """Validate if price is positive and not zero"""
    try:
        price_decimal = Decimal(str(price))
        return price_decimal > 0
    except:
        return False

def validate_quantity(quantity: Union[float, str, Decimal]) -> bool:
    """Validate if quantity is positive and not zero"""
    try:
        qty_decimal = Decimal(str(quantity))
        return qty_decimal > 0
    except:
        return False