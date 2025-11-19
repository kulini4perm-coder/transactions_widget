def filter_by_state(list_of_dicts: list[dict], value_state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует и возвращает список по значению ключа 'state'"""

    filtered_list: list[dict] = []
    for any_dict in list_of_dicts:
        if any_dict.get("state") == value_state:
            filtered_list.append(any_dict)

    return filtered_list


def sort_by_date(list_of_dicts: list[dict], descending: bool = True) -> list[dict]:
    """Функция сортирует список словарей по значению ключа 'date'"""

    reverse_flag = descending  # Направление сортировки: True для убывания, False для возрастания

    # Используем функцию sorted(), сортируем по значению ключа 'date'
    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=reverse_flag)

    return sorted_list
