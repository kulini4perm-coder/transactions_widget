import os

import pytest

from src.decorators import log


# Тестовая функция, которая работает успешно
@log()
def success_func(x: int, y: int) -> int:
    return x + y


# Тестовая функция, которая падает с ошибкой
@log()
def error_func(x: int, y: int) -> float:
    return x / y


# Проверка успешного выполнения (проверка вывода в консоль)
def test_log_console_success(capsys: pytest.CaptureFixture[str]) -> None:
    success_func(1, 2)
    captured = capsys.readouterr()  # Перехватываем вывод в консоль
    assert captured.out == "success_func ok\n"


# Проверка выполнения с ошибкой (проверка формата сообщения об ошибке)
def test_log_console_error(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(ZeroDivisionError):
        error_func(10, 0)

    captured = capsys.readouterr()
    # Проверяем наличие имени функции, типа ошибки и входных данных
    assert captured.out == "error_func error: ZeroDivisionError. Inputs: (10, 0), {}\n"


# Проверка записи в файл
def test_log_to_file() -> None:
    filename = "test_log.txt"

    # Если файл остался от прошлых тестов — удаляем
    if os.path.exists(filename):
        os.remove(filename)

    # Оборачиваем функцию декоратором с указанием файла
    @log(filename=filename)
    def func_to_file(a: str) -> str:
        return a

    func_to_file("test_data")

    # Проверяем, что файл создался и содержит нужную строку
    assert os.path.exists(filename)
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        assert "func_to_file ok" in content

    # Чистим за собой
    os.remove(filename)


# Проверка с использованием данных из фикстур к другим тестам
def test_log_with_fixtures(capsys: pytest.CaptureFixture[str], some_dicts: list[dict]) -> None:
    @log()
    def process_data(data: list[dict]) -> int:
        return len(data)

    process_data(some_dicts)
    captured = capsys.readouterr()
    assert captured.out == "process_data ok\n"
