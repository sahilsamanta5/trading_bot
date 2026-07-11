# bot/validators.py

from bot.config import VALID_ORDER_TYPES, VALID_SIDES


def validate_symbol(symbol):
    """Validate trading symbol."""

    if not symbol:
        raise ValueError("Symbol is required.")

    symbol = symbol.strip().upper()

    if not symbol.isalnum():
        raise ValueError("Invalid trading symbol.")

    return symbol


def validate_side(side):
    """Validate order side."""

    if not side:
        raise ValueError("Side is required.")

    side = side.strip().upper()

    if side not in VALID_SIDES:
        raise ValueError(
            f"Side must be one of: {', '.join(VALID_SIDES)}"
        )

    return side


def validate_order_type(order_type):
    """Validate order type."""

    if not order_type:
        raise ValueError("Order type is required.")

    order_type = order_type.strip().upper()

    if order_type not in VALID_ORDER_TYPES:
        raise ValueError(
            f"Order type must be one of: {', '.join(VALID_ORDER_TYPES)}"
        )

    return order_type


def validate_quantity(quantity):
    """Validate quantity."""

    try:
        quantity = float(quantity)
    except (TypeError, ValueError):
        raise ValueError(
            "Quantity must be a valid number."
        ) from None

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity


def validate_price(price, order_type):
    """Validate price for LIMIT orders."""

    if order_type != "LIMIT":
        return None

    if price is None:
        raise ValueError(
            "Price is required for LIMIT orders."
        )

    if isinstance(price, str):
        price = price.strip()

    try:
        price = float(price)
    except (TypeError, ValueError):
        raise ValueError(
            "Price must be a valid number."
        ) from None

    if price <= 0:
        raise ValueError(
            "Price must be greater than zero."
        )

    return price