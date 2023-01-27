from datetime import date, timedelta

def countingSundays(firstYear, lastYear):
    start_date = date(firstYear, 1, 1)
    end_date = date(lastYear, 12, 31)
    delta = end_date - start_date   # returns timedelta
    count_of_sundays = 0

    for i in range(delta.days + 1):
        date_YYYYMMDD = start_date + timedelta(days=i)
        day_of_week_numerical = str(date_YYYYMMDD.weekday)
        day_of_week_full_name = date_YYYYMMDD.strftime('%A')
        year = date_YYYYMMDD.strftime('%Y')
        month = date_YYYYMMDD.strftime('%m')
        day_without_month_or_year = str(date_YYYYMMDD.strftime('%d'))
        if day_of_week_full_name == 'Sunday' and day_without_month_or_year == '01':
            count_of_sundays += 1
    return(count_of_sundays)