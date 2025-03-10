import datetime
from re import findall

tuple1 = (1, 2, 3, "String", False, [0, 2, 4])
print(tuple1)
#print(tuple.count)  #chto delaet

print("---------------------------------------------------------")

# доступ к элементам кортежа
print(tuple1[-1][-1])
print(tuple1[::-1])
print(tuple1[:3])
# создание кортежа с помощью конструктора
tuple2 = tuple("A string that will be turned into a tuple...")
print(tuple2)

list1 = [1, 2, 3, True, False, 4, 5, 6, 7, 8, 9]

# преобразование между кортежем и списком
tuple3 = tuple(list1)  # pomeschaem list iz 1,2 u 3
print("Преобразование списка в кортеж с помощью функции tuple():", tuple3)

print("---------------------------------------------------------")

list2 = list(tuple3)
print("Преобразование списка в кортеж с помощью кортежа(): ", list2)
print("---------------------------------------------------------")

print(tuple3.index(True, 2))  # проверяем индекс "2" и True, из листа, на каком месте она

print("---------------------------------------------------------")

# счет элементов внутри кортежа
print(tuple3.count(3))

print("------------------------------------------------------2---")

# смотрим сколько элементов в списке
print(len(tuple3))

print("The amount of all elements inside a tuple list: ", len(tuple3))
print("------------------------------------------------------3---")

# проверка уникальных значений $$$$$$chto znachit unique values$$$$$$$$
uniqueValues = set(tuple3)
print(uniqueValues)
print("There are " + str(len(uniqueValues)) + " unique, non-duplicated values")
# list v tuple eto nehashiruemyi list i esli dobavit list v list budet oshibka
# mu ne mozhem dobavlyat slovar(dictionary), v spisok kotoryi stal tuple
# i my ne mozhem dobavlyat list v list kotoryi stal tuple
tuple4 = ([12, 2, 3, 4], [5, 6, 7])  # mu mozhem sozdat list v tuple
# no ne mozhem izmenyat ego na list
print(tuple4.count([12, 2, 3, 4]))
print("---------------------------------------------------------")

single = (False,)  # koma prevraschaet v tuple
print(type(single))
print("---------------------------------------------------------")

single = {False}
print(type(single))
print("---------------------------------------------------------")

single1 = (1, 2, 3)
single2 = (1, 2, 3)  # хэшируемые выводы коллекции
print(single1 == single2)
print(single1 is single2)
print(id(single1))
print(id(single2))

print("---------------------------------------------------------")

# список не является хэшируемым, так как список может быть изменен
# Кортежи хэшируются, так как они неизменяемы

# Поменять местами две переменные внутри кортежа, используя распаковку кортежа
simpletuple = (3, 6)
x, y = simpletuple
newtup = (x, y)
print(newtup)

if 3 in simpletuple:
    print("A number exist in a collection ", simpletuple)
else:
    print("The variable is not present in a collection ", simpletuple)

print("---------------------------------------------------------")

# if [1,2] not in single:
#     print("A number exist in a collection ", single)
# else:
#     print("The variable is not present in a collection ", single)

# if "My first" in list1:
#     print("A number exist in a collection ", list1)
# else:
#     print("The variable is not present in a collection ", list1)
print("---------------------------------------------------------")

# Homework
car_brands = ["BMW", "Audi", "Volkswagen"]

for brand in car_brands:
    print(brand)

car_brands.append('Volvo')

car_brands.pop(0)
print(car_brands)

# Создайте переменную с именем fruits и добавьте 
# один за другим элементы Apples, Cherries и Strawberries. Прокрутите список fruits и выведите каждый элемент на экран.

# fruits = ["Apples", "Cherries", "Strawberries"]
# for taste in fruits:
#     print(taste)

cities = ["London", "Paris", "Berlin", "Amsterdam"]
capital = cities[2]  

print(f"The capital city of Germany is: {capital}")

colors = ["cyan", "magenta", "green", "yellow", "black", "white"]
colors.pop(2)
colors.pop(4)
print(colors)

letters = ['p', 'e', 'n', 'g', 'u', 'i', 'n']
penguin = ''.join(letters)  
penguin = penguin.capitalize() 

print(penguin)

import re
string = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

