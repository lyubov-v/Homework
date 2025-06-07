from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
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

    return wrapper


@log(filename="mylog.txt")
def get_date(data_file: str) -> str:
    """Принимает строку, возвращает строку в формате ДД.ММ.ГГГГ"""
    return f"{data_file[8:10]}.{data_file[5:7]}.{data_file[:4]}"


get_date("2019-07-03T18:35:29.512364")


@log(filename=None)
def positive_summ(a: int, b: int) -> int:
    """Возвращет сумму только положительных чисел"""
    if a > 0 and b > 0:
        result = a + b
    return result


positive_summ(-1, 8)
