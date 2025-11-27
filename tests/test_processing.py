import pytest

from src.processing import filter_by_state, sort_by_date


# Тестируем функцию filter_by_state по заданному статусу state
# Проверка по явно указанному статусу 'EXECUTED'
def test_filter_by_state_executed(some_dicts: list[dict], executed_dicts: list[dict]) -> None:
    assert filter_by_state(some_dicts, "EXECUTED") == executed_dicts


# Проверка по явно указанному статусу 'CANCELED'
def test_filter_by_state_canceled(some_dicts: list[dict], canceled_dicts: list[dict]) -> None:
    assert filter_by_state(some_dicts, "CANCELED") == canceled_dicts


# Проверка по умолчанию
def test_filter_by_state_by_default(some_dicts: list[dict], executed_dicts: list[dict]) -> None:
    assert filter_by_state(some_dicts) == executed_dicts


# Проверка фильтрации по статусу, словари с которым отсутствуют
def test_filter_by_state_processing(some_dicts: list[dict]) -> None:
    assert filter_by_state(some_dicts, "PROCESSING") == []


# Тест для разных корректных дат
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("PROCESSING", []),
        ("PENDING", []),
    ],
)
def test_filter_by_state_parametrize(some_dicts: list[dict], value: str, expected: list[dict]) -> None:
    assert filter_by_state(some_dicts, value) == expected


# Тестируем функцию sort_by_date


# Проверка сортировки по убыванию (по умолчанию descending=True)
def test_sort_by_date_descending_default(some_dicts: list[dict], dicts_descending: bool) -> None:
    assert sort_by_date(some_dicts) == dicts_descending


# Проверка сортировки по убыванию с явным указанием descending=True
def test_sort_by_date_descending(some_dicts: list[dict], dicts_descending: bool) -> None:
    assert sort_by_date(some_dicts, descending=True) == dicts_descending


# Проверка сортировки по возрастанию с указанием descending=False
def test_sort_by_date_ascending(some_dicts: list[dict], dicts_ascending: bool) -> None:
    assert sort_by_date(some_dicts, descending=False) == dicts_ascending
