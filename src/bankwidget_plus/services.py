# services.py

import json
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def simple_search(query: str, transactions: list[dict]) -> str:
    """
    Ищет транзакции, содержащие строку запроса в поле 'Описание'
    """
    try:
        logger.info(f"Запрос поиска: {query}")
        filtered = [
            tx for tx in transactions
            if query.lower() in tx.get("Описание", "").lower()
        ]

        result = {
            "query": query,
            "matches": len(filtered),
            "results": filtered
        }

        return json.dumps(result, ensure_ascii=False, indent=2)

    except Exception as e:
        logger.error(f"Ошибка при поиске: {e}")
        return json.dumps({"error": str(e)})
