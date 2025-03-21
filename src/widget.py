from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_info: str) -> str:
    """Принимает информацию о карте или счете и возвращает с маской"""
    name = []
    digit = []
    for symbol in card_info:
        if symbol.isdigit():
            digit.append(symbol)
        else:
            name.append(symbol)
    name_str = "".join(name)
    digit_str = "".join(digit)
    if "Счет" in name_str:
        masking = get_mask_account(digit_str)
        return f"{name_str}{masking}"
    else:
        masking = get_mask_card_number(digit_str)
        return f"{name_str}{masking}"


def get_date(data_file: str) -> str:
    """Принимает строку, возвращает строку в формате ДД.ММ.ГГГГ"""
    return f"{data_file[8:10]}.{data_file[5:7]}.{data_file[:4]}"
