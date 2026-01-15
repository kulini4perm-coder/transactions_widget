from typing import Any
from unittest.mock import MagicMock, patch

from src.data_loader import read_transactions_from_csv, read_transactions_from_excel


# Тестируем функцию чтения csv-файла

@patch("pandas.read_csv")
def test_read_transactions_from_csv_success(
        mock_read_csv: MagicMock, csv_excel_transactions: list[dict[str, Any]]) -> None:
    """Тест успешного чтения CSV с использованием фикстуры"""

    mock_df = MagicMock()
    mock_df.to_dict.return_value = csv_excel_transactions
    mock_read_csv.return_value = mock_df

    result = read_transactions_from_csv("data/transactions.csv")

    assert result == csv_excel_transactions
    assert result[0]["currency_code"] == "PEN"
    assert result[0]["amount"] == 16210
    mock_read_csv.assert_called_once()


@patch("pandas.read_csv")
def test_read_transactions_from_csv_error(mock_read_csv: MagicMock) -> None:
    """Тест покрытия блока EXCEPT для CSV"""

    mock_read_csv.side_effect = Exception("Ошибка чтения")

    result = read_transactions_from_csv("invalid.csv")

    assert result == []


@patch("pandas.read_csv")
def test_read_csv_file_not_found_error(mock_read: MagicMock) -> None:
    """Тест FileNotFoundError для CSV"""

    mock_read.side_effect = FileNotFoundError

    result = read_transactions_from_csv("non_existent.csv")

    assert result == []


# Тестируем функцию чтения excel-файла

@patch("pandas.read_excel")
def test_read_transactions_from_excel_success(
        mock_read_excel: MagicMock, csv_excel_transactions: list[dict[str, Any]]
) -> None:
    """Тест успешного чтения Excel с использованием фикстуры"""

    mock_df = MagicMock()
    # Имитируем цепочку .where().to_dict() для обработки NaN
    mock_df.where.return_value = mock_df
    mock_df.to_dict.return_value = csv_excel_transactions
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel("data/transactions_excel.xlsx")

    assert result == csv_excel_transactions
    assert result[0]["state"] == "EXECUTED"
    assert result[0]["description"] == "Перевод организации"
    mock_read_excel.assert_called_once()


@patch("pandas.read_excel")
def test_read_transactions_from_excel_error(mock_read_excel: MagicMock) -> None:
    """Тест покрытия блока EXCEPT для Excel"""

    mock_read_excel.side_effect = Exception("Ошибка Excel")

    result = read_transactions_from_excel("invalid.xlsx")

    assert result == []


@patch("pandas.read_excel")
def test_read_excel_file_not_found_error(mock_read: MagicMock) -> None:
    """Тест FileNotFoundError для Excel"""

    mock_read.side_effect = FileNotFoundError

    result = read_transactions_from_excel("non_existent.xlsx")

    assert result == []
