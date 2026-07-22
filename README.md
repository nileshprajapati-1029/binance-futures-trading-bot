# Binance Futures Testnet Trading Bot

A simple Python CLI application to place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M).

---

## Features

- Place MARKET Orders
- Place LIMIT Orders
- BUY & SELL Support
- Command Line Interface (argparse)
- Input Validation
- Logging
- Error Handling
- Binance Futures Testnet

---

## Project Structure

```
trading_bot/
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
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

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

**Windows (PowerShell)**

```powershell
.\.venv\Scripts\Activate
```

**Windows (Command Prompt)**

```cmd
.venv\Scripts\activate
```

### 5. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a `.env` File

Create a `.env` file in the project root and add your Binance Futures Testnet API credentials:

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
SECRET_KEY=YOUR_BINANCE_TESTNET_SECRET_KEY
```

### 7. Run the Application

#### Place a MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

#### Place a LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 130000
```



### Clone repository

```bash
git clone <repository-url>
```

### Open project

```bash
cd trading_bot
```

### Create virtual environment

```bash
python -m venv .venv
```

### Activate

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```
API_KEY=
SECRET_KEY=
```

---

## Run MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

---

## Run LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 130000
```

---

## Logs

Logs are stored in:

```
logs/trading_bot.log
```

---

## Assumptions

- Binance Futures Testnet account is configured.
- API Keys are valid.
- Internet connection is available.
- Testnet endpoint is used.

---

## Technologies Used

- Python 3.11
- python-binance
- argparse
- python-dotenv
- logging

---

## Author

Nilesh Prajapati

## Requirements

- Python 3.11 or later
- Binance Futures Testnet Account
- Binance Testnet API Key & Secret
- Internet Connection

## Assumptions

- The application uses Binance Futures Testnet.
- API keys are stored securely in a `.env` file.
- The user has sufficient test funds in the Binance Testnet account.
- The internet connection is active while placing orders.
