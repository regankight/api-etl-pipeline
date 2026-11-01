import os
import pandas as pd

def clean_data(df):
    df = df.dropna(subset=['id', 'email'])
    df['email'] = df['email'].str.lower().str.strip()
    df['full_name'] = df['name']
    df = df[['id', 'email', 'full_name']]
    os.makedirs('data', exist_ok=True)
    df.to_csv('data/clean_users.csv', index=False)
    return df
