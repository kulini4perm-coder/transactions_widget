from typing import Any, cast

import pandas as pd


def read_transactions_from_csv(file_path: str) -> list[dict[Any, Any]]:
    """Функция считывает финансовые операции из CSV-файла через pandas.
    Возвращает список словарей."""

    try:
        df = pd.read_csv(file_path, sep=';')
        # Преобразуем DataFrame в список словарей (orient='records')
        return cast(list[dict[Any, Any]], df.to_dict(orient="records"))
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []


def read_transactions_from_excel(file_path: str) -> list[dict[Any, Any]]:
    """Функция считывает финансовые операции из Excel через pandas.
    Возвращает список словарей."""

    try:
        df = pd.read_excel(file_path)
        # Заменяем значения NaN на None для корректного отображения в словарях
        df = df.where(pd.notnull(df), None)
        return cast(list[dict[Any, Any]], df.to_dict(orient="records"))
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []
