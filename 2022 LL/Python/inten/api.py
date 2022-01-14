import requests
import json

API_KEY = '1dbd59baf29415c1ff9bb3d4bfa229f4'
lang = "kr"
city = "Daegu"
units = "metric"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang={lang}&units={units}"

result = requests.get(api)
print(type(result.text))

data = json.loads(result.text)

print(data)
print(data["weather"][0]["main"])