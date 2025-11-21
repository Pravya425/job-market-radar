import requests
import pandas as pd
from config import QUERY

API_URL = "https://www.arbeitnow.com/api/job-board-api"

def fetch_jobs(limit=100):
    # Always return a DataFrame, even if something goes wrong
    try:
        r = requests.get(API_URL, timeout=30)
        r.raise_for_status()
        data = r.json()

        q_words = QUERY.lower().split()  # e.g., ["data", "analyst"]

        rows = []
        for j in data.get("data", []):
            title = (j.get("title") or "")
            desc  = (j.get("description") or "")
            hay = (title + " " + desc).lower()

            if not any(w in hay for w in q_words):
                continue

            rows.append({
                "id": j.get("slug") or j.get("url"),
                "title": title,
                "company": j.get("company_name"),
                "location": j.get("location"),
                "salary_min": None,
                "salary_max": None,
                "created": j.get("created_at"),
                "description": desc,
                "source": "arbeitnow"
            })

            if len(rows) >= limit:
                break

        df = pd.DataFrame(rows)
        print(f"[fetch_jobs] matched jobs: {len(df)}")
        return df

    except Exception as e:
        print("[fetch_jobs] error:", e)
        return pd.DataFrame([])

if __name__ == "__main__":
    df = fetch_jobs()
    print(df.head())
