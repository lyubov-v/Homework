from functools import wraps


def log(filename):
    def wrapper(function):
        @wraps(function)
        def recording(*args, **kwargs):
            result = function(*args,**kwargs)
            try:
                if filename == None or filename == "":
                    print(f"{function.__name__} OK")
                with open(filename, "w") as file:
                    file.write(f"{function.__name__} OK\n")
            except Exception as e:
                if filename == None or filename == "":
                    print(f"{function.__name__} error {e} arguments: {args}, {kwargs}")

                with open(filename, "w") as file:
                    file.write(f"{function.__name__} error {e} arguments: {args}, {kwargs}")
            return result
        return recording
    return wrapper


@log(filename="mylog.txt")
def get_date(data_file: str) -> str:
    """Принимает строку, возвращает строку в формате ДД.ММ.ГГГГ"""
    return f"{data_file[8:10]}.{data_file[5:7]}.{data_file[:4]}"

get_date("2019-07-03T18:35:29.512364")


