from fetch_tiingo import fetch_ohlcv
import json

print("without end date")
print(fetch_ohlcv("AAPL", "2025/8/01"))
print("With end date")
print(fetch_ohlcv("AAPL", "2020/10/01", "2020/10/02"))

