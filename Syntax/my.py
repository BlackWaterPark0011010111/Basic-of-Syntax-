print("Hello, world!")
print("---------------------------------------------------------------1------")

#name = input("Enter your name: ")
#print("Hello, " + name + "!")
#print("--------------------------------------------------------------2-------")
a = 5
b = 3
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)
print("-------------------------------------------------------------3--------")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
print("-------------------------------------------------------------4--------")
for i in range(1, 6):
    print("Number:", i)
print("--------------------------------------------------------------5-------")

count = 1
while count <= 5:
    print("Count:", count)
    count += 1
print("-------------------------------------------------------------6--------")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print("-------------------------------------------------------------7--------")

person = {"name": "Alice", "age": 25}
print(person["name"], "is", person["age"], "years old.")
print("--------------------------------------------------------------8-------")

def greet(name):
    print("Hello, " + name + "!")
greet("Bob")
print("--------------------------------------------------------------9-------")

def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum:", add(num1, num2))
print("------------------------------------------------------------10---------")

import random

num = random.randint(1, 10)
print("Random number:", num)
print("--------------------------------------------------------------11-------")

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
print("------------------------------------------------------------12---------")

text = input("Enter text: ")
print("Reversed:", text[::-1])

print("------------------------------------------------------------13---------")


with open("test.txt", "w") as file:
    file.write("Hello, file!")

with open("test.txt", "r") as file:
    content = file.read()
    print("File content:", content)
print("------------------------------------------------------------14---------")

with open("test.txt", "w") as file:
    file.write("Hello, file!")

with open("test.txt", "r") as file:
    content = file.read()
    print("File content:", content)
   
print("------------------------------------------------------------15---------")


word = input("Enter a word: ")
if word == word[::-1]:
    print("It's a palindrome!")#level, radar, madam, noon,121, 1331, 12321, "A Santa at NASA","Was it a car or a cat I saw"
else:
    print("Not a palindrome.")


print("------------------------------------------------------------16---------")

def factorial(n):
    result = 1

    for i in range(1, n + 1):
        result *= i

    return result

num = int(input("Enter a number: "))

print("Factorial:", factorial(num))


print("------------------------------------------------------------17---------")


text = input("Enter a string: ")

vowels = "aeiouAEIOU"

count = sum(1 for char in text if char in vowels)

print("Number of vowels:", count)

print("------------------------------------------------------------18---------")


a = 5

b = 10
print("Before swap:", a, b)

a, b = b, a 
print("After swap:", a, b)