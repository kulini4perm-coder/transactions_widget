def filter_by_state(list_of_dicts: list[dict], value_state: str = "EXECUTED") -> list[dict]:
    """Функция фильтрует и возвращает список по значению ключа 'state'"""

    filtered_list: list[dict] = []
    for any_dict in list_of_dicts:
        if any_dict.get("state") == value_state:
            filtered_list.append(any_dict)

    return filtered_list
