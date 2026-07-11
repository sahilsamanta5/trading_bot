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
        """Place a MARKET order."""

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

        response = self._normalize_response(response)

        if not response:
            raise RuntimeError("Binance returned an empty response.")

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
        """Place a LIMIT order."""

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

        response = self._normalize_response(response)

        if not response:
            raise RuntimeError("Binance returned an empty response.")

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
    def _normalize_response(response):
        """
        Convert SDK responses into a plain dictionary.
        """

        if response is None:
            return {}

        if isinstance(response, dict):
            return response

        # Binance SDK response object
        if hasattr(response, "data") and callable(response.data):
            return response.data()

        # Fallback
        if hasattr(response, "__dict__"):
            return dict(response.__dict__)

        return {}

    @staticmethod
    def format_response(response):
        """Format Binance order response."""

        response = response or {}

        return {
            "order_id": response.get("orderId"),
            "symbol": response.get("symbol"),
            "side": response.get("side"),
            "type": response.get("type"),
            "status": response.get("status"),
            "orig_qty": response.get("origQty"),
            "executed_qty": response.get("executedQty"),
            "price": response.get("price"),
            "avg_price": response.get("avgPrice"),
            "cum_quote": response.get("cumQuote"),
            "update_time": response.get("updateTime"),
        }