"""Итерационные таблицы, как следует из названия, используются 
для одной основной цели - итерации.
Существует также целый ряд встроенных 
функций, для которых итерации требуются в качестве 
аргументов.
Список строк может быть итерирован для доступа к 
к каждому из его значений, а функция len
может быть использована для получения значения 
количество элементов в переданной итерируемой таблице 
(в данном случае - строке).
То же самое относится к любому типу 
итерируемых."""

"""Iteration tables, as the name suggests, are used 
for one main purpose - iteration. 
There are also a number of built-in 
functions that require iterations as 
arguments. 
A list of strings can be iterated over to access 
each of its values, and the len function can be used to 
get the number of elements in the passed iterable 
(in this case, a string).
The same applies to any type of iterable."""
from numpy import iterable


iterables_list = [
     "string", "list", "set",
     "tuple", "dictionary"
 ]
for item in iterables_list:
 print(item, len(item))

"""string 6
    list 4
    set 3
    tuple 5
dictionary 10"""


"""
Словари - это особый случай, поскольку каждый элемент является составным 
ключа и значения.Итератор словаря выдает только ключ.Это имеет тот же эффект, что и 
использование метода keys метода словаря. Этот метод выдает ключ каждого элемента в 
словаря.Словари имеют и другие методы для получения значений
Dictionaries are a special case, since each element is a composite of a key and a 
value. A dictionary iterator yields only the key. This has the same effect as using the 
keys method of a dictionary. This method yields the key of each element in the dictionary. 
Dictionaries have other methods to get values
"""
profile = {     "name": "Mary Schmidt",     "age": 54 }
for key in iterable:     print(key)

"""name
age"""
for key in iterable.keys():
     print(key)

"""name
age
"""

"""
Method values ​​yields the values ​​of each element. The items method yields a tuple a tuple 
containing the key and value of each element This tuple can be unpacked in the same for 
statement to make the code more readable
Значения метода выдает значения каждого элемента.Метод items выдает кортеж 
кортеж, содержащий ключ и значение каждого элементаЭтот кортеж может быть распакован в 
той же инструкции for, чтобы сделать код более читабельным"""
for value in iterable.values():
     print(value)

#Mary Schmidt
#54
for item in iterable.items():
     print(item)

#('name', 'Mary Schmidt')
#('age', 54)
for key, value in iterable.items():
     print(key, "=>", value)

#name => Mary Schmidt
#age => 54




"""

Другой распространенной схемой является использование кортежей 
вместо словарей для хранения пар ключ-значениепар, которые должны оставаться постоянными. Это 
можно сделать, определив двумерный кортеж (кортеж кортежей).В результате итерации будет получен 
кортеж, который можно распаковать, как это делается в методе itemsметод словаря
Another common scheme is to use tuplesinstead of dictionaries to store key-value pairs
that should remain constant. This can be done by defining a two-dimensional tuple 
(a tuple of tuples).The result of the iteration will be a tuple, which can beunpacked as 
is done in the items method of a dictionary
"""

days = (
     ('Mon', 'Monday'),
     ('Tue', 'Tuesday'),
     ('Wed', 'Wednesday'),
     ('Thu', 'Thursday'),
     ('Fri', 'Friday'),
     ('Sat', 'Saturday'),
     ('Sun', 'Sunday')
 )
for key, value in days:
    print(key, "=>", value)

#Mon => Monday
#Tue => Tuesday
# continues



"""

В Python есть несколько встроенных функций, которые требуют или принимают итерации и могут быть 
очень Список, кортеж, dict и set - вот некоторые из них.Еще одной из наиболее часто используемых 
функций является enumerate.Функция enumerate принимает любую итерируемую переменную и для каждого
 значения выдает кортеж, содержащий позицию этого значения и само значение само значение.
 Python has several built-in functions that require or accept iterations and can be very 
List, tuple, dict and set are some of them. Another of the most commonly used functions is 
enumerate. The enumerate function takes any iterable variable and for each value, it produces 
a tuple containing the position of that value and the value the value itself"""

list = [
     'Monday',
     'Tuesday',
     'Wednesday',
     'Thursday',
     'Friday',
     'Saturday',
     'Sunday'
 ]
for position, value in enumerate(list):
    print(position, "=>", value)

#0 => Monday
#1 => Tuesday
# continues




"""
Функция enumerate позволяет сделать более простой и более читабельный код по сравнению с 
альтернативой добавления счетчика вручную
The enumerate function allows for simpler and more readable code than the alternative of 
manually adding a counter."""
list = [
     'Monday',
     'Tuesday',
     'Wednesday',
     'Thursday',
     'Friday',
     'Saturday',
     'Sunday'
 ]
sition = 0
for value in list:
    print(position, "=>", value)
    position += 1

"""> Monday
> Tuesday
continue"""

"""функция enumerate позволяет сделать более простой 
более читабельный код по сравнению с альтернативой 
авления счетчика вручную
the enumerate function allows for simpler, more readable code than the alternative of 
manually setting the counter
"""
t = [
     'Monday',
     'Tuesday',
     'Wednesday',
     'Thursday',
     'Friday',
     'Saturday',
     'Sunday'
 ]
