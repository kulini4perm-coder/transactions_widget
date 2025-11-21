import pytest


@pytest.fixture() # Для get_mask_card_number
def number_card():
    return '1234567890123456'


@pytest.fixture() # Для get_mask_account
def number_account():
    return '12345678901234567890'

