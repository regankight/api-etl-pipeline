# API → Clean → KPI Snapshot

Minimal ETL pipeline using a public API. Fetches, cleans, and logs KPI snapshots from real API data.

### 🧩 Flow Overview

1. **Fetch** – Grabs user data from JSONPlaceholder API  
2. **Clean** – Drops nulls, normalizes email, extracts full name  
3. **Snapshot** – Logs daily KPIs (user count, unique emails)

### 🔧 Stack

- Python (`requests`, `pandas`)
- CSV-based persistence (file-system snapshot)
- Modular, script-based orchestration

### 🚀 Run It

```bash
pip install pandas requests
python main.py
