import leap


def test_year_divisible_by_4_not_100():
    assert True == leap.is_Leap_Year(2000)
