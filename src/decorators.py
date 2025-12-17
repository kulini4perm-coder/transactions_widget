from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str]  = None) -> Callable:
    """Декоратор, который логирует вызов функции, её результат или возникшую ошибку."""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            message = ""

            try:
                result = func(*args, **kwargs)

            except Exception as e:  # Сообщение в случае ошибки: имя, тип ошибки и входные данные
                message = f"{func.__name__} error: {type(e).__name__}. " f"Inputs: {args}, {kwargs}\n"
                raise e

            else:  # Сообщение в случае успешного выполнения
                message = f"{func.__name__} ok\n"
                return result

            finally:  # Запись в файл или вывод в консоль
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message)

                else:
                    print(message, end="")

        return wrapper

    return decorator