sition = 0
for value in list:
    print(position, "=>", value)
    position += 1

"""> Monday
> Tuesd
""""""

Функция enumerate может даже можно использовать даже для итераций, которые дают итераторы, 
например, метод items словаря.Эта итерабельность может быть дополнительно 
распаковать с помощью круглых скобок
The enumerate function can even be used for iterables that yield iterators, 
for example, the items method of a dictionary. This iterability can be further 
unpacked using parentheses"""
dict = {
     "name": "Mary Schmidt",
     "age": 54
 }
for position, value in enumerate(dict.items()):
    print(position, "=>", value)

"""0 => ('name', 'Mary Schmidt')
1 => ('age', 54)"""
for pos, (key, val) in enumerate(dict.items()):
    print(pos, ".", key, "=>", val)

"""0 . name => Mary Schmidt
1 . age => 54

"""

"""

Функция zip принимает любое количество итераций и возвращает объект zip.Этот объект представляет 
собой итератор, который выдает кортеж со значением в в каждой позиции каждой переданной итератора.
The zip function takes any number of iterations and returns a zip object. This object is an 
iterator that yields a tuple with the value at each position of each passed iterator."""
nums = [1, 2, 3]
eng = ("one", "two", "three")
zip1 = zip(nums, eng)
print(zip1)
"""<zip object at 0x7ff4f285cd80>"""
for item in zip(nums, eng):
    print(item)

"""(1, 'one')
(2, 'two')
(3, 'three')"""




"""An iterable of any type (and any 
number) can be passed to the 
function. 
Note that sets can be passed too, but since they have no order 
the elements are extracted randomly. 
Each time we execute this code 
the German words will appear in a 
different order"""
"""
Итерабельность любого типа (и любого 
количество) может быть передано в функцию 
функции.
Обратите внимание, что можно передавать и множества 
тоже, но поскольку они не имеют порядка 
элементы извлекаются случайным образом.
Каждый раз, когда мы выполняем этот код 
немецкие слова будут появляться в 
разном порядке
"""
nums = "123"
eng = ("one", "two", "three")
deu = {"ein", "zwei", "drei"}
cat = {"un": 1, "dos": 2, "tres": 3}
fra = ["un", "deux", "trois"]
for item in zip(nums, eng, deu, cat, fra):
    print(item)

('1', 'one', 'zwei', 'un', 'un')
('2', 'two', 'drei', 'dos', 'deux')
('3', 'three', 'ein', 'tres', 'trois')






"""
Items can also be 
unpacked to provide more readable 
code inside the loop.
"""
"""
Предметы также могут быть 
распаковывать, чтобы обеспечить 
более читабельный 
код внутри цикла.
"""
nums = "123"
eng = ("one", "two", "three")
deu = {"ein", "zwei", "drei"}
cat = {"un": 1, "dos": 2, "tres": 3}
fra = ["un", "deux", "trois"]
for num, en, de, ca, fr in zip(nums, eng, deu, cat, fra):
    print(str(num) + ". " + en + ", " + de + ", " + ca + ", " + fr)
"""
1. one drei un un
2. two zwei dos deux
3. three ein tres trois"""

nums = [1, 2, 3, 4, 5]
print(sum(nums), max(nums), min(nums))
#15 5 1
nums = {1, 2, 3, 4, 5}
print(sum(nums), max(nums), min(nums))
#  15 5 1
nums = [1, 2, 3, 4, "5"]
print(sum(nums), max(nums), min(nums))
"""Traceback (most recent call last):
File "/home/DCI/test.py", line 30, in <module>"""
print(sum(nums), max(nums), min(nums))
"""TypeError: unsupported operand type(s) for +: 
'int' and 'str'"""
nums = ["a", "b", "c", "d", "e"]
print(max(nums), min(nums))
# -----e a




"""Функция sorted возвращает новый список в 
алфавитном или числовом порядке. 
Она не изменяет существующий итерируемый список.
Сортировка словаря с помощью sorted вернет 
список с ключами в алфавитном порядке, 
поскольку по умолчанию словарь итерируется 
по ключу.
Получить отсортированный список значений можно 
с помощью метода values.
Он принимает аргумент ключевого слова 
reverse как булево значение, которое по умолчанию равно False"""
"""The sorted function returns a new list in 
alphabetical or numerical order. 
It does not modify the existing iterable. 
Sorting a dictionary with sorted will return a 
list with keys in alphabetical order, 
since the dictionary is iterated by key by default. 
You can get a sorted list of values ​​
using the values ​​method. 
It takes the keyword argument 
reverse as a boolean value, which defaults to False"""
nums = [4, 3, 5, 2, 1]
print(sorted(nums))
#[1, 2, 3, 4, 5]
print(nums)
#[4, 3, 5, 2, 1]
dict1 = {"c": 2, "b": 1, "a": 3}
print(sorted(dict1))
#['a', 'b', 'c']
print(sorted(dict1.values()))
#[1, 2, 3]
print(sorted(dict1, reverse=True))
#['c', 'b', 'a']


