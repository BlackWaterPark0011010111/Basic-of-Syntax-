from datetime import datetime
import datetime #импортируем модуль сначала 
import calendar
import pytz

from datetime import datetime,timedelta # импортируем timedata

print(dir(datetime))

#print(datetime.datetime.now())# смотрим время сдесь и сейчас
 

import datetime as dt #мы меняем имя дататайп на dt


print(dt.datetime.now())
x = dt.datetime.now()


x = dt.datetime(2000, 3, 4)
print(dir(dt))

#simple date/time information extraction
print(x)
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)

print(x.strftime('%A'))
print(x.strftime('%B'))
print(x.strftime('%U'))
print(x.strftime('%m'))
print(x.strftime('%A'))
print(x.strftime('%F'))
print(x.strftime('%x')) #enforce american date format


#time delta or time difference
new_date = x+timedelta(days=365)
new_time = x -timedelta(hours=20)
print(new_date)
print(new_time)

#Date comparisons
y = datetime.now()
if x ==y:
    print('Datetime objects are the same')
else:
    print('Well, they aren`t the same')

    #Time information

    timezones = pytz.all_timezones
    print(timezones)

    z = datetime(2028,9,29,12,4,33, tzinfo=pytz.UTC)
    z = datetime(2028,9,29,12,4,33, tzinfo=pytz.timezone('Zulu'))
    print(x)
print("---------------------------------------------------1---")

print(dir(calendar))
print("---------------------------------------------------1---")

cal = calendar.month(2023, 9)
print(cal)
#check if a year is a leap year e.g. 2024
leap = calendar.isleap(2024)
print(leap)
print(pytz.utc)
pytz.timezone('US/Central')


# current Datetime
unaware = datetime.now()
print('Timezone naive:', unaware)

# Standard UTC timezone aware Datetime
aware = datetime.now(pytz.utc)
print('Timezone Aware:', aware)

# US/Central timezone datetime
aware_us_central = datetime.now(pytz.timezone('US/Central'))

print("US Central DateTime", aware_us_central.strftime(" %H, %Y, %B"))


some_date = datetime(2021, 7, 14)

print(some_date)