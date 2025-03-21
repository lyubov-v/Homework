def filter_by_state(info: list, state="EXECUTED") -> list:
    """Фильтрует список по значению state"""
    new_info = []
    for position in info:
        if position.get("state") == state:
            new_info.append(position)
        else:
            continue
    return new_info


def sort_by_date(info: list, ascending=True) -> list:
    """Сортирует список по дате(убывание)"""
    sort_info = []
    for position in info:
        if position.get("date") == None:
            raise KeyError("Необходимо значение для ключа date")

        sort_info = sorted(info, key=lambda position: position["date"], reverse=ascending)

    return sort_info
