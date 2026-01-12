import json
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_dir = os.path.join(BASE_DIR, "logs")  # Создаем полный путь к папке logs в корне
log_file = os.path.join(log_dir, "utils.log")

if not os.path.exists(log_dir):  # Создаем папку logs, если её нет
    os.makedirs(log_dir)

logger = logging.getLogger("utils")  # Настраиваем логирование
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_financial_transactions(path: str) -> list[dict]:
    """Читает JSON-файл и возвращает список словарей с данными о транзакциях.
    В случае отсутствия файла, пустого содержимого или если данные не являются списком,
    возвращает пустой список."""

    logger.info(f"Запрос на чтение файла: {path}")

    if not os.path.exists(path):  # Проверка существования файла
        logger.error(f"Ошибка: файл не найден по пути {path}")
        return []

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

            if isinstance(data, list):  # Проверка, что данные являются списком
                logger.info(f"Файл успешно прочитан. Найдено транзакций: {len(data)}")
                return data
            else:
                logger.error(f"Ошибка: данные в файле {path} не являются списком (list)")
                return []

    except (json.JSONDecodeError, FileNotFoundError):
        # Ошибка декодирования (пустой файл или не JSON) или файл не найден
        logger.error(f"Ошибка: файл {path} содержит некорректный JSON или пуст")
        return []
