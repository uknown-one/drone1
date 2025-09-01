import time
import threading
import uuid

# Dictionary to keep track of active missions
missions = {}

def start_mission(location: str, mission_type: str) -> str:
    """
    Starts a new drone mission and returns a mission_id.
    """
    mission_id = str(uuid.uuid4())
    missions[mission_id] = {
        "location": location,
        "mission_type": mission_type,
        "status": "in_progress"
    }

    # Run mission in background thread (simulate async drone work)
    thread = threading.Thread(target=_simulate_mission, args=(mission_id,))
    thread.daemon = True
    thread.start()

    return mission_id


def get_mission_status(mission_id: str) -> dict:
    """
    Returns status of a mission by mission_id.
    """
    return missions.get(mission_id, {"error": "Mission not found"})


def list_missions() -> dict:
    """
    Returns all missions (useful for debugging).
    """
    return missions


def _simulate_mission(mission_id: str):
    """
    Simulate a mission running in the background.
    Updates mission status over time.
    """
    if mission_id not in missions:
        return

    # Example simulation: drone takes 10 seconds to complete
    time.sleep(5)
    missions[mission_id]["status"] = "halfway"

    time.sleep(5)
    missions[mission_id]["status"] = "completed"
