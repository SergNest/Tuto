from datetime import date


def get_days_in_month(month, year):
    if year % 4 == 0 and month == 2:
        return 29
    elif month == 2:
        return 28
    else:
        new_date = date(year=year, month=month, day=1)
    return new_date.max.day
    

print(get_days_in_month(2, 2022))