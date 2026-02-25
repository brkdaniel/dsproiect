import requests

r = requests.get('https://api.open-meteo.com/v1/forecast?latitude=44.43&longitude=26.10&current_weather=true')

#200 - ok
print(f"Status Code: {r.status_code}")

print("Datele primite:")
print(r.json())