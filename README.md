# Binance Futures Trading Bot

A modular Python-based trading bot for **Binance USDⓈ-M Futures** with support for **Market** and **Limit** orders, comprehensive logging, environment-based configuration, and a clean, extensible architecture.

> **Note:** This project is intended for educational purposes and automated trading experimentation. Always test thoroughly on the Binance Futures Testnet or Demo environment before using any real funds.

---

# Features

* Binance USDⓈ-M Futures integration
* Market Orders
* Limit Orders
* Testnet/Demo Trading support
* Environment variable configuration
* Structured logging
* Modular project architecture
* Simple CLI interface
* Easy to extend with new order types

---

# Project Structure

```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── config.py
│   ├── logging_config.py
│   ├── orders.py
│   └── __init__.py
│
├── logs/
│
├── cli.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```

---

# Requirements

* Python 3.10+
* Binance Futures Testnet or Demo API Key
* pip

---

# Installation

Clone the repository:

```bash
git clone https://github.com/sahilsamanta5/trading_bot.git

cd binance-futures-trading-bot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_API_SECRET
BINANCE_BASE_URL=https://testnet.binancefuture.com/fapi
```

Never commit your `.env` file to version control.

---

# Usage

## Market Order

```bash
python cli.py \
    --symbol BTCUSDT \
    --side BUY \
    --type MARKET \
    --quantity 0.001
```

Example:

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## Limit Order

```bash
python cli.py \
    --symbol BTCUSDT \
    --side BUY \
    --type LIMIT \
    --quantity 0.001 \
    --price 100000
```

Example:

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 10000
```

---

# Sample Output

```text
========== ORDER REQUEST ==========
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001
===================================

Order placed successfully!

========== ORDER RESPONSE ==========
Order ID      : 20869770695
Status        : FILLED
Executed Qty  : 0.0010
====================================
```

---

# Logging

The bot logs every important event, including:

* Connection status
* API requests
* API responses
* Order execution
* Errors
* Exceptions

Example:

```text
Connected to Binance Futures Testnet

API Request:
{
    ...
}

API Response:
{
    ...
}

MARKET ORDER COMPLETED
```

---

# Supported Order Types

| Order         | Supported  |
| ------------- | ---------- |
| Market        | ✅          |
| Limit         | ✅          |
| Stop Market   | 🚧 Planned |
| Stop Limit    | 🚧 Planned |
| Take Profit   | 🚧 Planned |
| Trailing Stop | 🚧 Planned |

---

# Roadmap

* [ ] Stop Loss Orders
* [ ] Take Profit Orders
* [ ] Trailing Stop Orders
* [ ] Position Management
* [ ] Open Orders
* [ ] Order Cancellation
* [ ] Account Balance
* [ ] Leverage Configuration
* [ ] Risk Management
* [ ] Strategy Engine
* [ ] WebSocket Price Streaming
* [ ] Backtesting Support
* [ ] Docker Support
* [ ] Unit Tests

---

# Security

* Never expose your API Secret.
* Keep API credentials in environment variables.
* Use Testnet/Demo Trading while developing.
* Restrict API permissions to only what your application requires.
* Avoid enabling withdrawals for trading bots.

---

# Disclaimer

Trading cryptocurrencies involves significant financial risk. This software is provided **"as is"** without any warranty. The author is not responsible for any financial losses resulting from the use of this project.

---

# License

This project is licensed under the MIT License.

---

# Author

**Sahil Samanta**

Software Engineer

GitHub: https://github.com/sahilsamanta5

Portfolio: https://sahilsamanta.vercel.app/
