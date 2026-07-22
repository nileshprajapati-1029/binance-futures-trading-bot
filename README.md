# Binance Futures Testnet Trading Bot

A Python-based Command Line Interface (CLI) application to place **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**. This project demonstrates secure API integration, input validation, logging, and error handling using a modular Python architecture.

---

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY & SELL Support
- Command Line Interface (CLI) using argparse
- Input Validation
- Error Handling
- Structured Logging
- Secure API Key Management using `.env`
- Binance Futures Testnet Integration

---

## Project Structure

```text
binance-futures-trading-bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env (Not included in GitHub)
```

---

## Requirements

- Python 3.11 or later
- Binance Futures Testnet Account
- Binance Futures Testnet API Key & Secret
- Internet Connection

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nileshprajapati-1029/binance-futures-trading-bot.git
```

### 2. Navigate to the Project Folder

```bash
cd binance-futures-trading-bot
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment

#### Windows (PowerShell)

```powershell
.\.venv\Scripts\Activate
```

#### Windows (Command Prompt)

```cmd
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
SECRET_KEY=YOUR_BINANCE_TESTNET_SECRET_KEY
```

> **Important:** Never upload your `.env` file or API credentials to GitHub.

---

## Usage

### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 130000
```

---

## Logs

All trading activities and errors are stored in:

```text
logs/trading_bot.log
```

---

## Assumptions

- Binance Futures Testnet account is configured.
- Valid API Key and Secret are available.
- API credentials are stored securely in the `.env` file.
- Internet connection is available.
- The application uses the Binance Futures Testnet endpoint.

---

## Technologies Used

- Python 3.11
- python-binance
- python-dotenv
- argparse
- logging
- Git
- GitHub

---

## Results

- Successfully connected to Binance Futures Testnet.
- Executed MARKET and LIMIT orders successfully.
- Validated user inputs before placing orders.
- Logged all order requests and responses.
- Implemented robust exception handling for API and network errors.

---

## Future Improvements

- Stop-Loss Orders
- Take-Profit Orders
- Order Cancellation
- Real-Time Market Data using WebSockets
- Trading Strategy Automation
- Docker Support
- Unit Testing

---

## Author

**Nilesh Prajapati**

GitHub: https://github.com/nileshprajapati-1029