import json

import pytest

from bankwidget_plus.services import simple_search


@pytest.fixture
def transactions():
    return [
        {"Описание": "Покупка кофе в Старбаксе"},
        {"Описание": "Оплата электроэнергии"},
        {"Описание": "Перевод другу на карту"},
        {"Описание": "Кофе с молоком"},
    ]


def test_simple_search_matches(transactions):
    result_json = simple_search("кофе", transactions)
    result = json.loads(result_json)

    assert result["query"] == "кофе"
    assert result["matches"] == 2
    assert any("Старбаксе" in tx["Описание"] for tx in result["results"])
    assert any("молоком" in tx["Описание"] for tx in result["results"])


def test_simple_search_no_matches(transactions):
    result_json = simple_search("стиральная машина", transactions)
    result = json.loads(result_json)

    assert result["matches"] == 0
    assert result["results"] == []