"""Функция sorted также может быть использована 
для сортировки списков словарей 
списка на основе значений одного из 
ключей этих словарей.
Это можно сделать, передав в качестве ключевого аргумента функцию 
функции в качестве ключевого аргумента. Эта 
функция должна возвращать значение, которое 
которое будет использоваться для сортировки.
"""
"""The sorted function can also be used to sort lists of dictionaries
list based on the values ​​of one of the keys of those dictionaries.
This can be done by passing a function
function as a keyword argument. This function must return a value that will be used for sorting.
"""
dict1 = [
     {"name": "John", "age": 31},
     {"name": "Mary", "age": 46},
     {"name": "Lucy", "age": 25}
 ]
 
by_age = lambda user: user["age"]
by_name = lambda user: user["name"]
print(sorted(dict1, key=by_age))
[{'name': 'Lucy', 'age': 25}, {'name': 'John', 
'age': 31}, {'name': 'Mary', 'age': 46}]
print(sorted(dict1, key=by_name))
[{'name': 'John', 'age': 31}, {'name': 'Lucy', 
'age': 25}, {'name': 'Mary', 'age': 46}]



"""Некоторые функции используют итерируемые таблицы для возврата значения 
булево значение, указывающее, соответствует ли итерабель 
соответствует определенному условию.
Функция any вернет True только в том случае, если 
любое из значений в итерабельной таблице является 
истинным.
Функция all возвращает True только в том случае, если 
все значения в итерируемой таблице являются истинными.
"""
"""Some functions use iterables to return a 
boolean value indicating whether the iterable 
meets a certain condition. 
The any function will return True only if 
any of the values ​​in the iterable is true. 
The all function will return True only if 
all of the values ​​in the iterable are true."""
a_list = [1, True, "Mary", {1, 2}]
print(bool(a_list), any(a_list), all(a_list))
#True True True
a_list = [1, True, "Mary", {}]
print(bool(a_list), any(a_list), all(a_list))
#True True False
a_list = [0, False, "", {}]
print(bool(a_list), any(a_list), all(a_list))
#True False False



"""
Некоторые функции, использующие итерируемые таблицы, возвращают 
булево значение, указывающее, соответствует ли итерабель 
соответствует определенному условию.
Функция any возвращает значение True только в том случае, если 
любое из значений в итерабельной таблице является 
истинным.
Функция all возвращает True только в том случае, если 
все значения в итерируемой таблице являются истинными
"""
"""Some functions that use iterables return a 
Boolean value indicating whether the iterable 
meets a certain condition. 
The any function returns True only if 
any of the values ​​in the iterable is true. 
The all function returns True only if 
all of the values ​​in the iterable are true. 
"""""
a_list = [1, True, "Mary", {1, 2}]
print(bool(a_list), any(a_list), all(a_list))
#True True True
a_list = [1, True, "Mary", {}]
print(bool(a_list), any(a_list), all(a_list))
#True True False
a_list = [0, False, "", {}]
print(bool(a_list), any(a_list), all(a_list))
#True False False
"""
Some functions use iterables to return a 
boolean value indicating if the iterable 
matches a certain condition.
The function any will return True only if 
any of the values in the iterable is 
truthy.
The function all will return True only if 
all the values in the iterable are truthy"""




"""
Наиболее распространенные функции в 
Наиболее распространенные функции в функциональном программировании требуют как 
итерабельность и функция.
Так обстоит дело с функцией map, которая 
применяет заданную функцию к каждому 
элементу заданной итерируемой таблицы.
Она возвращает объект map, который представляет собой 
итерируемый объект, содержащий вывод данного 
процесс"""
"""The most common functions in 
The most common functions in functional programming require both an 
iterable and a function. 
This is the case with the map function, which 
applies a given function to each 
element of a given iterable table. 
It returns a map object, which is an 
iterable object containing the output of the given 
process"""
_list = [1, 2, 3, 4, 5]
by_two = lambda num: num * 2
a_list_by_two = map(by_two, a_list)
print(a_list_by_two)
"""<map object at 0x7f11957546d0>
 print(list(a_list_by_two))
[2, 4, 6, 8, 10]
"""

"""

Функция filter возвращает итерабельную переменную 
с элементами заданного итерабля 
которые соответствуют условию, заданному в 
функции.
Она возвращает объект filter, который представляет собой 
итерируемый объект, содержащий вывод данного 
процесс"""
"""The filter function returns an iterable 
with the elements of the given iterable 
that match the condition specified in the 
function. 
It returns a filter object, which is an 
iterable containing the output of the given 
process"""
nums = [1, 2, 3, 4, 5]
is_odd = lambda num: (num % 2) != 0
odds = filter(is_odd, nums)
print(odds)
#<filter object at 0x7fced01036d0>
print(list(odds))
[1, 3, 5]





"""CONSTRUCTORS
- list()
- tuple()
- set()
- dict()
PACKING
- enumerate()
- zip()
REDUCE
- sum()
- max()
- min()
ORDER
- sorted()
BOOLEAN
- any()
- all()
FUNCTIONAL
- map()
- filter()
"""