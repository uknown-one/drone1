import os

class Config:
    # Flask settings
    DEBUG = True
    SECRET_KEY = os.environ.get("SECRET_KEY", "super-secret-key")

    # Database settings
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DATABASE = os.path.join(BASE_DIR, "..", "missions.db")

    # CORS settings
    CORS_HEADERS = "Content-Type"

    # Server settings
    HOST = "127.0.0.1"
    PORT = 5000
