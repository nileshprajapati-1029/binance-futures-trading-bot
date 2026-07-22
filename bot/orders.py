from bot.logging_config import logger
from binance.enums import *

from bot.client import client


def place_market_order(symbol, side, quantity):

    logger.info(
        f"MARKET ORDER REQUEST | Symbol={symbol} | Side={side} | Qty={quantity}"
    )

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=ORDER_TYPE_MARKET,
        quantity=quantity
    )

    logger.info(
        f"MARKET ORDER RESPONSE | OrderID={order['orderId']} | Status={order['status']}"
    )

    return order

def place_limit_order(symbol, side, quantity, price):

    logger.info(
        f"LIMIT ORDER REQUEST | Symbol={symbol} | Side={side} | Qty={quantity} | Price={price}"
    )

    order = client.futures_create_order(
        symbol=symbol,
        side=side,
        type=ORDER_TYPE_LIMIT,
        quantity=quantity,
        price=price,
        timeInForce=TIME_IN_FORCE_GTC
    )

    logger.info(
        f"LIMIT ORDER RESPONSE | OrderID={order['orderId']} | Status={order['status']}"
    )

    return order