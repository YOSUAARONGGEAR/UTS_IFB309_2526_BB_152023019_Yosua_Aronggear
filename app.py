from flask import Flask, jsonify
import random, datetime, pandas as pd

app = Flask(__name__)

def generate_sensor_data(n=5):
    data = []
    for i in range(n):
        suhu = round(random.uniform(27, 36), 2)
        humidity = round(random.uniform(55, 70), 2)
        lux = random.randint(100, 200)
        ts = datetime.datetime.now().isoformat()
        data.append({
            "id": i + 1,
            "suhu": suhu,
            "humidity": humidity,
            "lux": lux,
            "timestamp": ts
        })
    return pd.DataFrame(data)

@app.route('/data')
def get_data():
    df = generate_sensor_data(5)
    return jsonify({"data": df.to_dict(orient='records')})

if __name__ == "__main__":
    print("🌐 Server berjalan di http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)




