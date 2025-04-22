from fastapi import FastAPI
import requests
from typing import List

app = FastAPI()

BINANCE_API_URL = "https://api.binance.com/api/v3/klines"
BREAKOUT_THRESHOLD = 0.5 / 100  # 0.5% price movement
INTERVAL = "15m"  # Timeframe for 15-minute candles

# Function to fetch 15-minute candlesticks for a symbol
def get_candlestick_data(symbol: str, limit: int = 100) -> List[List]:
    params = {
        "symbol": symbol,
        "interval": INTERVAL,
        "limit": limit
    }
    response = requests.get(BINANCE_API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    return []

# Function to check for consolidation and breakout
def detect_breakout(symbol: str) -> List[str]:
    data = get_candlestick_data(symbol)
    if not data:
        return []

    # Extract closing prices from the candlestick data
    closing_prices = [float(item[4]) for item in data]  # Close price is at index 4

    # Define the range (max and min) for the recent consolidation
    highest_close = max(closing_prices)
    lowest_close = min(closing_prices)

    # Calculate the breakout threshold
    breakout_upper = highest_close * (1 + BREAKOUT_THRESHOLD)
    breakout_lower = lowest_close * (1 - BREAKOUT_THRESHOLD)

    # Check if the most recent close price is a breakout
    last_close = closing_prices[-1]
    if last_close >= breakout_upper or last_close <= breakout_lower:
        return [symbol]
    
    return []

# Endpoint to scan all Binance perpetual futures for breakouts
@app.get("/breakouts")
def get_breakouts():
    # List of symbols to scan (could be extended or dynamically fetched)
    symbols = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "BNBUSDT", "ADAUSDT"]  # Add more pairs if needed
    breakouts = []

    for symbol in symbols:
        breakout_symbols = detect_breakout(symbol)
        if breakout_symbols:
            breakouts.extend(breakout_symbols)
    
    return {"breakouts": breakouts}
