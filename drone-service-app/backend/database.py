import sqlite3
from config import Config

DB_PATH = Config.DATABASE

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS missions (
            mission_id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            mission_type TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_mission(mission_id, location, mission_type, status):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        'INSERT INTO missions (mission_id, location, mission_type, status) VALUES (?, ?, ?, ?)',
        (mission_id, location, mission_type, status)
    )
    conn.commit()
    conn.close()

def get_mission_by_id(mission_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM missions WHERE mission_id=?', (mission_id,))
    mission = cursor.fetchone()
    conn.close()
    return mission
