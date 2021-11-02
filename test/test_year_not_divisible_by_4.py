import pytest

import leap


def test_year_not_divisible_by_4():
    assert False == leap.is_Leap_Year(2100)
