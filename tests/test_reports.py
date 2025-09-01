import json

import pandas as pd
import pytest

from bankwidget_plus.reports import expenses_by_weekday


@pytest.fixture
def df_for_weekdays() -> pd.DataFrame:
    data = [
        {"Дата операции": "2025-08-18", "Сумма платежа": 100.0},  # Пн
        {"Дата операции": "2025-08-19", "Сумма платежа": 200.0},  # Вт
        {"Дата операции": "2025-08-20", "Сумма платежа": 300.0},  # Ср
        {"Дата операции": "2025-08-21", "Сумма платежа": 400.0},  # Чт
        {"Дата операции": "2025-08-22", "Сумма платежа": 500.0},  # Пт
    ]
    return pd.DataFrame(data)


@pytest.mark.parametrize(
    "start_date,expected_days",
    [
        (
            "2025-08-17",
            {"Понедельник": 100.0, "Вторник": 200.0, "Среда": 300.0, "Четверг": 400.0, "Пятница": 500.0},  # Все видим
        ),
        ("2025-08-20", {"Среда": 300.0, "Четверг": 400.0, "Пятница": 500.0}),  # Только последние 3 дня
        ("2025-08-23", {}),  # Ничего нет
    ],
)
def test_expenses_by_weekday_parametrized(
    df_for_weekdays: pd.DataFrame, start_date: str, expected_days: dict[str, float]
) -> None:
    result_json = expenses_by_weekday(df_for_weekdays, start_date)
    result = json.loads(result_json)

    for day, amount in expected_days.items():
        assert day in result
        assert result[day] == amount

    # Проверим, что лишние дни не попали
    for day in {"Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"} - set(
        expected_days
    ):
        assert day not in result
