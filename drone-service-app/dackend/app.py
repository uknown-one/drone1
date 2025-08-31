from flask import Flask, request, jsonify
import random
from database import init_db, add_mission, get_mission_by_id

app = Flask(__name__)

# Initialize the database on startup
init_db()


@app.route('/api/start_mission', methods=['POST'])
def start_mission():
    """Start a new drone mission"""
    mission_data = request.get_json()

    # Validate input
    if not mission_data or "location" not in mission_data or "mission_type" not in mission_data:
        return jsonify({"error": "Missing required fields: location and mission_type"}), 400

    location = mission_data["location"]
    mission_type = mission_data["mission_type"]

    # Generate random mission ID (simulate)
    mission_id = random.randint(1000, 9999)
    status = "Mission Started"

    # Save to database
    add_mission(mission_id, location, mission_type, status)

    return jsonify({
        "message": "Mission started successfully!",
        "mission_id": mission_id
    }), 201


@app.route('/api/mission_status/<int:mission_id>', methods=['GET'])
def mission_status(mission_id):
    """Get the status of a mission by ID"""
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
    app.run(debug=True)
