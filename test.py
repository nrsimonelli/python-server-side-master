import requests

# your server location
BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/nick")
# need to not be an object so use .json
print(response.json())