from flask import Flask, request, jsonify
from drone_control import start_mission, get_mission_status

app = Flask(__name__)

@app.route("/api/start_mission", methods=["POST"])
def api_start_mission():
    data = request.get_json()
    location = data.get("location")
    mission_type = data.get("mission_type")

    mission_id = start_mission(location, mission_type)
    return jsonify({"mission_id": mission_id, "status": "in_progress"})


@app.route("/api/mission_status/<mission_id>", methods=["GET"])
def api_mission_status(mission_id):
    status = get_mission_status(mission_id)
    return jsonify(status)
