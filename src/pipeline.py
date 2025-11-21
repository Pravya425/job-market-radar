from ingest_jobs import fetch_jobs
from load_db import upsert_raw_jobs
from extract_skills import extract_skills
from utils import insert_job_skills

def run_pipeline():
    df = fetch_jobs(limit=100)

    if df is None or df.empty:
        print("[pipeline] No jobs fetched. Nothing to insert.")
        return

    upsert_raw_jobs(df)

    for _, row in df.iterrows():
        skills = extract_skills(row.get("description"))
        insert_job_skills(row["id"], skills)

    print("[pipeline] Inserted jobs:", len(df))

if __name__ == "__main__":
    run_pipeline()
