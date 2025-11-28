from src.generators import filter_by_currency


# Тест для существующей валюты "USD"
def test_filter_by_currency_usd(transactions: list[dict], transactions_usd: str) -> None:
    result_list = list(filter_by_currency(transactions, "USD"))
    assert result_list == transactions_usd


# Тест для существующей валюты "RUB"
def test_filter_by_currency_rub(transactions: list[dict], transactions_rub: str) -> None:
    result_list = list(filter_by_currency(transactions, "RUB"))
    assert result_list == transactions_rub


# Тест, если валюта не найдена
def test_filter_by_currency_missing_currency(transactions: list[dict]) -> None:
    missing_currency: str = "EUR"
    result_list = list(filter_by_currency(transactions, missing_currency))
    assert result_list == []


# Тест, если список операций пустой
def test_filter_by_currency_empty_list() -> None:
    empty_list: list[dict] = []
    result_list = list(filter_by_currency(empty_list, "USD"))
    assert result_list == []
