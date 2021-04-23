# To get next day of a given date.

date_format = tuple(input("Enter date: ").split('-'))
date = int(date_format[0])
month = int(date_format[1])
year = int(date_format[2])

next_date = 0
next_month = 0
next_year = 0

if year % 4 == 0 and month == 2 and date == 28:
    next_date = 29
    next_month = 2
    next_year = year
elif month == 12 and date == 31:
    next_date = 1
    next_month = 1
    next_year = year + 1
elif month == 2 and date == 28:
    next_date = 1
    next_month = 3
    next_year = year
elif ((month % 2 == 0 and month < 8) or (month % 2 == 1 and month >= 8)) and date == 30:
    next_date = 1
    next_month = month + 1
    next_year = year
elif ((month % 2 == 1 and month < 8) or (month % 2 == 0 and month >= 8)) and date == 31:
    next_date = 1
    next_month = month + 1
    next_year = year
else:
    next_date = date + 1
    next_month = month
    next_year = year

print(str(next_date) + "-" + str(next_month) + "-" + str(next_year))

# Sample Input
# Enter date: 28-02-2000

# Output
# 29-2-2000
