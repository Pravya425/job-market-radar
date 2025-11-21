<!-- UPDATED: Nov 21, 2025 -->

# 📊 Job Market Radar

### **Real-Time Job Market Analytics Pipeline + Skill Extraction + Dashboard**

This project builds a full **end-to-end ETL + analytics system** that collects real job postings from a live API, extracts skills, stores structured results in a database, and visualizes insights through a Streamlit dashboard.

It demonstrates practical data engineering + data analytics skills used in real-world jobs.



# 🚀 Features

### ✓ **Real-time job ingestion**

* Fetches job postings from the **Arbeitnow Job Board API**
* Flexible keyword matching using `.env` (e.g., `data`, `analyst`, `analytics`)
* No API key required

### ✓ **Database storage**

Supports:

* **SQLite** (default — zero setup)
* **PostgreSQL** (production mode)

Tables created:

* `raw_jobs`
* `job_skills`

### ✓ **Skill extraction (NLP-lite)**

Extracts skills from job descriptions using:

* Keyword matching
* Custom skill dictionary
* Multi-label extraction

### ✓ **Interactive analytics dashboard**

Built using **Streamlit**:

* Top skills bar chart
* Latest job postings
* Auto-refresh capability

---

# 🏗️ Architecture

```
             +-----------------------+
             |    Arbeitnow API      |
             +-----------+-----------+
                         |
                         v
               +------------------+
               |  Ingest Jobs     |
               +------------------+
                         |
                         v
               +------------------+
               |   Pipeline.py    |
               | - clean data     |
               | - extract skills |
               | - store in DB    |
               +------------------+
                         |
                         v
        +---------------------------------+
        |   SQLite / PostgreSQL Database  |
        | raw_jobs       job_skills       |
        +---------------------------------+
                         |
                         v
              +-------------------------+
              |     Streamlit App       |
              +-------------------------+
```



# 🛠️ Setup Instructions (Step-by-Step)

## **1. Clone the project**

```bash
git clone https://github.com/Pravya425/job-market-radar.git
cd job-market-radar
```

## **2. Install dependencies**

```bash
pip3 install -r requirements.txt
```

## **3. Create `.env` file**

```
QUERY=data
DB_URL=sqlite:///jobs.db
```

For PostgreSQL:

```
DB_URL=postgresql://postgres:password@localhost:5432/jobs
```

## **4. Run the pipeline**

```bash
python3 src/pipeline.py
```

## **5. Launch the dashboard**

```bash
streamlit run dashboard/app.py
```



# 🎯 Example Screenshots

### **Top Skills Dashboard**

![Top Skills](screenshots/top_skills.png)

### **Latest Job Postings**

![Latest Jobs](screenshots/latest_jobs.png)



# 📌 Sample Data (Preview)

A sample of the ingested job postings is stored here:

📄 **`data/sample_jobs.csv`**

Example (first rows):

| Title              | Company     | Location  | Created    | Skills                    |
| ------------------ | ----------- | --------- | ---------- | ------------------------- |
| Investment Analyst | ABC Capital | Germany   | 2025-11-20 | Python, Finance, Excel    |
| Technical Writer   | XYZ GmbH    | Nuremberg | 2025-11-19 | Documentation, Confluence |
| Linux System Admin | Telekom AG  | Berlin    | 2025-11-19 | Linux, Networking         |

*(Actual values depend on API results.)*


# 📁 Project Structure

```
job-market-radar/
│
├── src/
│   ├── ingest_jobs.py
│   ├── extract_skills.py
│   ├── load_db.py
│   ├── pipeline.py
│   └── utils.py
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── skills_dict.json
│   └── sample_jobs.csv
│
├── screenshots/
│   ├── top_skills.png
│   └── latest_jobs.png
│
├── sql/
│   └── schema.sql
│
├── .env
├── requirements.txt
└── README.md
```



# 🚀 Future Enhancements

* Add Airflow/Prefect for scheduled ingestion
* Add sentiment analysis or TF-IDF skill clustering
* Add salary prediction model
* Add multiple job sources (Indeed, LinkedIn, RemoteOK)
* Deploy Streamlit on cloud



# 🙋 Author

**Pranay Reddy Tatiparti (Pravya425)**
Data Analyst | Data Engineer | AI & ML Practitioner


# ⭐ If this project helped you…

Leave a ⭐ on the repo — it helps visibility!