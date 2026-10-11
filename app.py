from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "application": "Parking Reservation System",
        "status": "running",
        "message": "Welcome to the parking reservation service"
    })

@app.route("/slots")
def slots():
    return jsonify({
        "total_slots": 15,
        "reserved_slots": 5,
        "available_slots": 10
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)