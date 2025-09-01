import json

import pytest

from bankwidget_plus.services import simple_search


@pytest.fixture
def transactions() -> list[dict[str, str]]:
    return [
        {"Описание": "Покупка кофе в Старбаксе"},
        {"Описание": "Оплата электроэнергии"},
        {"Описание": "Перевод другу на карту"},
        {"Описание": "Кофе с молоком"},
    ]


@pytest.mark.parametrize(
    "query,expected_count,expected_descriptions",
    [
        ("кофе", 2, ["Старбаксе", "молоком"]),
        ("перевод", 1, ["Перевод"]),
        ("электроэнергии", 1, ["электроэнергии"]),
        ("неизвестное", 0, []),
    ],
)
def test_simple_search_parametrized(
    transactions: list[dict[str, str]], query: str, expected_count: int, expected_descriptions: list[str]
) -> None:
    result_json = simple_search(query, transactions)
    result = json.loads(result_json)

    assert result["query"] == query
    assert result["matches"] == expected_count

    for word in expected_descriptions:
        assert any(word.lower() in tx["Описание"].lower() for tx in result["results"])
