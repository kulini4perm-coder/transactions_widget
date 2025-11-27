import pytest


@pytest.fixture()  # Для get_mask_card_number
def number_card() -> str:
    return "1234567890123456"


@pytest.fixture()  # Для get_mask_account
def number_account() -> str:
    return "12345678901234567890"


@pytest.fixture()  # Для mask_account_card
def input_card() -> str:
    return "Visa Classic 1234567812345678"


@pytest.fixture()  # Для mask_account_card
def input_account() -> str:
    return "Счет 98765432101234567890"


@pytest.fixture()  # Фикстура для filter_by_state
def some_dicts() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture()  # Фикстура для filter_by_state
def executed_dicts() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture()  # Фикстура для filter_by_state
def canceled_dicts() -> list[dict]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture  # Фикстура sort_by_date с ожидаемыми данными, отсортированными по убыванию
def dicts_descending() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture  # Фикстура sort_by_date с ожидаемыми данными, отсортированными по возрастанию
def dicts_ascending() -> list[dict]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
