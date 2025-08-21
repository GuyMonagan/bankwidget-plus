import json

import pandas as pd
import pytest

from bankwidget_plus.reports import expenses_by_weekday


@pytest.fixture
def df_for_weekdays():
    data = [
        {"Дата операции": "2025-08-18", "Сумма платежа": 100.0},  # Пн
        {"Дата операции": "2025-08-19", "Сумма платежа": 200.0},  # Вт
        {"Дата операции": "2025-08-20", "Сумма платежа": 300.0},  # Ср
        {"Дата операции": "2025-08-21", "Сумма платежа": 400.0},  # Чт
        {"Дата операции": "2025-08-22", "Сумма платежа": 500.0},  # Пт
    ]
    return pd.DataFrame(data)


def test_expenses_by_weekday(df_for_weekdays):
    result_json = expenses_by_weekday(df_for_weekdays)
    result = json.loads(result_json)

    assert result["Понедельник"] == 100.0
    assert result["Пятница"] == 500.0
    assert "Суббота" not in result
