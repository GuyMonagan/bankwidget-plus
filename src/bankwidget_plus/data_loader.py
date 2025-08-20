import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return pd.DataFrame()
