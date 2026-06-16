# to know how many days in a month

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap_year(year):
    return year%4 == 0 and (year%100 == 0 or year%4 == 0)


def month_year(year, month):
    if not 1 <= month <= 12:
        return "Invalid month"
    if month == 2 and is_leap_year(year):
        return f"There are 29 days in the {month} month of the year {year}"
    return f"There are {month_days[month]} days in the {month} month of the year {year}"
    
year = int(input())
month = int(input())

print(month_year(year,month))