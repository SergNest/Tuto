from datetime import datetime


def get_days_from_today(date):
    listdate = date.split('-')
    current_datetime = datetime.now()
    new_date = datetime(year=int(listdate[0]), month=int(listdate[1]), day=int(listdate[2]))
    res = current_datetime - new_date
    return res.days
    

print(get_days_from_today("2021-10-09"))