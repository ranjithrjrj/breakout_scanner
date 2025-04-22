# Binance Breakout Scanner

This is a simple FastAPI-based application that scans Binance perpetual futures for breakout opportunities. It checks for breakouts from consolidation patterns based on the last 15-minute candlesticks. If the price moves more than 0.5% above or below the recent consolidation range, it is considered a breakout.

## Features

- Scans Binance perpetual futures symbols for breakouts.
- Uses 15-minute candlesticks to detect consolidation patterns.
- Identifies breakouts based on a 0.5% price movement above or below the consolidation range.
- Exposes a `/breakouts` endpoint to view the current breakout symbols.

## Prerequisites

- Python 3.7+ (for local development)
- FastAPI (for backend)
- Uvicorn (ASGI server)
- Binance API (public market data)
- Render for hosting (or any server for deployment)

## Installation

### 1. Clone the repository

Clone this repository to your local machine or deploy it directly using Render or any cloud platform.

```bash
git clone https://github.com/your-username/binance-breakout-scanner.git
cd binance-breakout-scanner
