from typing import Iterator


def filter_by_currency(list_of_dicts: list[dict], currency: str) -> Iterator[dict]:
    """Функция принимает список транзакций и затем поочередно выдает
    транзакции по заданной валюте"""

    for transaction in list_of_dicts:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
