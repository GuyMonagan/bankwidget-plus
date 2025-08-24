from typing import Iterator
from unittest.mock import MagicMock, patch

import pandas as pd
import pytest
from _pytest.capture import CaptureFixture

from bankwidget_plus import main as main_module


@pytest.fixture
def fake_inputs(monkeypatch: pytest.MonkeyPatch) -> None:
    inputs: Iterator[str] = iter(["1", "2025-01-01 00:00:00", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))


@patch("bankwidget_plus.main.load_data")
def test_main_with_fake_data(
    mock_load_data: MagicMock,
    fake_inputs: None,
    capsys: CaptureFixture[str],
) -> None:
    mock_load_data.return_value = pd.DataFrame(
        [
            {"Дата операции": "2025-01-08", "Сумма платежа": 1000.0, "Описание": "Фейковый перевод"},
            {"Дата операции": "2025-01-07", "Сумма платежа": 300.0, "Описание": "Фейковое кафе"},
        ]
    )

    main_module.main()
    captured = capsys.readouterr()
    assert '"count": 2' in captured.out
    assert "Фейковый перевод" in captured.out
    assert "Фейковое кафе" in captured.out


@patch("bankwidget_plus.main.load_data")
def test_main_weekday_report(
    mock_load_data: MagicMock,
    monkeypatch: pytest.MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    mock_load_data.return_value = pd.DataFrame(
        [
            {"Дата операции": "2025-01-08", "Сумма платежа": 100.0},
            {"Дата операция": "2025-01-09", "Сумма платежа": 200.0},
        ]
    )
    inputs: Iterator[str] = iter(["2", "2025-01-01", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main_module.main()  # Сначала запускаем
    out = capsys.readouterr().out  # Потом читаем вывод

    assert "Понедельник" in out or "Вторник" in out or "Среда" in out


@patch("bankwidget_plus.main.load_data")
def test_main_invalid_choice(
    mock_load_data: MagicMock,
    monkeypatch: pytest.MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    mock_load_data.return_value = pd.DataFrame()
    inputs: Iterator[str] = iter(["42", "0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main_module.main()
    out = capsys.readouterr().out
    assert "Неверный выбор" in out


@patch("bankwidget_plus.main.load_data")
def test_main_exit_immediately(
    mock_load_data: MagicMock,
    monkeypatch: pytest.MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    mock_load_data.return_value = pd.DataFrame()
    monkeypatch.setattr("builtins.input", lambda _: "0")

    main_module.main()
    out = capsys.readouterr().out
    assert "До свидания" in out
