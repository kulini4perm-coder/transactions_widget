import json
import os


def get_financial_transactions(path: str) -> list[dict]:
    """ Читает JSON-файл и возвращает список словарей с данными о транзакциях.
    В случае отсутствия файла, пустого содержимого или если данные не являются списком,
    возвращает пустой список. """

    if not os.path.exists(path):  # Проверка существования файла
        return []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

            if isinstance(data, list):  # Проверка, что данные являются списком
                return data
            else:
                return []

    except (json.JSONDecodeError, FileNotFoundError):
        # Ошибка декодирования (пустой файл или не JSON) или файл не найден
        return []
