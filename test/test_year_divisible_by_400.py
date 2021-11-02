import leap


def test_year_divisible_by_400():
    assert leap.is_Leap_Year(2000) == True
