from datetime import datetime

import pandas as pd


def filter_transactions_since_date(df: pd.DataFrame, date: datetime) -> pd.DataFrame:
    """
    Фильтрует транзакции, совершённые после указанной даты.

    Преобразует значения в столбце "Дата операции" к типу datetime
    с учётом формата DD-MM-YYYY, затем отбирает строки, где дата
    операции не ранее заданной.
    """
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], errors="coerce", dayfirst=True)
    return df[df["Дата операции"] >= date].copy()
