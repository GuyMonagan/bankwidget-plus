import json

import pandas as pd
import pytest
from pandas import DataFrame

from bankwidget_plus.views import homepage_view


@pytest.fixture
def sample_df() -> DataFrame:
    data = [
        {"Дата операции": "2025-01-08", "Сумма платежа": 1000.0, "Описание": "Перевод в другом банке"},
        {"Дата операции": "некорректная", "Сумма платежа": 2500.5, "Описание": "Оплата товаров"},
        {"Дата операции": "2025-01-07", "Сумма платежа": 300.0, "Описание": "Кафе"},
    ]
    return pd.DataFrame(data)


@pytest.mark.parametrize(
    "date_input,expected_count,expected_amount,expected_descriptions,unexpected_descriptions",
    [
        (
            "2025-01-01 00:00:00",  # дата
            2,  # count
            1300.0,  # сумма
            ["Перевод", "Кафе"],  # ожидаемое
            ["Оплата товаров"],  # исключаемое
        ),
        (
            "2025-09-01 00:00:00",  # дата после всех транзакций
            0,
            0.0,
            [],
            ["Перевод", "Кафе", "Оплата товаров"],
        ),
    ],
)
def test_homepage_view_parametrized(
    sample_df: DataFrame,
    date_input: str,
    expected_count: int,
    expected_amount: float,
    expected_descriptions: list[str],
    unexpected_descriptions: list[str],
) -> None:
    result_json = homepage_view(sample_df, date_input)
    parsed = json.loads(result_json)

    assert parsed["count"] == expected_count
    assert parsed["total_amount"] == expected_amount

    for text in expected_descriptions:
        assert any(text in tx["Описание"] for tx in parsed["transactions"])

    for text in unexpected_descriptions:
        assert all(text not in tx["Описание"] for tx in parsed["transactions"])
