import os
import pandas as pd

from paths import DATA_DIR

def clean_data(df):
    df = df.dropna(subset=['id', 'email'])
    df['email'] = df['email'].str.lower().str.strip()
    df['full_name'] = df['name']
    df = df[['id', 'email', 'full_name']]
    os.makedirs(DATA_DIR, exist_ok=True)
    df.to_csv(os.path.join(DATA_DIR, 'clean_users.csv'), index=False)
    return df
