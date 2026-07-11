# bot/orders.py

from bot.client import BinanceClient
from bot.config import DEFAULT_TIME_IN_FORCE
from bot.logging_config import (
    trading_logger,
    market_logger,
    limit_logger,
)


class OrderService:
    """Service class for placing Binance Futures orders."""

    def __init__(self):
        self.client = BinanceClient()

    def place_market_order(self, symbol, side, quantity):
        """
        Place a MARKET order.

        Args:
            symbol (str): Trading symbol.
            side (str): BUY or SELL.
            quantity (float): Order quantity.

        Returns:
            dict: Binance API response.
        """

        market_logger.info(
            "MARKET ORDER | Symbol=%s Side=%s Quantity=%s",
            symbol,
            side,
            quantity,
        )

        response = self.client.place_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="MARKET",
            quantity=quantity,
            newOrderRespType="RESULT",
        )

        market_logger.info(
            "MARKET ORDER RESPONSE | OrderID=%s Status=%s ExecutedQty=%s",
            response.get("orderId"),
            response.get("status"),
            response.get("executedQty"),
        )

        trading_logger.info(
            "MARKET ORDER COMPLETED | OrderID=%s Status=%s",
            response.get("orderId"),
            response.get("status"),
        )

        return response

    def place_limit_order(self, symbol, side, quantity, price):
        """
        Place a LIMIT order.

        Args:
            symbol (str): Trading symbol.
            side (str): BUY or SELL.
            quantity (float): Order quantity.
            price (float): Limit price.

        Returns:
            dict: Binance API response.
        """

        limit_logger.info(
            "LIMIT ORDER | Symbol=%s Side=%s Quantity=%s Price=%s",
            symbol,
            side,
            quantity,
            price,
        )

        response = self.client.place_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce=DEFAULT_TIME_IN_FORCE,
            newOrderRespType="RESULT",
        )

        limit_logger.info(
            "LIMIT ORDER RESPONSE | OrderID=%s Status=%s ExecutedQty=%s",
            response.get("orderId"),
            response.get("status"),
            response.get("executedQty"),
        )

        trading_logger.info(
            "LIMIT ORDER COMPLETED | OrderID=%s Status=%s",
            response.get("orderId"),
            response.get("status"),
        )

        return response

    @staticmethod
    def format_response(response):
        """
        Format Binance order response for display.

        Args:
            response (dict): Raw Binance API response.

        Returns:
            dict: Simplified response.
        """

        return {
            "order_id": response.get("orderId"),
            "symbol": response.get("symbol"),
            "side": response.get("side"),
            "type": response.get("type"),
            "status": response.get("status"),
            "orig_qty": response.get("origQty"),
            "executed_qty": response.get("executedQty"),
            "price": response.get("price"),
            "avg_price": response.get("avgPrice") or "N/A",
        }