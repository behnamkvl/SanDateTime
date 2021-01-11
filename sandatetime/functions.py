from datetime import timedelta
from persiantools.jdatetime import JalaliDateTime, JalaliDate
import pytz
import time


one_hour_in_ms = 60 * 60 * 1000
one_day_in_ms = one_hour_in_ms * 24
get_current_epoch = lambda : int(round(time.time() * 1000))
get_tehran_tzinfo_by_epoch = lambda e: JalaliDateTime.fromtimestamp(e//1000, pytz.timezone("Asia/Tehran")).tzinfo # will be used indirectly and by other functions
now = JalaliDateTime.now(tz=get_tehran_tzinfo_by_epoch(get_current_epoch()))

jalali_to_gregorian = lambda j: j.to_gregorian().date() # needed when using plotly

epoch_to_jalali = lambda e: JalaliDateTime.fromtimestamp(e/1000, tz=get_tehran_tzinfo_by_epoch(e)) 

def utc_date_to_jalali(year, month, day):
    return JalaliDate.to_jalali(year, month, day)

def jalali_to_epoch(year, month, day=1, hour=0, minute=0, second=0, milliseconds=0):
    tehran_tzinfo = get_tehran_tzinfo_by_epoch(int(JalaliDateTime(year, month, day, hour, minute, second, milliseconds*1000).timestamp() * 1000))
    return int(JalaliDateTime(year, month, day, hour, minute, second, milliseconds*1000, tzinfo=tehran_tzinfo).timestamp() * 1000)

today_epoch = jalali_to_epoch(now.year, now.month, now.day)
# ---------------------------------------------------------
def back_days_epoch(n):
    d = now - timedelta(days = n)
    e = jalali_to_epoch(d.year, d.month, d.day)
    x = epoch_to_jalali(e)
    if x.hour == 23:
        e += one_hour_in_ms
    return e

#----------------------------------------------------------
def get_months():
    months = []
    now_epoch = get_current_epoch()
    year = 1396
    month = 1    
    flag = True
    while flag:
        start = jalali_to_epoch(year, month)    
        name = '{}/{}'.format(year, month) if month > 9 else '{}/0{}'.format(year, month)
        month += 1
        if month > 12:
            month = 1
            year += 1
        end = jalali_to_epoch(year, month)
        if end > now_epoch:
            flag = False
        months.append((start, end, name ))
    return months

# ---------------------------------------------------------
def get_last_wednsday_jalali_epoch():
    offset_jalali = (now.weekday() - 4) % 7
    if offset_jalali == 0:
        offset_jalali = 7
    e = today_epoch - offset_jalali * one_day_in_ms
    x = epoch_to_jalali(e)
    assert x.hour == 0 and x.minute == 0 and x.microsecond == 0
    return e

# ---------------------------------------------------------
def gregorian_date_to_jalali_epoch(datetime_date):
    j_date = utc_date_to_jalali(datetime_date.year, datetime_date.month, datetime_date.day)
    return jalali_to_epoch(j_date.year, j_date.month, j_date.day)

# ---------------------------------------------------------