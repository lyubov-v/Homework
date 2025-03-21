import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import none_date


def test_filter_by_state(bank_data):
    assert filter_by_state(bank_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter(state_canceled, bank_data, non_state):
    assert filter_by_state(state_canceled, state="EXECUTED") == []
    assert filter_by_state(bank_data, state="CANCELED") == state_canceled
    assert filter_by_state(non_state) == []


def test_sort_date(bank_data, none_date):
    assert sort_by_date(bank_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(bank_data, ascending=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


with pytest.raises(KeyError) as exc_info:
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED"},
            {"id": 939719570, "state": "EXECUTED"},
            {"id": 594226727, "state": "CANCELED"},
            {"id": 615064591, "state": "CANCELED"},
        ]
    )
    assert str(exc_info.value) == "Необходимо значение для ключа date"
