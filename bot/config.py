# bot/config.py

import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Binance API Configuration
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = os.getenv("BINANCE_BASE_URL")

# Default order configuration
DEFAULT_TIME_IN_FORCE = "GTC"

# Valid order sides
VALID_SIDES = (
    "BUY",
    "SELL",
)

# Valid order types
VALID_ORDER_TYPES = (
    "MARKET",
    "LIMIT",
)