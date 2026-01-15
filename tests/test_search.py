from typing import Any

import pytest

from src.search import process_bank_search


def test_process_bank_search_success(csv_excel_transactions: list[dict[str, Any]]) -> None:
    # Тест успешного поиска по существующему описанию
    result: list[dict[str, Any]] = process_bank_search(csv_excel_transactions, "Перевод")
    assert len(result) == 1
    assert result[0]["description"] == "Перевод организации"


def test_process_bank_search_ignore_case(csv_excel_transactions: list[dict[str, Any]]) -> None:
    # Тест поиска с игнорированием регистра
    result: list[dict[str, Any]] = process_bank_search(csv_excel_transactions, "пЕРЕВОД")
    assert len(result) == 1
    assert result[0]["id"] == 650703


def test_process_bank_search_not_found(csv_excel_transactions: list[dict[str, Any]]) -> None:
    # Тест ситуации, когда совпадений нет.
    result: list[dict[str, Any]] = process_bank_search(csv_excel_transactions, "Оплата")
    assert result == []


@pytest.mark.parametrize("search_str", ["Перевод", "организации", "орган"])
def test_process_bank_search_substrings(csv_excel_transactions: list[dict[str, Any]], search_str: str) -> None:
    # Тест поиска по различным подстрокам
    result: list[dict[str, Any]] = process_bank_search(csv_excel_transactions, search_str)
    assert len(result) == 1
