import pandas as pd
from datetime import datetime

def filter_transactions_since_date(df: pd.DataFrame, date: datetime) -> pd.DataFrame:
    df["Дата операции"] = pd.to_datetime(
        df["Дата операции"],
        errors="coerce",
        dayfirst=True
    )
    return df[df["Дата операции"] >= date].copy()
