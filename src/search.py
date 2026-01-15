import re


def process_bank_search(data: list[dict], search_string: str) -> list[dict]:
    """Ищет операции по строке в описании (поле 'description').
    Возвращает список словарей, соответствующих запросу."""

    # Компилируем регулярное выражение с игнорированием регистра
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)

    # Фильтруем список, проверяя наличие совпадения в описании
    return [item for item in data if pattern.search(item.get("description", ""))]
