

#====================База====================
print("\n=== 1. Basic Data Types ===")

#Int (целое число)
x = 10
y = 0b1010  #бинарное представление
z = 0o12    #восьмеричное
w = 0xA     #шестнадцатеричное

print(f"Integer: {x} (type: {type(x)})")
print(f"Binary: {bin(x)} | Octal: {oct(x)} | Hex: {hex(x)}")
print(f"0b1010 = {0b1010} | 0o12 = {0o12} | 0xA = {0xA}")

#float
pi = 3.1415926535
scientific = 2.5e-3  
#0.0025

print(f"\nFloat: {pi:.2f} (type: {type(pi)})")  # округляем до 2 знаков
print(f"Scientific: {scientific} -> {scientific:.4f}")

#string
name = "Alice"
multiline = """Это
многострочная
строка"""
raw_string = r"C:\new_folder\temp"  # сырая строка

print(f"\nString: {name} (type: {type(name)})")
print(f"Multiline: {multiline}")
print(f"Raw string: {raw_string}")

#Boolean(логический тип)

is_active = True
print(f"\nBoolean: {is_active} (type: {type(is_active)})")
print(f"10 > 5: {10 > 5} | 10 == 5: {10 == 5}")

# ==================== Коллекции====================
print("\n===Collections=============")

#List
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "two", 3.0, True, None]
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

print(f"\nList: {numbers} (type: {type(numbers)})")
print(f"Mixed list: {mixed_list}")
print(f"Matrix[1][2]: {matrix[1][2]}")  #доступ к элементу 

#list methods

numbers.append(6)
numbers.insert(0, 0)
print(f"After append/insert: {numbers}")
print(f"Sliced [1:4:2]: {numbers[1:4:2]}")  #с шагом 2

#tuple (кортеж)
coordinates = (10.0, 20.0)
single_element = (42,)  #кортеж из одного элемента

print(f"\nTuple: {coordinates} (type: {type(coordinates)})")
print(f"Single element tuple: {single_element}")

#dict
person = {
    'name': 'Bob',
    'age': 25,
    'skills': ['Python', 'SQL', 'Git']
}
print(f"\nDictionary: {person} (type: {type(person)})")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")

#set(множество)
unique_numbers = {1, 2, 3, 3, 2}
set_from_list = set([1, 2, 2, 3, 4])

print(f"\nSet: {unique_numbers} (type: {type(unique_numbers)})")
print(f"Set from list: {set_from_list}")
print(f"Union: {unique_numbers.union({4, 5})}")

# ====================Специальные типы===============================
print("\n===Special Types===")

#NoneType
empty_value = None
print(f"\nNone: {empty_value} (type: {type(empty_value)})")

#Bytes and Bytearray
data = b'hello'
mutable_data = bytearray(data)

print(f"\nBytes: {data} (type: {type(data)})")
print(f"Bytearray: {mutable_data} (type: {type(mutable_data)})")

#frozenSet(неизменяемое множество)
frozen = frozenset([1, 2, 3])
print(f"\nFrozenSet: {frozen} (type: {type(frozen)})")

# ====================Проверка и преобразование типов====================
print("\n===Type Checking & Conversion===")

#Type checking
values = [42, "42", 42.0, True, None, [42], (42,), {42}]
print("\nType checking:")
for v in values:
    print(f"{str(v):<6} is {type(v).__name__}")


print("\nType conversion examples:")
print(f"int('1010', 2) = {int('1010', 2)}")# из двоичной
print(f"float('3.14') = {float('3.14')}")
print(f"str(3.14) = {str(3.14)}")
print(f"list('hello') = {list('hello')}")
print(f"tuple([1,2,3]) = {tuple([1,2,3])}")
print(f"set([1,2,2,3]) = {set([1,2,2,3])}")
print(f"dict([('a',1),('b',2)]) = {dict([('a',1),('b',2)])}")


# Работа с валютой
price = 19.99
quantity = 3
total = price * quantity
print(f"\nCurrency: ${total:.2f}")#форматирование валюты

#Парсинг данных
data_string = "name=John;" \
"age=30;" \
"city=New York"
parsed_data = dict(item.split("=") for item in data_string.split(";"))
print(f"\nParsed data: {parsed_data}")

#генерация данных
squares = [x**2 for x in range(1, 6)]
print(f"\nSquares: {squares}")

#фильтрация данных
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"\nEven numbers: {even_numbers}")

print("\n===Experiments===")

"""
#Изменение mutable vs immutable
print("\nMutable vs Immutable:")
a = [1, 2, 3]
b = a
b.append(4)
print(f"a = {a} | b = {b}")  
#изменятся оба

x = 5
y = x
y += 1
print(f"x = {x} | y = {y}")  
# x не изменится

#Неожиданное поведение
print("\nUnexpected behaviors:")
print(0.1 + 0.2 == 0.3)  
# False из-за погрешности float
print(1_000_000_000_000_000_000 > 10**18)  
#true или False?

#Работа с памятью
import sys
print("\nMemory usage:")
print(f"Int 10: {sys.getsizeof(10)} bytes")
print(f"float 3.14: {sys.getsizeof(3.14)} bytes")
print(f"string 'hello': {sys.getsizeof('hello')} bytes")
print(f"list [1,2,3]: {sys.getsizeof([1,2,3])} bytes")
"""

print("\n===END===")