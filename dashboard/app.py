import os
from pathlib import Path
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

# Load .env from project root
ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

DB_URL = os.getenv("DB_URL")

if not DB_URL:
    st.error("DB_URL is not set. Check your .env file in project root.")
    st.stop()

engine = create_engine(DB_URL)

st.title("📈 Job Market Radar – Real-Time Analytics")

# Always use an explicit connection for pandas + SQLAlchemy 2.x
with engine.connect() as conn:
    skills = pd.read_sql(text("""
        SELECT skill, COUNT(*) as cnt
        FROM job_skills
        GROUP BY skill
        ORDER BY cnt DESC;
    """), conn)

    jobs = pd.read_sql(text("""
        SELECT title, company, location, salary_min, salary_max, created
        FROM raw_jobs
        ORDER BY created DESC
        LIMIT 30;
    """), conn)

st.subheader("Top Skills Right Now")
if len(skills) == 0:
    st.info("No skills yet. Run `python3 src/pipeline.py` first.")
else:
    st.bar_chart(skills.set_index("skill"))

st.subheader("Latest Job Postings")
st.dataframe(jobs)
