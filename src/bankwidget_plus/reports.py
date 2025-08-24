import json
import logging

import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

WEEKDAYS_RU = {
    0: "Понедельник",
    1: "Вторник",
    2: "Среда",
    3: "Четверг",
    4: "Пятница",
    5: "Суббота",
    6: "Воскресенье"
}


def expenses_by_weekday(df: pd.DataFrame, start_date: str = "2000-01-01") -> str:
    try:
        logger.info(f"Отчёт по дням недели с {start_date}")

        # Преобразуем столбец с датами
        df["Дата операции"] = pd.to_datetime(df["Дата операции"], errors="coerce")

        # Фильтруем по дате и явно создаём копию
        df_filtered = df[df["Дата операции"] >= pd.to_datetime(start_date)].copy()

        # Добавляем день недели в копию
        df_filtered.loc[:, "weekday"] = df_filtered["Дата операции"].dt.weekday

        # Группировка по дню недели и подсчёт суммы
        result = df_filtered.groupby("weekday")["Сумма платежа"].sum().to_dict()

        # Преобразование в читаемый формат
        readable_result = {
            WEEKDAYS_RU.get(day): float(amount)
            for day, amount in result.items()
        }

        return json.dumps(readable_result, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Ошибка при построении отчёта по дням недели: {e}")
        return json.dumps({"error": str(e)})
