from typing import Dict, Generator, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: List[Dict], currency: str) -> Generator:
    """Принимает список транзакций,возвращает словарь, с заданной валютой"""
    if transactions == [{}]:
        yield {}
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") is None:
            yield {}
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


usd_transactions = filter_by_currency(transactions, "RUB")
try:
    for _ in range(5):
        print(next(usd_transactions))
except:
    print({})


def transaction_descriptions(transactions: List[Dict]) -> Generator:
    """Возвращает описание платежа"""
    if transactions == [{}]:
        yield {}
    for transaction in transactions:
        if transaction.get("description") is None:
            yield ""
        yield transaction.get("description")


descriptions = transaction_descriptions(transactions)
try:
    for _ in range(8):
        print(next(descriptions))
except:
    """"""


def card_number_generator(start: int, stop: int) -> Generator:
    """Генерирует номера карт в 16 разрядном формате"""
    numbers = (x for x in range(start, stop + 1))
    for i in numbers:
        new_number = str(i).zfill(16)
        card_number = f"{new_number[0:4]} {new_number[4:8]} {new_number[8:12]} {new_number[12:]}"
        yield card_number


for card_number in card_number_generator(1, 8):
    print(card_number)
