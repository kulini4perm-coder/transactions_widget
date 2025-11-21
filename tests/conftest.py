import pytest


@pytest.fixture() # Для get_mask_card_number
def number_card():
    return '1234567890123456'


@pytest.fixture() # Для get_mask_account
def number_account():
    return '12345678901234567890'


@pytest.fixture() # Для mask_account_card
def input_card():
    return 'Visa Classic 1234567812345678'


@pytest.fixture() # Для mask_account_card
def input_account():
    return 'Счет 98765432101234567890'

