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
