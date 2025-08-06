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
