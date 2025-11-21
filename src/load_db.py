from sqlalchemy import create_engine, text
from config import DB_URL

engine = create_engine(DB_URL)

# auto-create tables if missing (works for SQLite)
with engine.begin() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS raw_jobs (
          id TEXT PRIMARY KEY,
          title TEXT,
          company TEXT,
          location TEXT,
          salary_min REAL,
          salary_max REAL,
          created TEXT,
          description TEXT,
          source TEXT,
          fetched_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """))
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS job_skills (
          job_id TEXT,
          skill TEXT,
          PRIMARY KEY (job_id, skill)
        );
    """))

def upsert_raw_jobs(df):
    with engine.begin() as conn:
        for _, r in df.iterrows():
            conn.execute(text("""
                INSERT OR IGNORE INTO raw_jobs
                (id,title,company,location,salary_min,salary_max,created,description,source)
                VALUES (:id,:title,:company,:location,:salary_min,:salary_max,:created,:description,:source);
            """), r.to_dict())
