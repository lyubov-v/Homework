import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("number, mask_number", [("7000792289606361", "7000 79** **** 6361"),
("70007922896063610361", "7000 79** **** 0361"),
("", " ** **** ")])
def test_mask_number(number, mask_number):
    assert get_mask_card_number(number) == mask_number


@pytest.mark.parametrize("account, mask_account", [("73654108430135874305", "**4305"),
("33652598", "**2598"),
("","**")])
def test_mask_account(account, mask_account):
    assert get_mask_account(account) == mask_account

