import leap


def test_year_divisible_by_100_not_400():
    assert False == leap.is_Leap_Year(1900)
    assert False == leap.is_Leap_Year(1700)
