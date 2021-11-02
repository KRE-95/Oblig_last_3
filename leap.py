def is_Leap_Year(year):
    # make a boolean (as the task ask for)

    # make a check if the year is divisible by 4 and by 400, not by 100.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    # not by 4 and 400 but by 100
    else:
        return False


# as a validation
print(" This a is a leap year : ", is_Leap_Year(2000))
print(" This a is a Not a leap year : ", is_Leap_Year(1900))

