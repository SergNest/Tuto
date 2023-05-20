from datetime import datetime


def get_str_date(date):    
    d = date.replace(' ', 'T')
    d = datetime.fromisoformat(d)
    return d.strftime("%A %d %b %Y")


print(get_str_date('2021-05-27T17:08:34.149Z'))
                # 2023-05-19T16:32:57.759058