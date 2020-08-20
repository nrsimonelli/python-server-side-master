import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 10, "name": "nick", "views": 23567},
        {"likes": 33, "name": "joe", "views": 96034},
        {"likes": 25, "name": "devin", "views": 5567},
        {"likes": 90, "name": "david", "views": 1135},
        {"likes": 57, "name": "colleen", "views": 667567}]

for i in range(len(data)):
  response = requests.put(BASE + "video/" + str(i), data[i])
  print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/2")
print(response.json())