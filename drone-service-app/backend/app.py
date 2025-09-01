from flask import Flask, request, jsonify, render_template
import random
from database import init_db, add_mission, get_mission_by_id
from flask_cors import CORS
from config import Config   # <-- import Config

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.from_object(Config)  # <-- load settings
CORS(app)

# Initialize the database on startup
init_db()

# --------------------------
# FRONTEND ROUTE
# --------------------------
@app.route("/")
def home():
    return render_template("index.html")


# --------------------------
# API ROUTES
# --------------------------
@app.route('/api/start_mission', methods=['POST'])
def start_mission():
    mission_data = request.get_json()

    if not mission_data or "location" not in mission_data or "mission_type" not in mission_data:
        return jsonify({"error": "Missing required fields: location and mission_type"}), 400

    location = mission_data["location"]
    mission_type = mission_data["mission_type"]

    mission_id = random.randint(1000, 9999)
    status = "Mission Started"

    add_mission(mission_id, location, mission_type, status)

    return jsonify({
        "message": "Mission started successfully!",
        "mission_id": mission_id
    }), 201


@app.route('/api/mission_status/<int:mission_id>', methods=['GET'])
def mission_status(mission_id):
    mission = get_mission_by_id(mission_id)

    if mission:
        return jsonify({
            "mission_id": mission[0],
            "location": mission[1],
            "mission_type": mission[2],
            "status": mission[3]
        })
    else:
        return jsonify({"error": "Mission not found"}), 404


if __name__ == "__main__":
    app.run(
        debug=app.config["DEBUG"],
        host=app.config["HOST"],
        port=app.config["PORT"]
    )
