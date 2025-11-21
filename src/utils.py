from sqlalchemy import text
from load_db import engine

def insert_job_skills(job_id, skills):
    with engine.begin() as conn:
        for s in skills:
            conn.execute(text("""
                INSERT INTO job_skills (job_id, skill)
                VALUES (:job_id, :skill)
                ON CONFLICT DO NOTHING;
            """), {"job_id": job_id, "skill": s})
