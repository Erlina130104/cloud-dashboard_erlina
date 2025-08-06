import requests
import random
import time

BACKEND_URL = "http://backend:5000/data"  # container name in docker-compose

while True:
    temperature = round(random.uniform(20.0, 35.0), 2)
    humidity = round(random.uniform(40.0, 80.0), 2)
    try:
        requests.post(BACKEND_URL, json={
            "temperature": temperature,
            "humidity": humidity
        })
        print(f"Sent -> Temperature: {temperature}, Humidity: {humidity}")
    except Exception as e:
        print("Error sending data:", e)
    time.sleep(3)


# ==== backend/app.py ====
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

latest_data = {"temperature": 0.0, "humidity": 0.0}

@app.route("/data", methods=["POST"])
def receive_data():
    global latest_data
    data = request.get_json()
    latest_data = data
    return {"message": "Data received"}, 200

@app.route("/data", methods=["GET"])
def send_data():
    return jsonify(latest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)