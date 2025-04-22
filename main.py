from fastapi import FastAPI
import asyncio
import time
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Breakout scanner is running in the background."}

async def breakout_scan():
    print(f"[{time.ctime()}] Running breakout scan...")
    # Call your actual breakout logic here
    # For now, just printing dummy output
    try:
        # Example request to Binance API (you'll replace this with your logic)
        response = requests.get("https://fapi.binance.com/fapi/v1/ticker/price")
        if response.status_code == 200:
            print("Breakout check complete.")
        else:
            print("Error from Binance API:", response.status_code)
    except Exception as e:
        print("Scan error:", e)

async def repeat_breakout_scan():
    while True:
        await breakout_scan()
        await asyncio.sleep(900)  # wait 15 minutes

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(repeat_breakout_scan())
