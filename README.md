# Homework
## Описание
Homework_10_1
В проекте создан файл Processing c функциями, сортирующими список по значению state(по умолчанию EXECUTED), а так же по дате от меньшего значения к большему.
## Пример работы функций
**Функция filter_by_state**
`print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)`
>>>[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

**Функция sort_by_date**
`print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)`
>>>[{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

## Homework_10_2
В проект добавлены модули с предыдущих домашних работ: widget.py и masks.py
В модуле masks.py содержатся функции:
**Функция get_mask_card_number**
`print(get_mask_card_number("7158300734726758"))`
>>>"7158 30** **** 6758"

**Функция get_mask_account**
`print(get_mask_account("35383033474447895560"))`
>>>"**5560"

В модуле widget.py содержатся функции:
**Функция mask_account_card**
`print(mask_account_card("MasterCard 7158300734726758"))`
>>>"MasterCard 7158 30** **** 6758"

**Функция get_date**
`print(get_date("2019-07-03T18:35:29.512364"))`
>>>"03.07.2019"
> 
> ### Для всех модулей созданы тесты
> Тесты содержаться в папке tests
Результаты покрытия кода тестами добавлены в проект в папку htmlcov
> 
 ## Homework_11.1
Добавлен модуль generators.py, содержащий функции:
**Функция filter_by_currency**

`result = filter_by_currency([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ],
"RUB")
try:
    for _ in range(2):
        print(next(result))
except: print({})`
>>>{'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689', 'operationAmount': {'amount': '67314.70', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}

**Функция transaction_descriptions**
`descriptions = transaction_descriptions([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ])
try:
    for _ in range(5):
        print(next(descriptions))
except: ""`
>>>Перевод организации
Перевод со счета на счет
Перевод со счета на счет
Перевод с карты на карту
Перевод организации

**Функция card_number_generator**
`for card_number in card_number_generator(1, 5):
    print(card_number)`
>>>0000 0000 0000 0001
0000 0000 0000 0002
0000 0000 0000 0003
0000 0000 0000 0004
0000 0000 0000 0005
### В директорию tests добавлен модуль test_generator.py с тестами для всех функций
Тесты по filter_by_currency со значением валют USD и RUB, с пустым списком, и без заданной валюты в списке
Тесты по transaction_descriptions на правильное выведение значений, а также при отсутствующем значении
Тесты для card_number_generator выполнены с параметризацией, генерируются верные значения

Результаты покрытия кода тестами добавлены в проект в папку htmlcov
## Homework_11.2
### В директорию src добавлен модуль decorators.py, в модуле реализован декоратор log.
### Декоратор log логирует выполнение, или возникающие ошибки при выполнении обернутой функции в заданный файл, если файл не задан,то выводит в консоль.
**Декоратор log**
`def log(filename: Any) -> Callable:
    """Декоратор, логтрующий в заданный файл имя выполненной функции, либо имя и ошибку при выполнении,
    если файл не задан, записывает результат в консоль"""

    def wrapper(function: Callable) -> Callable:
        @wraps(function)
        def recording(*args: Any, **kwargs: Any)-> Callable:
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                result = None
                if filename == None:
                    print(f"{function.__name__} error {e}, arguments: {args}, {kwargs}")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} error {e}, arguments: {args}, {kwargs}")
            if result:
                if filename == None:
                    print(f"{function.__name__} OK")
                else:
                    with open(filename, "a") as file:
                        file.write(f"{function.__name__} OK\n")
            return result

        return recording

    return wrapper`

### Пример
`@log(filename="mylog.txt")
def get_date(data_file: str) -> str:
    """Принимает строку, возвращает строку в формате ДД.ММ.ГГГГ"""
    return f"{data_file[8:10]}.{data_file[5:7]}.{data_file[:4]}"


get_date("2019-07-03T18:35:29.512364")`
>>>"gat_date OK" in "mylog.txt"
> 
> 
### В директорию tests добавлен файл test_decorators.py, где реализованы тесты для декоратора log.

test_log - проверяет декоратор на успешную запись в файл

test_log_error - проверяет декоратор при вызове функции с ошибкой на вывод в консоль

#### Результаты покрытия кода тестами записаны в папку htmlcov

