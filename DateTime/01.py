import datetime
from datetime import timedelta

# date = datetime.date(2025, 11, 12)

# today = datetime.date.today()

# print(today)
# print(today.year)
# print(today.month)
# print(today.day)
# print(type(date))


# time = datetime.time(14,12,34)
# print(type(time))
# print(time)
# print(time.hour)
# print(time.minute)
# print(time.second)'


# datetime = datetime.datetime(2025, 9, 12, 23, 12, 9)
# print(datetime)
# print(datetime.year)
# print(datetime.month)
# print(datetime.day)
# print(datetime.hour)
# print(datetime.minute)
# print(datetime.second)

# today = datetime.datetime.now()
#
# print(today)
# print(today.time())
# print(today.date())
#
# today = datetime.datetime.now()
# print(today)
#
# last_week = today-timedelta(days=7)
# print(last_week)

# next_ten_days = today+timedelta(days=10)
# print(next_ten_days)
#
#
# now = datetime.now()
#
# str_date_now = now.strftime("%Y-%m-%d %H:%M:%S")
# print(type(str_date_now))
# time = now.strftime("%d/%m/%Y")
# print(type(time))
# print(now.strftime("%A"))  # نام روز هفته


from datetime import date

d1 = date(2025, 11, 9)
d2 = date(2025, 12, 25)

delta = d2 - d1
print("اختلاف روزها:", delta.days)
