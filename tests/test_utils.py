from datetime import datetime

import pandas as pd
import pytest

from bankwidget_plus.utils import filter_transactions_since_date


@pytest.fixture
def sample_df() -> pd.DataFrame:
    data = [
        {"Дата операции": "2025-07-01", "Сумма платежа": 300.0},  # ✅ 1 июля
        {"Дата операции": "2025-08-01", "Сумма платежа": 1000.0},  # ✅ 1 августа
        {"Дата операции": "некорректная", "Сумма платежа": 2500.5},
    ]
    return pd.DataFrame(data)


@pytest.mark.parametrize(
    "start_date,expected_count,expected_sum",
    [
        (datetime(2025, 1, 1), 2, 1300.0),
        (datetime(2025, 1, 8), 1, 1000.0),
        (datetime(2025, 2, 1), 0, 0.0),
    ],
)
def test_filter_transactions_since_date(
    sample_df: pd.DataFrame,
    start_date: datetime,
    expected_count: int,
    expected_sum: float,
) -> None:
    filtered = filter_transactions_since_date(sample_df, start_date)
    assert len(filtered) == expected_count
    assert filtered["Сумма платежа"].sum() == expected_sum


def test_filter_ignores_invalid_dates(sample_df: pd.DataFrame) -> None:
    start_date = datetime(2025, 1, 1)
    filtered = filter_transactions_since_date(sample_df, start_date)
    assert "некорректная" not in filtered["Дата операции"].astype(str).tolist()
