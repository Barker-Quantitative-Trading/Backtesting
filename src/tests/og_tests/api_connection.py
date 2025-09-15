import requests
from dotenv import load_dotenv
import os

load_dotenv()  # automatically finds .env in cwd
token = os.getenv("TIINGO_TOKEN")
tokenHeader = os.getenv("TIINGO_TOKEN_HEADER")


print(token)
print(tokenHeader)

headers = {
        'Content-Type': 'application/json'
        }
requestResponse = requests.get(token,
                                    headers=headers)
print(requestResponse.json())



### Sending token through headers ###
headers = {
        "Content-Type": "application/json",
        "Authorization": tokenHeader
    }
requestResponse = requests.get("https://api.tiingo.com/api/test/",
                                    headers=headers)
print(requestResponse.json())
