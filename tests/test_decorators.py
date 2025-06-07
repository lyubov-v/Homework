import  pytest
from src.decorators import log


def test_log():
    @log(filename = "testlog.txt")
    def get_date(data_file: str) -> str:
        return f"{data_file[8:10]}.{data_file[5:7]}.{data_file[:4]}"
        get_date("2019-07-03T18:35:29.512364")
        with open(filename, "r") as file:
            record = file.read()
        assert record == "get_date OK"


def test_log_error(capsys):
    @log(None)
    def positive_summ(a: int, b: int)-> int or str:
        if a > 0 and b > 0:
            result = a + b
        return result
    positive_summ(-1, 8)
    captured = capsys.readouterr()
    assert captured.out == "positive_summ error cannot access local variable 'result' where it is not associated with a value, arguments: (-1, 8), {}\n"

