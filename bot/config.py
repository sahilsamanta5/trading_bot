import os

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = os.getenv("BINANCE_BASE_URL")

DEFAULT_TIME_IN_FORCE = "GTC"

VALID_SIDES = (
    "BUY",
    "SELL",
)

VALID_ORDER_TYPES = (
    "MARKET",
    "LIMIT",
)