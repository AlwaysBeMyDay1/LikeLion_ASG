import requests
import json

API_KEY = '1dbd59baf29415c1ff9bb3d4bfa229f4'
city = "Daegu"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

result = requests.get(api)
print(type(result.text))

data = json.loads(result.text)

print(type(data))