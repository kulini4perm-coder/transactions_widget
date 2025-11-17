import masks


def mask_account_card(type_and_number: str) -> str:
    """Функция принимает данные о картах и счетах и возвращает данные
    с замаскированным номером карты/счета"""

    name_card: str = ""
    number_card: str = ""
    mask_number: str = ""

    for char in type_and_number:  # Разбиваем данные на список с названием
        if char.isdigit():  # и список с номером карты/счета
            number_card += char
        else:
            name_card += char

    if len(number_card) == 16:  # Создаем маску для номера карты
        mask_number = masks.get_mask_card_number(number_card)

    else:  # Создаем маску для номера счета
        mask_number = masks.get_mask_account(number_card)

    return "".join(name_card + mask_number)  # Возвращаем данные с замаскированным номером карты/счета


def get_date(incoming_date: str) -> str:
    """Функция принимает данные о дате, преобразует
    и возвращает в необходимом формате"""

    day: str = incoming_date[8:10]  # Выбираем данные о дне, месяце, годе из входящей строки
    month: str = incoming_date[5:7]
    year: str = incoming_date[0:4]

    return f"{day}.{month}.{year}"  # Возвращаем в нужном формате
