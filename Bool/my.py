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
