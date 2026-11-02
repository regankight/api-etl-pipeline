import os
import pandas as pd
from datetime import datetime

from paths import OUTPUT_DIR


def snapshot_kpis(df):
    snapshot = {
        'timestamp': datetime.now(),
        'user_count': len(df),
        'unique_emails': df['email'].nunique()
    }
    out = pd.DataFrame([snapshot])
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    snapshot_path = os.path.join(OUTPUT_DIR, 'snapshot.csv')
    out.to_csv(
        snapshot_path,
        mode='a',
        header=not os.path.exists(snapshot_path),
        index=False
    )
