import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(widget_info_and_result):
    for i in widget_info_and_result:

        for key, value in i.items():
            assert mask_account_card(key) == value


def test_get_date():
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert get_date("2018-09-12T21:27:25.241689") == "12.09.2018"
    assert get_date("") == ".."
