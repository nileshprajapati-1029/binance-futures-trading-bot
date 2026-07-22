# bot/validators.py

VALID_SIDES = ["BUY", "SELL"]
VALID_ORDER_TYPES = ["MARKET", "LIMIT"]


def validate_symbol(symbol):
    if not symbol:
        raise ValueError("Symbol is required.")

    return symbol.upper()


def validate_side(side):
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValueError(
            f"Invalid side '{side}'. Allowed values: BUY or SELL."
        )

    return side


def validate_order_type(order_type):
    order_type = order_type.upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Invalid order type '{order_type}'. Allowed values: MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity):
    quantity = float(quantity)

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0.")

    return quantity


def validate_price(price, order_type):
    if order_type.upper() == "LIMIT":

        if price is None:
            raise ValueError("Price is required for LIMIT orders.")

        price = float(price)

        if price <= 0:
            raise ValueError("Price must be greater than 0.")

        return price

    return None