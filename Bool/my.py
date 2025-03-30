print("\n-----------------------------------------------------------------------1-----")
# булевы операции - самые основы
x = True
y = False

# базовые операции
print("x and y:", x and y)  # False
print("x or y:", x or y)    # True
print("not x:", not x)      # False

# print("x xor y:", x ^ y)  
# print("y == (not x):", y == (not x))  

print("\n-----------------------------------------------------------------------2-----")
# сравнения и булевы значения
a = 5
b = 10

print("a < b:", a < b)  
print("a == b:", a == b)
print("a != b:", a != b)

# print("(a < b) and (a != b):", (a < b) and (a != b))  
# print("(a > b) or (a == 5):", (a > b) or (a == 5))    

print("\n-----------------------------------------------------------------------3-----")
# приведение к bool
values = [0, 1, "", "hello", None, [], [1,2,3]]

print("Проверка значений на истинность:")
for v in values:
    # print(f"{str(v):<6} ->", bool(v))
    if v:
        print(f"{str(v):<6} -> True")  # с форматированием
    else:
        print(f"{str(v):<6} -> False")


print("\n-----------------------------------------------------------------------4-----")
# работа с None
var1 = None
var2 = 42

print("var1 is None:", var1 is None)   
print("var2 is not None:", var2 is not None)  

# if var1:
#     print("var1 имеет значение")  #не выполнится
# else:
#     print("var1 пустое")  #выполнится

print("\n-----------------------------------------------------------------------5-----")
# булевы выражения с in
fruits = ["apple", "banana", "orange"]

print("'apple' in fruits:", "apple" in fruits)  
print("'pear' not in fruits:", "pear" not in fruits)  

# print("'apple' in fruits and len(fruits) > 2:", "apple" in fruits and len(fruits) > 2) 

print("\n-----------------------------------------------------------------------6-----")
# короткие вычисления (short-circuit)
def check(x):
    print("check выполнен для", x)
    return x

# print(check(False) and check(True))  
# print(check(True) or check(False))   

print("\n-----------------------------------------------------------------------7-----")
# булевы операции с числами
n1 = 0
n2 = 7

# числа в булевом контексте
print("bool(n1):", bool(n1))  
print("bool(n2):", bool(n2))  

# print("n1 and n2:", n1 and n2)  # 0 возвращает последний операнд
# print("n1 or n2:", n1 or n2) 
# print("not n1:", not n1)   

print("\n-----------------------------------------------------------------------8-----")
#сравнение строк


s1 = "hello"
s2 = "world"
print("s1 == s2:", s1 == s2)  
# print("s1.startswith('h') and s2.endswith('d'):")  
print("s1 != s2:", s1 != s2)  


print("\n-----------------------------------------------------------------------9-----")
# булевы в numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3

# print("Четные числа:", arr[arr % 2 == 0])  
# print("Числа > 2 и < 5:", arr[(arr > 2) & (arr < 5)])  
print("Массив:", arr)
print("Маска (arr > 3):", mask)  
print("Применение маски:", arr[mask])  


print("\n----------------------------------------------------------------------10-----")
# pandas булева индексация

import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
df = pd.DataFrame(data)

print("Исходный DataFrame:")
print(df)

# фильтрация по условию
adults = df[df['age'] > 28]
# print("\nВозраст между 26 и 33:")
print("\nЛюди старше 28:")
# print("\nИмена начинающиеся на 'A' или возраст > 30:")
# print(df[(df['name'].str.startswith('A')) | (df['age'] > 30)])
# print(df[df['age'].between(26, 33)])
print(adults)

print("\n----------------------------------------------------------------------11-----")
# any() и all()

numbers = [0, 1, 2, 3, 4]

print("any(numbers):", any(numbers))  
# print("any(n > 2 for n in numbers):", any(n > 2 for n in numbers)) 
# print("all(n > 2 for n in numbers):", all(n > 2 for n in numbers)) 

print("\n----------------------------------------------------------------------12-----")
# булевы переменные как флаги
is_raining = True
has_umbrella = False

if is_raining and not has_umbrella:

# has_umbrella = True
# if is_raining and not has_umbrella:
#     print("Нужно взять зонт!")
# else:
#     print("Можно идти без зонта")  
    print("Нужно взять зонт!")  
else:
    print("Можно идти без зонта")

print("\n----------------------------------------------------------------------13-----")
# оператор := (морж) в условиях
names = ["Alice", "Bob", "Charlie"]

# long_name = next((name for name in names if len(name) > 5), None)
# if long_name:
#     print("Первое длинное имя:", long_name)