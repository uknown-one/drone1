

---

# Drone1

Is a simple full-stack application that allows users to request drone services (delivery, inspection, photography). Users can request drone missions, track progress, and visualize mission locations on an interactive map.

# The app includes:

* **Frontend** (HTML/CSS/JS) for submitting missions and viewing status.
* **Backend** (Flask) for handling mission requests.
* **Map Integration** (Leaflet.js) for visualizing mission locations.

---

## 🚀 Features

* Request a mission by entering location coordinates (latitude, longitude).
* Choose a mission type (Delivery, Inspection, Photography).
* View mission status.
* Display mission location on an interactive map.
* Store missions in a SQLite database.

---

## 📂 Project Structure

```
drone1/
|___ drone-service-app
|
├── backend/
│   ├── app.py              # Flask app entry point
│   ├── pipeline.py         # Orchestrates mission lifecycle with drone control
│   ├── drone_control.py    # Drone mission simulation logic
│   ├── config.py           # App configuration (settings, constants)
│   ├── requirements.txt    # Python dependencies
│   └── __init__.py
│
├── frontend/
│   ├── index.html          # UI with Leaflet map + form
│   ├── app.js              # Frontend logic (API calls, updates map)
│   └── styles.css          # Styling
│
└── README.md               # Project documentation

```

---

## ⚙️ Setup & Run

### 1. Clone the Repository

```bash
git clone https://github.com/uknown-one/drone1/
cd drone1
```

### 2. Setup Python Virtual Environment

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Backend Server

```bash
python app.py
```

Server will run at **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

### 5. Open Frontend

Open frontend/index.html directly in your browser OR serve it with Flask (optional).

The frontend communicates with Flask endpoints:

   /api/start_mission

  /api/mission_status

---

## 🛸 Future Improvements

* Live telemetry (battery, altitude, GPS) from real drones via SDK (e.g., DJI).
* WebSocket updates for mission tracking.
* Authentication (user accounts).
* Payment integration for commercial services.

---

## 📜 License

MIT License – free to use and modify.

---
