import os
import pandas as pd
from datetime import datetime


def snapshot_kpis(df):
    snapshot = {
        'timestamp': datetime.now(),
        'user_count': len(df),
        'unique_emails': df['email'].nunique()
    }
    out = pd.DataFrame([snapshot])
    os.makedirs('output', exist_ok=True)
    out.to_csv(
        'output/snapshot.csv',
        mode='a',
        header=not os.path.exists('output/snapshot.csv'),
        index=False
    )
