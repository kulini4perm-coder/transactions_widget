def get_mask_card_number(number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску:
    закрыты цифры по порядку с 7 по 12, номер разбит на блок по 4 цифры"""
    if not number or len(number) < 16:  # Добавлен после тестирования, проверяет длину номера
        raise ValueError("Номер карты слишком короткий или отсутствует.")
    if len(number) > 16:
        raise ValueError("Номер карты слишком длинный")

    list_char_of_number: list[str] = list(number)  # Перевод строкового значения в список

    for i in range(6, 12):  # Замена цифр по порядку с 7 по 12 на "*"
        list_char_of_number[i] = "*"

    insert_interval = 4  # Разбиваем пробелом номер на блоки с интервалом в 4 цифры
    insert_char = " "
    index = 4  # Начинаем с индекса 4
    while index < len(list_char_of_number):  # Выполняем разбивку пока номер индекса меньше длины списка
        list_char_of_number.insert(index, insert_char)
        index += insert_interval + 1

    mask_card_number: str = "".join(list_char_of_number)  # Объединяем список в строку для вывода маски

    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if not account_number or len(account_number) < 20:  # Добавлен после тестирования, проверяет длину номера
        raise ValueError("Номер счета слишком короткий или отсутствует.")
    if len(account_number) > 20:
        raise ValueError("Номер счета слишком длинный")

    mask_account: list[str] = ["*", "*"]  # Создаем список символов маски
    list_char_of_number: list[str] = list(account_number)  # Перевод строкового вида номера счета в список

    for i in range(16, len(list_char_of_number)):  # Выбираем из номера счета последние четыре цифры
        mask_account.append(list_char_of_number[i])  # и добавляем их в конец маски

    return "".join(mask_account)  # Выводим маску в строковом виде
