# bot/client.py

from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.config import API_KEY, API_SECRET, BASE_URL
from bot.logging_config import trading_logger


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

        trading_logger.info(
            "Connected to Binance Futures Testnet (%s)",
            BASE_URL,
        )

    def place_order(self, **order_data):
        """
        Place a futures order.

        Args:
            **order_data: Binance Futures order parameters.

        Returns:
            dict: Binance API response.
        """

        trading_logger.info("API Request: %s", order_data)

        try:
            response = self.client.futures_create_order(**order_data)

            trading_logger.info("API Response: %s", response)

            return response

        except BinanceAPIException as e:
            trading_logger.error("Binance API Error: %s", e)
            raise

        except BinanceRequestException as e:
            trading_logger.error("Binance Request Error: %s", e)
            raise

        except Exception:
            trading_logger.exception("Unexpected error while placing order.")
            raise

    def get_server_time(self):
        """Return Binance Futures server time."""
        return self.client.futures_time()

    def get_mark_price(self, symbol):
        """
        Return current mark price.

        Args:
            symbol (str): Trading pair (e.g. BTCUSDT)

        Returns:
            dict
        """
        return self.client.futures_mark_price(symbol=symbol)

    def ping(self):
        """
        Check Binance Futures Testnet connectivity.

        Returns:
            bool
        """

        try:
            self.client.futures_ping()

            trading_logger.info(
                "Successfully connected to Binance Futures Testnet."
            )

            return True

        except BinanceRequestException as e:
            trading_logger.error("Ping failed: %s", e)
            return False

        except Exception:
            trading_logger.exception(
                "Unexpected error while connecting to Binance."
            )
            return False