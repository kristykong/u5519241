def is_leap_year(year):
    # A year is a leap year if it is divisible by 4
    if year % 4 == 0:
        if year % 100 == 0:
            # They are also divisible by 400
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# test
print(is_leap_year(2020))  
print(is_leap_year(1900))  
print(is_leap_year(2000))  
print(is_leap_year(2019))  
