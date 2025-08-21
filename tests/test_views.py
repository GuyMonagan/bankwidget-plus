import pandas as pd
import pytest

from bankwidget_plus.views import homepage_view


@pytest.fixture
def sample_df():
    data = [
        {"Дата операции": "08.01.2025", "Сумма платежа": 1000.0, "Описание": "Перевод в другом банке"},
        {"Дата операции": "некорректная", "Сумма платежа": 2500.5, "Описание": "Оплата товаров"},
        {"Дата операции": "07.01.2025", "Сумма платежа": 300.0, "Описание": "Кафе"},
    ]
    return pd.DataFrame(data)


def test_homepage_view_filters_correctly(sample_df):
    result_json = homepage_view(sample_df, "01.01.2025 00:00:00")
    assert '"count": 2' in result_json
    assert '"total_amount": 1300.0' in result_json
    assert "Перевод" in result_json
    assert "Кафе" in result_json


def test_homepage_view_invalid_dates(sample_df):
    result_json = homepage_view(sample_df, "01.01.2025 00:00:00")
    assert "Оплата товаров" not in result_json
