import pytest

from src.generators import filter_by_currency, transaction_descriptions


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
