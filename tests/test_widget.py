import pytest


from src.widget import mask_account_card, get_date


# Тестируем функцию mask_account_card
def test_mask_account_card_for_card(input_card):  # Тест на определение карты
    assert mask_account_card(input_card) == "Visa Classic 1234 56** **** 5678"


def test_mask_account_card_for_account(input_account):  # Тест на определение счета
    assert mask_account_card(input_account) == 'Счет **7890'


@pytest.mark.parametrize('value, expected', [  # Параметризация для разных типов карт
        ("Maestro 1234567812345678", "Maestro 1234 56** **** 5678"),
        ("МИР 9876543210123456", "МИР 9876 54** **** 3456"),
        ("Visa 0000000000000000", "Visa 0000 00** **** 0000"),
    ])
def test_mask_account_card_type_card(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize("value, expected", [  # Параметризация для разных типов счетов
        ("Счет 12345678901234567890", "Счет **7890"),
        ("Депозитный 00000000000000000000", "Депозитный **0000"),
        ("Валютный счет 99992222333344445555", "Валютный счет **5555"),
    ])
def test_mask_account_card_type_accounts(value, expected):
    assert mask_account_card(value) == expected


@pytest.mark.parametrize("value, expected", [  # Параметризация в случае отсутствия названия карты/счета
        ("12345678901234567890", "Название карты/счета не определено **7890"),
        ("9876543210123456", "Название карты/счета не определено 9876 54** **** 3456"),
    ])
def test_mask_account_card_name_missing(value, expected):
    assert mask_account_card(value) == expected


# Тестируем функцию get_date
@pytest.mark.parametrize("value, expected", [  # Тест для разных корректных дат
        ("2024-01-01T00:00:00.000000", "01.01.2024"),
        ("2003-11-20T23:59:59.999999", "20.11.2003"),
        ("1985-02-29T10:00:00.000000", "29.02.1985"),
    ])
def test_get_date_different_dates(value, expected):
    assert get_date(value) == expected


def test_get_date_empty_string():  # С пустой входной строкой
    with pytest.raises(ValueError):
        get_date("")

