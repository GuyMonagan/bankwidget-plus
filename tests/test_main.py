import pytest
from bankwidget_plus import main as main_module

@pytest.fixture
def fake_input(monkeypatch):
    # Подменяем инпут
    monkeypatch.setattr("builtins.input", lambda _: "01.01.2025 00:00:00")

def test_main_output_with_real_excel(fake_input, capsys):
    main_module.main()
    captured = capsys.readouterr()
    assert '"count":' in captured.out
    assert '"transactions":' in captured.out
