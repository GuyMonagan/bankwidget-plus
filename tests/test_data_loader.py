from pathlib import Path

from _pytest.capture import CaptureFixture
from pandas import DataFrame

from bankwidget_plus.data_loader import load_data


def test_load_data_missing_file(tmp_path: Path, capsys: CaptureFixture[str]) -> None:
    fake_file = tmp_path / "nonexistent.xlsx"
    df: DataFrame = load_data(str(fake_file))
    assert df.empty
    captured = capsys.readouterr()
    assert "Файл не найден" in captured.out
