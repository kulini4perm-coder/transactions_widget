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


def card_number_generator(start_value: int, final_value: int) -> Iterator[str]:
    """Функция генерирует номера банковских карт в формате 'XXXX XXXX XXXX XXXX'
    в заданном числовом диапазоне"""

    for number in range(start_value, final_value + 1):
        card_str = str(number)
        number_of_zeros = 16 - len(card_str)
        full_card_str = "0" * number_of_zeros + card_str

        number_of_card = f"{full_card_str[:4]} {full_card_str[4:8]} {full_card_str[8:12]} {full_card_str[12:]}"

        yield number_of_card
