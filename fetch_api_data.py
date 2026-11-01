import os
import requests
import pandas as pd
import logging
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logger = logging.getLogger(__name__)


def fetch_api_data():
    url = "https://jsonplaceholder.typicode.com/users"

    session = requests.Session()
    retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    session.mount("https://", HTTPAdapter(max_retries=retries))

    r = session.get(url, timeout=10)
    r.raise_for_status()

    df = pd.DataFrame(r.json())
    logger.info("Fetched %d rows", len(df))
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/raw_users.csv", index=False)
    return df
