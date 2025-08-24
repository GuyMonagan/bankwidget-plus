import json
import logging
from datetime import datetime
from pandas import DataFrame

from bankwidget_plus.utils import filter_transactions_since_date

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def homepage_view(df: DataFrame, date_str: str) -> str:
    """
    Возвращает JSON-ответ с информацией о транзакциях с указанной даты.
    """
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
        logger.info(f"Фильтрация транзакций начиная с: {date_str}")
        filtered_df = filter_transactions_since_date(df, date)

        # Ключевой момент — сериализуемая дата
        filtered_df["Дата операции"] = filtered_df["Дата операции"].dt.strftime("%d.%m.%Y")

        result = {
            "count": len(filtered_df),
            "total_amount": float(filtered_df["Сумма платежа"].sum()),
            "transactions": filtered_df.to_dict(orient="records"),
        }

        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Ошибка при обработке главной страницы: {e}")
        return json.dumps({"error": str(e)})
