from datetime import timedelta, date


def betweenDays(date1, date2):
    diff = (int((date2-date1).days)+1)
    for day in range(diff):
        yield date1+timedelta(day)


# contoh
start_date = date(2019, 5, 1)
end_date = date(2019, 5, 5)
for dates in betweenDays(start_date, end_date):
    print(dates.strftime("%Y-%m-%d"))
