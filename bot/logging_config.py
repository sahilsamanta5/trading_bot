import logging
import os

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)


def get_logger(name, filename):
    """Create and return a configured logger."""

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(
        os.path.join(LOG_DIR, filename)
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


trading_logger = get_logger(
    "trading_bot",
    "trading_bot.log",
)

market_logger = get_logger(
    "market_order",
    "market_order.log",
)

limit_logger = get_logger(
    "limit_order",
    "limit_order.log",
)