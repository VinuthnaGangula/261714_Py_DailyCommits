# To find the day of the year for a given date.
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True


def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif (month % 2 == 1 and month < 8) or (month % 2 == 0 and month > 7):
        return 31
    else:
        return 30


def day_of_year(year, month, day):
    days = 0
    for i in range(1, month):
        days += days_in_month(year, i)
    m = days_in_month(year, month)
    if day <= m:
        days += day
        return days
    else:
        return None


print(day_of_year(2000, 12, 31))
