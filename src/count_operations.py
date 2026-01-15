from collections import Counter
from typing import Any, Dict, List


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций для каждой категории из переданного списка.
    Поиск ведется по точному совпадению в поле 'description'."""

    # Извлекаем все описания операций в отдельный список
    all_descriptions: List[str] = [str(operation.get("description", "")) for operation in data]

    # Используем Counter для быстрого подсчета всех уникальных описаний
    full_counts: Counter = Counter(all_descriptions)

    # Фильтруем результаты, оставляя только те категории, которые есть в списке 'categories'
    result: Dict[str, int] = {category: full_counts.get(category, 0) for category in categories}

    return result
