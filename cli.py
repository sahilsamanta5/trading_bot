# cli.py

import argparse

from bot.logging_config import trading_logger
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)",
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL",
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT",
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity",
    )

    parser.add_argument(
        "--price",
        help="Required for LIMIT orders",
    )

    args = parser.parse_args()

    try:
        # Validate user input
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        service = OrderService()

        if not service.client.ping():
            raise ConnectionError(
                "Unable to connect to Binance Futures Testnet."
            )

        # Print request summary
        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "LIMIT":
            print(f"Price    : {price}")

        print("===================================")

        trading_logger.info(
            "CLI Request | Symbol=%s Side=%s Type=%s Quantity=%s Price=%s",
            symbol,
            side,
            order_type,
            quantity,
            price,
        )

        # Place order
        if order_type == "MARKET":
            response = service.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
            )
        else:
            response = service.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price,
            )

        result = service.format_response(response)

        trading_logger.info(
            "CLI Response | OrderID=%s Status=%s ExecutedQty=%s AvgPrice=%s",
            result["order_id"],
            result["status"],
            result["executed_qty"],
            result["avg_price"],
        )

        print("\nOrder placed successfully!")

        print("\n========== ORDER RESPONSE ==========")
        print(f"Order ID      : {result['order_id']}")
        print(f"Status        : {result['status']}")
        print(f"Executed Qty  : {result['executed_qty']}")
        print(f"Average Price : {result['avg_price']}")
        print("====================================")

    except Exception as e:
        trading_logger.exception("Application Error")
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()