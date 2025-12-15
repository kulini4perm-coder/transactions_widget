import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тест filter_by_currency для существующей валюты "USD"
def test_filter_by_currency_usd(transactions: list[dict], transactions_usd: str) -> None:
    result_list = list(filter_by_currency(transactions, "USD"))
    assert result_list == transactions_usd


# Тест filter_by_currency для существующей валюты "RUB"
def test_filter_by_currency_rub(transactions: list[dict], transactions_rub: str) -> None:
    result_list = list(filter_by_currency(transactions, "RUB"))
    assert result_list == transactions_rub


# Тест filter_by_currency, если валюта не найдена
def test_filter_by_currency_missing_currency(transactions: list[dict]) -> None:
    missing_currency: str = "EUR"
    result_list = list(filter_by_currency(transactions, missing_currency))
    assert result_list == []


# Тест filter_by_currency, если список операций пустой
def test_filter_by_currency_empty_list() -> None:
    empty_list: list[dict] = []
    result_list = list(filter_by_currency(empty_list, "USD"))
    assert result_list == []


# Тест filter_by_currency с разными значениями
@pytest.mark.parametrize(
    "currency_code, expected_count, expected_descriptions",
    [
        ("USD", 3, ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]),
        ("RUB", 2, ["Перевод со счета на счет", "Перевод организации"]),
        ("EUR", 0, []),  # Проверка случая, когда валюты нет
    ],
)
def test_filter_by_currency_parameterized(
    transactions: list[dict], currency_code: str, expected_count: int, expected_descriptions: list[dict]
) -> None:
    result_list = list(filter_by_currency(transactions, currency_code))
    assert len(result_list) == expected_count


# Тест transaction_descriptions на корректность извлечения всех описаний из списка транзакций
def test_transaction_descriptions_correct(transactions: list[dict], expected_descriptions: list[str]) -> None:
    current_descriptions = list(transaction_descriptions(transactions))
    assert current_descriptions == expected_descriptions


# Тест transaction_descriptions, если список операций пустой
def test_transaction_descriptions_empty_list() -> None:
    empty_list: list[dict] = []
    result_descriptions = list(transaction_descriptions(empty_list))
    assert result_descriptions == []

    # Дополнительный тест на то, что пустой генератор сразу вызывает StopIteration при next()
    with pytest.raises(StopIteration):
        empty_iterator = transaction_descriptions(empty_list)
        next(empty_iterator)


# Тест card_number_generator для диапазона 1-5
def test_card_number_generator_1_to_5(expected_range_1_to_5: list[str]) -> None:
    start, end = 1, 5
    result_list = list(card_number_generator(start, end))
    assert result_list == expected_range_1_to_5


# Тест card_number_generator для диапазона 98 до 101
def test_card_number_generator_98_to_101(expected_range_98_to_101: list[str]) -> None:
    start, end = 98, 101
    result_list = list(card_number_generator(start, end))
    assert result_list == expected_range_98_to_101


# Тест card_number_generator если начальное и конечное значения аргументов равны
def test_card_number_generator_single_value() -> None:
    start, end = 1000, 1000
    result_list = list(card_number_generator(start, end))
    expected_list = ["0000 0000 0000 1000"]
    assert result_list == expected_list


# Тест card_number_generator когда start > end
def test_card_number_generator_empty_range() -> None:
    start, end = 10, 5  # Некорректный диапазон
    result_list = list(card_number_generator(start, end))
    assert result_list == []

    with pytest.raises(StopIteration):
        empty_iterator = card_number_generator(start, end)
        next(empty_iterator)


# Тест card_number_generator с разными диапазонами
@pytest.mark.parametrize(
    "start, end, expected_cards",
    [
        (1, 1, ["0000 0000 0000 0001"]),
        (1000000000000000, 1000000000000001, ["1000 0000 0000 0000", "1000 0000 0000 0001"]),
        (99, 101, ["0000 0000 0000 0099", "0000 0000 0000 0100", "0000 0000 0000 0101"]),
    ],
)
def test_card_number_generator_parameterized(start: int, end: int, expected_cards: list[str]) -> None:
    result = list(card_number_generator(start, end))
    assert result == expected_cards
