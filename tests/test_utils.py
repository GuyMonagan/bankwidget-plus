from datetime import datetime

import pandas as pd
import pytest

from bankwidget_plus.utils import filter_transactions_since_date


@pytest.fixture
def sample_df():
    data = [
        {"Дата операции": "07.01.2025", "Сумма платежа": 300.0},
        {"Дата операции": "08.01.2025", "Сумма платежа": 1000.0},
        {"Дата операции": "некорректная", "Сумма платежа": 2500.5},
    ]
    return pd.DataFrame(data)


def test_filter_transactions_since_date(sample_df):
    start_date = datetime(2025, 1, 1)
    filtered = filter_transactions_since_date(sample_df, start_date)
    assert len(filtered) == 2
    assert filtered["Сумма платежа"].sum() == 1300.0


def test_filter_ignores_invalid_dates(sample_df):
    start_date = datetime(2025, 1, 1)
    filtered = filter_transactions_since_date(sample_df, start_date)
    # Проверяем, что строка с "некорректная" не прошла
    assert "некорректная" not in filtered["Дата операции"].astype(str).tolist()
