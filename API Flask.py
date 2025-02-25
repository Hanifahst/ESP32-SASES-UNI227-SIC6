from flask import Flask, request, jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["sensor_database"]
collection = db["sensor_data"]

app = Flask(__name__)

@app.route('/sensor', methods=[])
def post_sensor():
    data = request.get_json()
    return jsonify({"message": "Data received", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True)

def receive_data():
    data = request.json
    suhu = data.get('temperature')
    humidity = data.get('humidity')

    collection.insert_one({
        "temperature": suhu,
        "humidity": humidity,
        "timestamp": datetime.now()
    })

    return jsonify({"message": "Data stored"})
