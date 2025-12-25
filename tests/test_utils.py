from unittest.mock import patch, mock_open
from src.utils import get_financial_transactions

# Тест, когда файл существует, доступен для чтения и содержит корректные данные.
@patch("os.path.exists")  # Заглушка для реального открытия файла
@patch("builtins.open", new_callable=mock_open, read_data='[{"amount": 100}]') # Имитируем проверочный файл
def test_get_financial_transactions(mock_file, mock_exists):
    # Настраиваем возврат значения для проверки существования файла
    mock_exists.return_value = True

    # Вызываем функцию
    result = get_financial_transactions("data/operations.json")

    # Проверяем результат
    assert result == [{"amount": 100}]

    # Проверяем, что файл открывался по верному пути и с нужной кодировкой
    mock_file.assert_called_once_with("data/operations.json", "r", encoding="utf-8")

# Тест, когда файл отсутствует
@patch("os.path.exists")
def test_get_financial_transactions_not_found(mock_exists):
    mock_exists.return_value = False  # Имитируем, что файл не найден

    result = get_financial_transactions("data/operations.json")

    assert result == []
    mock_exists.assert_called_once_with("data/operations.json")

# Тест: файл содержит словарь вместо списка
@patch("os.path.exists")
@patch("builtins.open", new_callable=mock_open, read_data='{"status": "not a list"}')
def test_get_financial_transactions_invalid_data(mock_file, mock_exists):
    mock_exists.return_value = True  # Имитируем, что файл существует

    result = get_financial_transactions("data/operations.json")  # Вызываем функцию

    assert result == []  # Проверяем, что вернулся пустой список

    mock_file.assert_called_once()