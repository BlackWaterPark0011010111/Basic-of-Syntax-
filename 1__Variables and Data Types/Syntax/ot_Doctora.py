"""
This is a multiline string
It is used by docstring
We will cover it later in depth
"""

print("Hello world!")
print()
print("Hello world for the second time")
print()
print("Hello", "world!!!")
print()
print("Hello", 'world', "!!!")
print("One of my favourite books is 'Python for programmers'")
print()
print('Actually, there are more books, including "Python for programmers by Deitel" ')
print()
print("Actually, there are more books, including 'Python for programmers by Deitel' ")
print("Hello", "world", "for", "the", "time", "being", sep="\n")

# This is my first comment
# It is a variable that is being used by the print statement

x = "This is my first variable using a simple print()."
print(x)
print(x)
print(x)

y = 53
print(type(y))
print("Y value is equeal to " + str(y))
print(type(y))

print("Let's try to convert in the opposite direction: string to a number")
z = "123"
z = int(z)
print(type(z))

f = 123.932342342
print(f)
print(type(f))
print(int(f))
print(float(y))

#Introduction of isinstance function
print("Intro to isinstance function")
print(type(f))
print(isinstance(f, float))

#Boolean data type
b = False
print(type(b))

#imaginary numbers
i = 5 + 5j
print(i)
print(type(i))

#swapping values in python
x = 10
y = 20
x, y = y, x
print(x, y, sep=" ")

#crazy number
x = 444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444445555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555566666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666666677777777777777777777777777777777777777777777777777777777777777777777777777777777
print(x)


#scientific notation
y = 9e15
print(type(y))

#using bool() casting on various data types
print(bool(0))
print(bool(" "))

#None data type
example = None
print(example)
print(type(example))

#math operations
print(234//11)
#modulus operator produces reminder
print(11%10)
#power operand
print(2**64)

#math functions
result = max(12, 333, 445, 2, 44)
print(result)
print(min(2, 33, 55, 1, 6666, result))
negative_day = -3455
print(abs(negative_day))
print(pow(2,10))
print(round(0.257, 2))

# using math module
import math
print(math.sqrt(81))
print(math.e)
print(math.pi)
print(math.ceil(3.1))
print(round(3.1))
print(math.floor(3.9))
print(round(math.pi, 2))

#assignment operators
c = 10
#c = c + 11
c += 11
print(c)

#binary representation
print("Binary numbers starting with 0b01...")
print(0b01)
print(0b10)
print(0b11)
print(0b111)
print(0b101)
print(0b011)
print(0b100)
print(0b1111)
print(0b11111)
print(0b11110) #30
print(0b11101) #29
print(0b11001) #25
print(0b10100) #20
print(0b11111111) #255
print(0b11001000) #200
print(0b01100100) #100
print(0b1111111111111111) #16 bit systems 65535
print(0b11111111111111111111111111111111) #32 bit systems store up to 
print(0b1111111111111111111111111111111111111111111111111111111111111111) 

#Hexadecimal number representation
print(0x10)
print(0x01)
print(0xFFFF) #16 bit systems 65535 in hexadecimal notation

#using bin function
print(bin(1000))
print(bin(10000000))

#using int function
print(int('FFFFFFFF', 16))
print(0b0000000000000000000000000000000000000000000000)

#using if statements
a = 15
b = 5

if b > a:
    print("B is greater than A")
elif a == b:
    print("Both values are equal")
else:
    print("So, obviously A is greater than B")


a = 15
b = 2

#Any reminder
if a % b == 0:
    print("There is no reminder")
else:
    print("There is a reminder")

a = "bool"
if a == True:
    print("A is a True value")
else:
    print("A is not a truephy value")


#for loop with a range function
for x in range(0, 10, 2):
    print(x)

list1 =  ["First", "Second", "Third", "Fourth", "Fifth"]
list2 = [1, 2, 3, 4, 5, 6, 7]
for x in list1:
    if x == "Fourth":
        continue
    print(x)
    for y in list2:
        print(y)
else:
    print("The loop has finished...")
        
#While loops
x = 10
while x > 0:
    print("Value of x in a while loop", x)
    # for y in range(10):
    #     print("This is my inner loop",y + x)
    x -= 1

for z in range(10, 0, -1):
    print("Value of z in a for loop", z)

#looping over dictionary
dict = {"one": 1, "two": 2, "three": 3}
for x in dict:
    print("key: ", x)
    print("value: ", dict[x])

mylist = ["Dog", "Cat", "Mouse", "Elephant"]
for animal in mylist: #for loop
    if animal == "Cat":
        print("My favourite animal is: ", animal)

mydict = {"name":"Jordan", "surname":"Stanley", "profession":"guitarist"}
for x in mydict:
    print(mydict[x])


#Logical and, or, not
x = 10
age = 17
if x == 10 or age == 18:
    print("Yes, good")
else:
    print("Sorry, not possible!")

#ternary if statement
print("Yes, good") if not(x == 10 or age == 18) else print("Sorry, not possible!")


#functions
def firstFunction():
    print("********************************************")
    print("This is my first function!")
    print("It does not do anything useful yet.")
    print("But it demonstrates how to avoid repetion of print function")
    print("*********************************************")

firstFunction()
firstFunction()

funcTest = firstFunction()
print(funcTest)
print(type(funcTest))

#function with a return keyword
def secondFunction(x, y):
    return x**y**2

x = 5
y = 32
result = secondFunction(x, y)
print(result)


#setting the scene for a function call
# arg1 = input("Please specify the value you want to take to the power of x....")
# arg2 = input("Please specify the value of x to which we will raise the first argument...")
# arg1 = float(arg1)
# arg2 = float(arg2)

# result = power(arg1, arg2)
# print(result)

firstFunction()
print(secondFunction(5, 6))
print(secondFunction(7, 9))

result = secondFunction(5, 6)
print(result)