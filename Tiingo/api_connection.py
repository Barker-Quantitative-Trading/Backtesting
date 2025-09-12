import requests

with open(".env", "r") as f:
    token = f.readline().strip()
    tokenHeader = f.readline().strip()

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
