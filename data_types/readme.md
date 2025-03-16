Тип данных (Data Type) — это характеристика значения, которая определяет, какие операции можно выполнять с этим значением. В Python есть несколько основных типов данных, которые позволяют хранить и обрабатывать информацию.

Основные типы данных в Python
1. Числовые (Numeric Types)
Используются для работы с числами.

int (целые числа): 10, -5, 1000
float (числа с плавающей точкой): 3.14, -0.01, 2.7e3
complex (комплексные числа): 2 + 3j, -1 - 4j

x = 10       # int
y = 3.14     # float
z = 2 + 3j   # complex
2. Логический (Boolean Type)

bool (булевый тип): принимает только два значения True (истина) или False (ложь).

is_active = True
is_deleted = False
3. Строки (String)
str (строка): последовательность символов, заключенных в кавычки (' ' или " ").

name = "Alice"
message = 'Hello, world!'
Строки поддерживают индексацию и срезы:


text = "Python"
print(text[0])  # P
print(text[-1]) # n
print(text[1:4]) # yth
4. Коллекции (Collections)
Используются для хранения нескольких значений.

4.1. Списки (Lists)
Изменяемая коллекция, в которой могут храниться разные типы данных.

numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", True, 3.14]
4.2. Кортежи (Tuples)

Неизменяемая коллекция.
coordinates = (10.5, 20.3)
days = ("Monday", "Tuesday", "Wednesday")
4.3. Множества (Sets)
Коллекция уникальных элементов.

unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # {1, 2, 3, 4}



4.4. Словари (Dictionaries)
Коллекция пар "ключ-значение".

user = {
    "name": "Alice",
    "age": 25,
    "city": "Berlin"
}
print(user["name"])  # Alice

5. NoneType
None используется для обозначения отсутствия значения.

result = None
Вывод типа данных
Python позволяет узнать тип переменной с помощью функции type():


print(type(10))      
print(type(3.14))       
print(type("Hello"))    
print(type(True))       
print(type([1, 2, 3]))  

A data type is a characteristic of a value that determines what operations can be performed on that value. Python has several basic data types that allow you to store and process information.

Basic Data Types in Python
1. Numeric Types
Used to work with numbers.

int (integers): 10, -5, 1000
float (floating point numbers): 3.14, -0.01, 2.7e3
complex (complex numbers): 2 + 3j, -1 - 4j

x = 10 # int
y = 3.14 # float
z = 2 + 3j # complex
2. Boolean Type

bool: takes only two values ​​True or False.

is_active = True
is_deleted = False
3. Strings
str: a sequence of characters enclosed in quotation marks (' ' or " ").

name = "Alice"
message = 'Hello, world!'
Strings support indexing and slicing:


text = "Python"
print(text[0]) # P
print(text[-1]) # n
print(text[1:4]) # yth
4. Collections
Used to store multiple values.

4.1. Lists
A mutable collection that can store different types of data.

numbers = [1, 2, 3, 4, 5]
mixed = [10, "hello", True, 3.14]
4.2. Tuples

An immutable collection.
coordinates = (10.5, 20.3)
days = ("Monday", "Tuesday", "Wednesday")
4.3. Sets
A collection of unique elements.

unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers) # {1, 2, 3, 4}
4.4. Dictionaries
A collection of key-value pairs.

user = {
"name": "Alice",
"age": 25,
"city": "Berlin"
}
print(user["name"]) # Alice

5. NoneType
None is used to indicate the absence of a value.

result = None
Data Type Inference
Python allows you to find out the type of a variable using the type() function:

print(type(10))      
print(type(3.14))       
print(type("Hello"))    
print(type(True))       
print(type([1, 2, 3]))  
