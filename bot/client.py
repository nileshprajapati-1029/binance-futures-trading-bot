from binance.client import Client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

client = Client(
    api_key=API_KEY,
    api_secret=SECRET_KEY,
    testnet=True
)