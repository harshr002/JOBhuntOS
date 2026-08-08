import pandas as pd
from datetime import datetime


def export_apply_queue(jobs_df, limit=50):
    if jobs_df.empty:
        return None

    df = jobs_df.copy()

    df = df[df["status"] == "Pending"]

    df["final_score_num"] = pd.to_numeric(
        df["final_score"],
        errors="coerce"
    ).fillna(0)

    df = df.sort_values(
        by="final_score_num",
        ascending=False
    ).head(limit)

    file_name = f"data/apply_queue_{datetime.now().strftime('%Y_%m_%d')}.csv"

    df.to_csv(file_name, index=False)

    return file_name