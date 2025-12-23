import os

import requests
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(amount: float, currency: str) -> float:
    """Конвертирует сумму из USD или EUR в RUB через Exchange Rates Data API.
    Возвращает сумму в рублях (float). В случае ошибки возвращает 0.0."""

    if currency == "RUB":  # Если валюта уже рубли, конвертация не требуется
        return float(amount)

    # URL для конвертации
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {"apikey": API_KEY}

    try:
        # Отправляем GET-запрос
        response = requests.get(url, headers=headers, timeout=10)  # timeout=10 - ограничиваем время ответа на запрос

        response.raise_for_status()  # Если статус-код не 200, это вызовет исключение и переход в блок except

        data = response.json()

        return float(data.get("result", 0.0))  # Возвращаем результат конвертации

    except (requests.RequestException, KeyError, ValueError):
        # В случае сетевой ошибки, неверного ключа или проблем с JSON возвращаем 0.0
        return 0.0


def get_transaction_amount_in_rub(transaction: dict) -> float:
    """Принимает транзакцию и возвращает сумму в рублях (float).
    Если валюта не RUB, обращается к внешнему API."""

    operation_amount = transaction.get("operationAmount", {})  # Извлекаем данные из транзакции
    amount = float(operation_amount.get("amount", 0.0))
    currency_code = operation_amount.get("currency", {}).get("code", "RUB")

    if currency_code == "RUB":
        return amount
    else:
        return convert_to_rub(amount, currency_code)
