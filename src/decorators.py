from functools import wraps


def log(filename):
    def wrapper(function):
        @wraps(function)
        def recording(*args,**kwargs):
            try:
                result = function(*args,**kwargs)
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
    if a >0 and b > 0:
        result = a + b
    return result
positive_summ(-1,8)


