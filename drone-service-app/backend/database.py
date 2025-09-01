import sqlite3
from config import Config
from datetime import datetime, timedelta

DB_PATH = Config.DATABASE

# Define mission status timeline
STATUS_FLOW = ["Mission Started", "In Flight", "Completing", "Completed"]

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS missions (
            mission_id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            mission_type TEXT NOT NULL,
            status TEXT NOT NULL,
            start_time TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_mission(mission_id, location, mission_type, status):
    start_time = datetime.utcnow().isoformat()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO missions (mission_id, location, mission_type, status, start_time) VALUES (?, ?, ?, ?, ?)',
        (mission_id, location, mission_type, status, start_time)
    )
    conn.commit()
    conn.close()

def get_mission_by_id(mission_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM missions WHERE mission_id=?', (mission_id,))
    mission = cursor.fetchone()
    
    if mission:
        # Update status dynamically based on elapsed time
        mission_id, location, mission_type, status, start_time = mission
        start_dt = datetime.fromisoformat(start_time)
        elapsed = (datetime.utcnow() - start_dt).total_seconds()

        # Determine status based on elapsed time
        if elapsed < 5:
            status = STATUS_FLOW[0]  # Mission Started
        elif elapsed < 15:
            status = STATUS_FLOW[1]  # In Flight
        elif elapsed < 25:
            status = STATUS_FLOW[2]  # Completing
        else:
            status = STATUS_FLOW[3]  # Completed

        # Update status in database
        cursor.execute(
            'UPDATE missions SET status=? WHERE mission_id=?',
            (status, mission_id)
        )
        conn.commit()
        mission = (mission_id, location, mission_type, status)
    
    conn.close()
    return mission
