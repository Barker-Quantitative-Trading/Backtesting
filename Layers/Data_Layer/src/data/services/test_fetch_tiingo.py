from fetch_tiingo import fetch_candle, fetch_asset
import json


print("without end date")
print(fetch_candle("AAPL", "2025/8/01"))

print("With end date")
print(fetch_candle("AAPL", "2020/10/01", "2020/10/02"))

print("asset Dictionary")
print(fetch_asset("AAPL"))
