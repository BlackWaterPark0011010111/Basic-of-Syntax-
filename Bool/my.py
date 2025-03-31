print("\n-----------------------------------------------------------------------1-----")
# Boolean operations - the basics
x = True
y = False

# Basic operations
print("x and y:", x and y)  # False
print("x or y:", x or y)    # True
print("not x:", not x)      # False

# print("x xor y:", x ^ y)  
# print("y == (not x):", y == (not x))  

print("\n-----------------------------------------------------------------------2-----")
# Comparisons and boolean values
a = 5
b = 10

print("a < b:", a < b)  
print("a == b:", a == b)
print("a != b:", a != b)

# print("(a < b) and (a != b):", (a < b) and (a != b))  
# print("(a > b) or (a == 5):", (a > b) or (a == 5))    

print("\n-----------------------------------------------------------------------3-----")
# Type conversion to bool
values = [0, 1, "", "hello", None, [], [1,2,3]]

print("Checking truthiness of values:")
for v in values:
    # print(f"{str(v):<6} ->", bool(v))
    if v:
        print(f"{str(v):<6} -> True")  # with formatting
    else:
        print(f"{str(v):<6} -> False")


print("\n-----------------------------------------------------------------------4-----")
# Working with None
var1 = None
var2 = 42

print("var1 is None:", var1 is None)   
print("var2 is not None:", var2 is not None)  

# if var1:
#     print("var1 has a value")  # won't execute
# else:
#     print("var1 is empty")  # will execute

print("\n-----------------------------------------------------------------------5-----")
# Boolean expressions with 'in'
fruits = ["apple", "banana", "orange"]

print("'apple' in fruits:", "apple" in fruits)  
print("'pear' not in fruits:", "pear" not in fruits)  

# print("'apple' in fruits and len(fruits) > 2:", "apple" in fruits and len(fruits) > 2) 

print("\n-----------------------------------------------------------------------6-----")
# Short-circuit evaluation
def check(x):
    print("check executed for", x)
    return x

# print(check(False) and check(True))  
# print(check(True) or check(False))   

print("\n-----------------------------------------------------------------------7-----")
# Boolean operations with numbers
n1 = 0
n2 = 7

# Numbers in boolean context
print("bool(n1):", bool(n1))  
print("bool(n2):", bool(n2))  

# print("n1 and n2:", n1 and n2)  # 0 returns the last operand
# print("n1 or n2:", n1 or n2) 
# print("not n1:", not n1)   

print("\n-----------------------------------------------------------------------8-----")
# String comparisons
s1 = "hello"
s2 = "world"
print("s1 == s2:", s1 == s2)  
# print("s1.startswith('h') and s2.endswith('d'):")  
print("s1 != s2:", s1 != s2)
print("\n-----------------------------------------------------------------------9-----")
# Boolean operations in numpy

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 3

# print("Even numbers:", arr[arr % 2 == 0])  
# print("Numbers > 2 and < 5:", arr[(arr > 2) & (arr < 5)])  
print("Array:", arr)
print("Mask (arr > 3):", mask)  
print("Applying mask:", arr[mask])  


print("\n----------------------------------------------------------------------10-----")
# Boolean indexing in pandas
 
import pandas as pd

data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35]}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Filtering by condition
adults = df[df['age'] > 28]
# print("\nAge between 26 and 33:")
print("\nPeople older than 28:")
# print("\nNames starting with 'A' or age > 30:")
# print(df[(df['name'].str.startswith('A')) | (df['age'] > 30)])
# print(df[df['age'].between(26, 33)])
print(adults)

print("\n----------------------------------------------------------------------11-----")
# any() and all()

numbers = [0, 1, 2, 3, 4]

print("any(numbers):", any(numbers))  
# print("any(n > 2 for n in numbers):", any(n > 2 for n in numbers)) 
# print("all(n > 2 for n in numbers):", all(n > 2 for n in numbers)) 
