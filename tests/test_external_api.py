from unittest.mock import MagicMock, Mock, patch
import requests
from src.external_api import convert_to_rub, get_transaction_amount_in_rub


# Тестируем успешную конвертацию USD в RUB через API
@patch("requests.get")
def test_convert_to_rub_success(mock_get: MagicMock) -> None:
    mock_response = Mock()  # Настройка Mock-ответа
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 9000.0}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = convert_to_rub(100.0, "USD")  # Вызов функции

    # Проверки
    assert result == 9000.0
    mock_get.assert_called_once()  # Проверяем, что запрос был отправлен


# Тестируем обработку ошибки API (статус 401 Unauthorized).
@patch("os.getenv", return_value="fake_api_key")
@patch("requests.get")
def test_convert_to_rub_api_error(mock_get: MagicMock, mock_getenv: MagicMock) -> None:
    # Имитируем ответ с ошибкой
    mock_response = Mock()
    mock_response.status_code = 401
    # Вместо возврата 200, raise_for_status должен выбросить исключение
    mock_response.raise_for_status.side_effect = requests.RequestException

    mock_get.return_value = mock_response

    result = convert_to_rub(100.0, "EUR")

    # Ожидаем, что функция вернет 0.0, как задумано в обработке ошибок
    assert result == 0.0


# Тестируем случай, когда конвертация не нужна (валюта уже RUB).
def test_convert_to_rub_is_rub() -> None:
    result = convert_to_rub(500.0, "RUB")
    assert result == 500.0


# Тесты для get_transaction_amount_in_rub


# Тестируем вызов функции-конвертера для транзакции в USD.
@patch("src.external_api.convert_to_rub", return_value=5555.0)
def test_get_transaction_amount_in_rub_usd(mock_convert: MagicMock) -> None:
    transaction = {"operationAmount": {"amount": "50.00", "currency": {"code": "USD"}}}

    result = get_transaction_amount_in_rub(transaction)

    assert result == 5555.0
    # Проверяем, что внутренняя функция convert_to_rub была вызвана 1 раз
    mock_convert.assert_called_once_with(50.0, "USD")


# Тестируем получение суммы для транзакции в RUB (без конвертации).
def test_get_transaction_amount_in_rub_rub() -> None:
    transaction = {"operationAmount": {"amount": "1500.25", "currency": {"code": "RUB"}}}

    result = get_transaction_amount_in_rub(transaction)

    assert result == 1500.25
