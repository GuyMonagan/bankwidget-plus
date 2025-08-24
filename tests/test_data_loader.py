import pandas as pd
import pytest
from bankwidget_plus.data_loader import load_data

def test_load_data_missing_file(tmp_path, capsys):
    fake_file = tmp_path / "nonexistent.xlsx"
    df = load_data(str(fake_file))
    assert df.empty
    captured = capsys.readouterr()
    assert "Файл не найден" in captured.out