char = ""
for i in string:
    if i.isalpha():
        char = "".join([char, i])
print(str(char))

def intersection(list_1, list_2):
    # Преобразуем списки в множества для быстрого поиска общих элементов
    set_1 = set(list_1)
    set_2 = set(list_2)
    
    # Используем операцию пересечения множеств
    common_elements = set_1.intersection(set_2)
    
    # Преобразуем результат обратно в список
    result = list(common_elements)
    
    return result

list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

result = intersection(list_1, list_2)
print(result)

def colours():
    def red():
        print("red")
    def blue():
        print("blue")
    red()
    blue()
colours()

"""Кортежи подобны спискам, но они не могут быть изменяемыми.
Они являются эквивалентом констант для коллекций и работают быстрее, чем списки.
Они:
- Имеют порядок.
- Допускают дублирование значений.
- Не позволяют изменять свои объекты.
- Разрешают объекты разных типов.

Они определяются с помощью круглых скобок ().
Любая итерируемая переменная может быть преобразована в кортеж с помощью конструктора tuple.
Конструктор кортежей также может быть использован для создания пустых кортежей, если не задан аргумент.
Результат будет таким же, как и при использовании пустых скобок ()"""

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
)
hello = tuple("hello")
print(hello)
('h', 'e', 'l', 'l', 'o')
empty_tuple = tuple()
print(empty_tuple)
()

"""Кортежи могут содержать значения любого типа.
Элементы кортежа могут быть смешанных типов.
Сами элементы также могут быть кортежами"""

fridge = ("Apple", "Apple")
letters = tuple("hello")
ages = (32, 45, 42, 12, 34, 57)
dates = (datetime, datetime)
data = ("John", 32, datetime)
tuples = (
    ("John", "Mary", "Amy"),
    (32, 43, 51)
)
"""Печать кортежа покажет его значения в том же порядке, который использовался при определении кортежа.
К каждому значению кортежа можно получить доступ с помощью его числовой позиции в кортеже (начиная с нуля).
Эта позиция называется индексом.
Нарезка может быть использована для доступа к частям кортежа или изменить его порядок."""

print(days)
#('Monday', 'Tuesday', ...)
print(days[0])
#Monday
print(days[4])
#Friday
print(days[0:2])
#('Monday', 'Tuesday')
print(days[-2:])
#('Thursday', 'Friday')
print(days[::-1])
#('Friday', 'Thursday', ...)

"""Кортежи также имеют метод index, который возвращает индекс первого вхождения заданного значения в кортеже.
Количество вхождений значения можно также получить с помощью метода count."""
print(days.index('Thursday'))
3
print(days[3])
#Thursday
 #print(days.count('Monday'))
1

"""Элементы внутри кортежа не могут быть изменены.
Если элемент кортежа относится к другому типу итерируемого, то его содержимое все равно может быть изменено."""
days[0] = "Sunday""""
Traceback (most recent call last):
File "/home/DCI/test.py", line 71,
in <module>"""
days[0] = "Sunday""""
TypeError: 'tuple' object does not support item assignment"""
days = (["Monday"], ["Tuesday"])
days[0][0] = "Sunday"
days[1].pop()
days[1].append("Monday")
print(days)
#(['Sunday'], ['Monday'])

"""В отличие от списков, кортежи не могут быть изменены.
Поэтому они не имеют ни одного из методов, которые могут быть использованы в списках для манипулирования их содержимым:
- добавить Append
- удалить Pop
- расширить
- вставить Insert
- Вставить Extend
- Удалить Remove
- Сортировать Sort
- Реверс Revers"""

days.append("Saturday")
"""Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'"""
days.pop()
"""Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'pop'"""
days.sort()
"""Traceback (most recent call last):
File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'sort'"""
"""
Сравнение двух кортежей вернет значение True, если следующие утверждения истинны для элементов в нем:
- Они одинаковые
- Они расположены в одинаковом порядке"""
list1 = (1, 2, 3)
list2 = (1, 2, 3)
list1 == list2
True
list1 is list2
False


list3 = (3, 2, 1)
list1 == list3
False
list1 == list3[::-1]
True
list4 = [1, 1, 2, 2, 3, 3]
list1 == list4
False
"""

Кортежи имеют только методы для поиска и анализа значений:
- Index
- Count
"""
