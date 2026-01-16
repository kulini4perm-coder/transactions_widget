from typing import Any

from src.count_operations import process_bank_operations


def test_process_bank_operations_with_fixture(csv_excel_transactions: list[dict[str, Any]]) -> None:
    # Проверка подсчета категорий на основе данных из фикстуры
    categories = ["Перевод организации", "Оплата связи"]

    result = process_bank_operations(csv_excel_transactions, categories)

    assert result["Перевод организации"] == 1
    assert result["Оплата связи"] == 0


def test_process_bank_operations_multiple_items() -> None:
    # Проверка корректности сложения нескольких одинаковых категорий
    data = [
        {"description": "Оплата кофе"},
        {"description": "Оплата кофе"},
        {"description": "Перевод"},
    ]
    categories = ["Оплата кофе", "Перевод", "ЖКХ"]

    result = process_bank_operations(data, categories)

    assert result["Оплата кофе"] == 2
    assert result["Перевод"] == 1
    assert result["ЖКХ"] == 0
