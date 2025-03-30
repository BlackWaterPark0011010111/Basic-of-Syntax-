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

# bool([]) 
# bool([False]) 
# bool(-1)
