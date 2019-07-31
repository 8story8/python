import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) # Wednesday

# x = datetime.datetime(2019, 7, 31)
# print(x)

print(x.strftime("%a")) # Wed
print(x.strftime("%w")) # 3(Mon : 1, Tue : 2, Wed : 3, ...)
print(x.strftime("%d")) # 31
print(x.strftime("%b")) # Jul
print(x.strftime("%B")) # July
print(x.strftime("%m")) # 07
print(x.strftime("%y")) # 19(2019)
print(x.strftime("%Y")) # 2019
print(x.strftime("%H")) # 15(Hour, 00 ~ 23)
print(x.strftime("%I")) # 03(Hour, 00 ~ 12)
print(x.strftime("%p")) # PM(AM/PM)
print(x.strftime("%M")) # 37(Min, 00 ~ 59)
print(x.strftime("%S")) # 09(Sec, 00 ~ 59)
print(x.strftime("%f")) # 703079(Microsecond, 000000 ~ 999999)
print(x.strftime("%z")) # (UTC offset)
print(x.strftime("%Z")) # (Timezone)
print(x.strftime("%j")) # 212(Day number of year, 001 ~ 366)
print(x.strftime("%U")) # 30(Week number of year, Sunday as the first day of week, 00 ~ 53)
print(x.strftime("%W")) # 30(Week number of year, Monday as the first day of week, 00 ~ 53)
print(x.strftime("%c")) # Wed Jul 31 15:37:09 2019(Local version of date and time)
print(x.strftime("%x")) # 07/31/19(Local version of date)
print(x.strftime("%X")) # 15:37:09(Local version of time)
print(x.strftime("%%")) # %(% as character)
