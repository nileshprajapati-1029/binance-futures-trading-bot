from bot.logging_config import logger

import argparse
from requests.exceptions import ConnectionError
from binance.exceptions import BinanceAPIException

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading Symbol")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("=" * 60)
        print("ORDER REQUEST")
        print("=" * 60)

        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if price:
            print(f"Price    : {price}")

        print("=" * 60)

        if order_type == "MARKET":

            order = place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            order = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\n✅ ORDER SUCCESS\n")

        print(f"Order ID       : {order['orderId']}")
        print(f"Status         : {order['status']}")
        print(f"Executed Qty   : {order['executedQty']}")

    except ValueError as e:
      logger.error(f"Validation Error: {e}")
      print("\n❌ Validation Error")
      print(e)

    except BinanceAPIException as e:
      logger.error(f"Binance API Error: {e}")
      print("\n❌ Binance API Error")
      print(e)

    except ConnectionError as e:
      logger.error(f"Network Error: {e}")
      print("\n❌ Network Error")
      print("Please check your internet connection.")

    except Exception as e:
      logger.error(f"Unexpected Error: {e}")
      print("\n❌ Unexpected Error")
      print(e)


if __name__ == "__main__":
    main()