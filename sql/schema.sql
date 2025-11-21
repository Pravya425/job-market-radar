CREATE TABLE IF NOT EXISTS raw_jobs (
  id TEXT PRIMARY KEY,
  title TEXT,
  company TEXT,
  location TEXT,
  salary_min REAL,
  salary_max REAL,
  created TIMESTAMP,
  description TEXT,
  source TEXT,
  fetched_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS job_skills (
  job_id TEXT REFERENCES raw_jobs(id),
  skill TEXT,
  PRIMARY KEY (job_id, skill)
);
