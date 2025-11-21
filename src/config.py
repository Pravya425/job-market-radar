import os
from pathlib import Path
from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

QUERY = os.getenv("QUERY", "data analyst")
DB_URL = os.getenv("DB_URL")
