import requests
import json

headers = {
    'Content-Type': 'application/json'
}
requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl/prices?startDate=2019-01-02&token=35943def70200e950c1dfa202bfcb2a4bb0b94a7", headers=headers)
data = requestResponse.json()  # this gives you a Python dictionary

# Option 1: Using json.dump()
with open("output.json", "w") as f:
    json.dump(data, f, indent=4)  # indent=4 makes it pretty-printed

# Option 2: If you have JSON as a string
#json_string = response.text  # this is the raw JSON string
#with open("output.json", "w") as f:
#    f.write(json_string)


# Requesting Instrament data
#-------------------------------------------------

requestResponse = requests.get("https://api.tiingo.com/tiingo/daily/aapl?token=35943def70200e950c1dfa202bfcb2a4bb0b94a7", headers=headers)
data2 = requestResponse.json()
print(data2)