from src.processing import filter_by_state, sort_by_date


import pytest

from tests.conftest import bank_data, non_state


def test_filter_by_state(bank_data):
    assert filter_by_state(bank_data) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]



def test_filter(state_canceled, bank_data, non_state):
    assert filter_by_state(state_canceled, state = "EXECUTED"  ) == []
    assert filter_by_state(bank_data, state = "CANCELED") == state_canceled
    assert filter_by_state(non_state) == []