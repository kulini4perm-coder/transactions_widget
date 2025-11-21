import pytest


from src.masks import get_mask_card_number, get_mask_account


# Тестируем функцию get_mask_card
def test_get_mask_card_number_stand(number_card):  # Стандартный тест с фикстурами
    assert get_mask_card_number(number_card) == '1234 56** **** 3456'


@pytest.mark.parametrize('value, expected', [  # Используем параметризацию для разнообразных номеров
        ("1234567890123456", "1234 56** **** 3456"), # Стандартная длина 16 символов
        ("6543210987654321", "6543 21** **** 4321"), # Другой стандартный номер
        ("0000000000000000", "0000 00** **** 0000"), # Все нули
    ])
def test_get_mask_card_number_diff_numb(value, expected):
    assert get_mask_card_number(value) == expected


def test_get_mask_card_number_extreme(): # Проверка исключений

    with pytest.raises(ValueError):
        get_mask_card_number("123456789012345") # Проверка ValueError для короткой строки

    with pytest.raises(ValueError):
        get_mask_card_number("123456789012345689")  # Проверка ValueError для длинной строки

    with pytest.raises(ValueError):  # Проверка ValueError для пустой строки
        get_mask_card_number("")


# Тестируем функцию get_mask_account
def test_get_mask_account_stand(number_account):  # Стандартный тест с фикстурами
    assert get_mask_account(number_account) == '**7890'


@pytest.mark.parametrize('value, expected', [  # Используем параметризацию для разнообразных номеров
        ("12341234567890123456", "**3456"), # Стандартная длина 20 символов
        ("09876543210987654321", "**4321"), # Другой стандартный номер
        ("00000000000000000000", "**0000"), # Все нули
    ])
def test_get_mask_account_diff_numb(value, expected):
    assert get_mask_account(value) == expected


def test_get_mask_account_extreme(): # Проверка исключений

    with pytest.raises(ValueError):
        get_mask_account("1234123456789012345") # Проверка ValueError для короткой строки

    with pytest.raises(ValueError):
        get_mask_account("123412345678901234567")  # Проверка ValueError для длинной строки

    with pytest.raises(ValueError):  # Проверка ValueError для пустой строки
        get_mask_account("")
