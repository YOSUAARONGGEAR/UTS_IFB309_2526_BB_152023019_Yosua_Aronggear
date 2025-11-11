import requests, json

url = "http://127.0.0.1:5000/data"
resp = requests.get(url)
data = resp.json()

print("=== RAW JSON ===")
print(json.dumps(data, indent=2))

print("\n=== HASIL PARSING (DATA TERAKHIR) ===")
last = data["data"][-1]
print(f"Suhu       : {last['suhu']} °C")
print(f"Kelembapan : {last['humidity']} %")
print(f"Lux        : {last['lux']}")
print(f"Timestamp  : {last['timestamp']}")




