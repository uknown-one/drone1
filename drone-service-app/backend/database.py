import sqlite3

DB_NAME = "missions.db"


def init_db():
    """Create missions table if it doesn't exist"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS missions (
            id INTEGER PRIMARY KEY,
            location TEXT,
            mission_type TEXT,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_mission(mission_id, location, mission_type, status):
    """Insert a mission into the database"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO missions (id, location, mission_type, status)
        VALUES (?, ?, ?, ?)
    ''', (mission_id, location, mission_type, status))
    conn.commit()
    conn.close()


def get_mission_by_id(mission_id):
    """Retrieve a mission by its ID"""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT * FROM missions WHERE id=?', (mission_id,))
    mission = c.fetchone()
    conn.close()
    return mission
