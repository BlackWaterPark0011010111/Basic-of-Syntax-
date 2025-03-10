from datetime import datetime

print("Task 1: Get current datetime and print the current year")
current_datetime = datetime.now()
print(current_datetime.year)

print("# Task 2: Get the weekday of a specific date")
some_date = datetime(2021, 7, 14)
print(some_date.weekday())

print("Task 3: Check if a year is a leap year")
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year_to_check = 2021
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year")
else:
    print(f"{year_to_check} is not a leap year")

print("Task 4: Convert a string into a datetime object")
date_as_string = "Feb 14 2021 8:30AM"
date_obj = datetime.strptime(date_as_string, "%b %d %Y %I:%M%p")
print(date_obj)
"""
Task 1: Здесь нам нужно использовать метод datetime.now() чтобы получить текущую дату и время, 
а печатаем только текущий год с current_datetime.year.
Task 2: чтобы узнать какой день недели на конкретной дате (указано 14 июля 2021), мы используем метод .weekday(). 
Это возвращает число от 0 (понедельник) до 6 (воскресенье).
Task 3: является ли год високосным,  функция is_leap_year() использует условия, описанные в календарных правилах.
Task 4: здесь нужно взять datetime.strptime() для того, чтобы преобразовать строку с датой, в объект datetime.
мы указываем формат строки, для Python, чтобы он знал , как её интерпретировать.
."""


"""Task 1: Here, we need to use the method datetime.now() to get the current date and time, and then print only
 the current year with current_datetime.year.
Task 2: To find out what day of the week a specific date is (for example, July 14, 2021), we use the method 
.weekday(). It returns a number from 0 (Monday) to 6 (Sunday).
Task 3: To check if a year is a leap year, the function is_leap_year() uses rules described in the calendar
 system.
Task 4: Here, we use datetime.strptime() to convert a string with a date into a datetime object.
 We provide the string format for Python so it knows how to interpret it."""