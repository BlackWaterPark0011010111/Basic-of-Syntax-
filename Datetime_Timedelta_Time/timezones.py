"""Task 1: Convert birthday from German time to New Zealand time
Я использовала tz.gettz() для установки часового пояса для Берлина (Europe/Berlin), 
и потом перевела его на время Новой Зеландии (Pacific/Auckland).

I used tz.gettz() to set the timezone for Berlin (Europe/Berlin),
and then converted it to New Zealand time (Pacific/Auckland).

Task 2: Meeting at 13:35 Moscow time with international team
Создаем объект datetime для времени встречи в Москве (Europe/Moscow), 
и переводим его в часовые пояса для местоположений каждого члена команды, используя astimezone().

creating a datetime object for the meeting time in Moscow (Europe/Moscow),
and convert it to the time zones for each team member's location using astimezone().
"""
# Dublin / Ireland
# Berlin / Germany
# Johannesburg / South Africa
# San Francisco / USA

"""Task 3: Convert UNIX timestamp to readable date
Здесь используем fromtimestamp(), чтобы преобразовать UNIX-временную метку в читабельный формат для даты
Here, with using fromtimestamp() to convert the UNIX timestamp into a readable date format.

"""

from datetime import datetime
from dateutil import tz
print("--------------------------------------------------------------------1-----")
birthday = datetime(1995, 5, 17, 15, 30, tzinfo=tz.gettz('Europe/Berlin'))
nz_time = birthday.astimezone(tz.gettz('Pacific/Auckland'))
print("Birthday in New Zeeland time: ", nz_time.strftime("%Y-%m-%d %H:%M:%S"))

print("--------------------------------------------------------------------2-----")
moscow_time = datetime(2021, 7, 8, 13, 35, tzinfo=tz.gettz('Europe/Moscow'))
dublin_time = moscow_time.astimezone(tz.gettz('Europe/Dublin'))
print("Irish participants will meet at:", dublin_time.strftime("%Y-%m-%d %H:%M:%S%z"))


berlin_time = moscow_time.astimezone(tz.gettz('Europe/Berlin'))
print("German participants will meet at:", berlin_time.strftime("%Y-%m-%d %H:%M:%S%z"))


johannesburg_time = moscow_time.astimezone(tz.gettz('Africa/Johannesburg'))
print("South African participants will meet at:", johannesburg_time.strftime("%Y-%m-%d %H:%M:%S%z"))


sf_time = moscow_time.astimezone(tz.gettz('America/Los_Angeles'))
print("American participants will meet at:", sf_time.strftime("%Y-%m-%d %H:%M:%S%z"))

print("--------------------------------------------------------------------3-----")
unix_timestamp = 1626430738
date_time = datetime.fromtimestamp(unix_timestamp)
print("Readable date:", date_time.strftime("%m/%d/%Y, %H:%M:%S"))