import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Загружает данные из Excel-файла по указанному пути.

    Попытка чтения осуществляется с помощью pandas.read_excel.
    В случае отсутствия файла, выводится сообщение об ошибке
    и возвращается пустой DataFrame.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        pd.DataFrame: Загруженные данные в виде DataFrame,
        либо пустой DataFrame при FileNotFoundError.
    """
    try:
        return pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return pd.DataFrame()
