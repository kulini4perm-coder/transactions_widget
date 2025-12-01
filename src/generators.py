from typing import Iterator


def filter_by_currency(list_of_dicts: list[dict], currency: str) -> Iterator[dict]:
    """Функция принимает список транзакций и затем поочередно выдает
    транзакции по заданной валюте"""

    for transaction in list_of_dicts:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(list_of_dicts: list[dict]) -> Iterator[str]:
    """Генератор возвращает описание каждой операции из списка транзакций по очереди"""

    for transaction in list_of_dicts:
        yield transaction["description"]
