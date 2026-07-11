# bot/client.py

import logging

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.config import API_KEY, API_SECRET, BASE_URL

logger = logging.getLogger(__name__)


class BinanceClient:
    """Wrapper around the Binance Futures Testnet client."""

    def __init__(self):
        if not API_KEY:
            raise ValueError("BINANCE_API_KEY is missing.")

        if not API_SECRET:
            raise ValueError("BINANCE_API_SECRET is missing.")

        if not BASE_URL:
            raise ValueError("BINANCE_BASE_URL is missing.")

        self.client = Client(API_KEY, API_SECRET)
        self.client.FUTURES_URL = BASE_URL

        logger.info("Connected to Binance Futures: %s", BASE_URL)

    def place_order(self, **order_data):
        """
        Place a futures order.

        Args:
            **order_data: Binance Futures order parameters.

        Returns:
            dict: Binance API response.
        """
        logger.info("Order Request: %s", order_data)

        try:
            response = self.client.futures_create_order(**order_data)

            logger.info("Order Response: %s", response)

            return response

        except BinanceAPIException as e:
            logger.error("Binance API Error: %s", e)
            raise

        except BinanceRequestException as e:
            logger.error("Binance Request Error: %s", e)
            raise

        except Exception as e:
            logger.exception("Unexpected Error: %s", e)
            raise

    def get_server_time(self):
        """
        Get Binance Futures server time.

        Returns:
            dict: Server time.
        """
        return self.client.futures_time()

    def get_mark_price(self, symbol):
        """
        Get current mark price for a symbol.

        Args:
            symbol (str): Trading pair (e.g., BTCUSDT).

        Returns:
            dict: Mark price information.
        """
        return self.client.futures_mark_price(symbol=symbol)

    def ping(self):
        """
        Check Binance Futures Testnet connectivity.

        Returns:
            bool: True if reachable, otherwise False.
        """
        try:
            self.client.futures_ping()
            logger.info("Binance Futures Testnet is reachable.")
            return True

        except BinanceRequestException as e:
            logger.error("Ping failed: %s", e)
            return False

        except Exception as e:
            logger.exception("Unexpected ping error: %s", e)
            return False