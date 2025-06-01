"""Coding a calculator
Context
In this exercise, your are given code for a program that is a basic calculator. User input is assumed to be a mathematical formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Here is the basic code for the calculator:

# create a new exception class called "MathematicalError" from BaseException class
class MathematicalError(Exception):pass

# write a function called parse_input that parses all the user input according to rules list defined in the exercise text
def parse_input(user_input):


# function calculate takes 2 integers and an operation type as an argument
def calculate(n1, op, n2):

  if op == '+':
    return n1 + n2
  if op == '-':
    return n1 - n2
  if op == '*':
    return n1 * n2
  if op == '/':
    return n1 / n2

while True:
  user_input = input('>>> ')
  if user_input == 'quit':
    break
  result = calculate(n1, op, n2)
  print(result)
An interaction could look like this (easiest if you run this on Idle):

>>> 1 + 1
2.0
>>> 3.2 - 1.5
1.7000000000000002
>>> quit
Task
Your task is to right a function called parse_input,that splits user input using str.split(), and checks (using exceptions) whether the following list of things are valid (using try and except):

If the input does not consist of 3 elements, raise a MathematicalError, which is a custom Exception. (Hint: create a custom exception class)
Try to convert the first and third input to a float type(like so: float_value = float(str_value)). Catch any ValueError(built-in exception) that occurs, and instead raise a MathematicalError (custom exception).
If the second input is not '+' or '-' (or any other operator that you use), again raise a MathematicalError.
If the input is valid, perform the calculation and print out the result (as in the code above). The user is then prompted to provide new input, and so on, until the user types "quit".

unittest
In order to test your solution:

Name your solution file as solution_calc.py .Run the test_calc.py
Copy test_calc.py file (provided in this repo) to the same folder
Run the test_calc.py script."""

import os
class MathematicalError(Exception):
    pass

def parse_input(user_input):
    parts = user_input.split()  
    if len(parts) != 3:
        raise MathematicalError("Input must contain exactly three parts: number, operator, number")
    
    try:
        n1 = float(parts[0])  
        n2 = float(parts[2])  
    except ValueError:
        raise MathematicalError("First and third inputs must be numbers")
    
    op = parts[1]  
    if op not in ('+', '-', '*', '/'):
        raise MathematicalError("Operator must be one of: +, -, *, /")
    
    return n1, op, n2  


def calculate(n1, op, n2):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1 * n2
    if op == '/':
        if n2 == 0:
            raise MathematicalError("Division by zero is not allowed")
        return n1 / n2


while True:
    user_input = input('>>> ') 
    if user_input.lower() == 'quit':
        break  
    
    try:
        n1, op, n2 = parse_input(user_input)  
        result = calculate(n1, op, n2)  
        print(result)
    except MathematicalError as e:
        print(f"Error: {e}")  


# basic division
try:
    print(10 / 0)
except:
    print("can't divide")

#if 0 != 0: print(10 / 0)
#else: print("can't divide")

# file handling
try:
    f = open("file.txt")
    print(f.read())
    f.close()
except:
    print("file error")

#if os.path.exists("file.txt"):
#    f = open("file.txt")
#    print(f.read())
#    f.close()
#else: print("no file")

# number conversion
try:
    num = int("not a number")
    print("success:", num)
except ValueError:
    print("not a number")

#if "not a number".isdigit(): 
#    num = int("not a number")
#    print("success:", num)
#else: print("not a number")

# list index
nums = [1,2,3]
try:
    print(nums[5])
except IndexError:
    print("bad index")

#if len(nums) > 5: print(nums[5])
#else: print("bad index")

# dict key
user = {"name": "john"}
try:
    print(user["age"])
except KeyError:
    print("no key")

#print(user.get("age", "no key"))

# multiple exceptions
try:
    num = int(input("number: "))
    print(10 / num)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("can't divide by zero")
except:
    print("some error")

# else/finally
try:
    num = int("42")
except ValueError:
    print("conversion error")
else:
    print("result:", num)
finally:
    print("always runs")

# custom exception
class MyError(Exception): pass

try:
    raise MyError("test")
except MyError as e:
    print("caught:", e)

# nested try
try:
    try:
        1 / 0
    except ZeroDivisionError:
        print("inner handler")
        raise
except:
    print("outer handler")

# function example
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("divide by zero")
        return None
    except TypeError:
        print("need numbers")
        return None

print(divide(10, 2))
print(divide(10, 0))
print(divide("10", "2"))

# file operations
try:
    with open("test.txt", "w") as f:
        f.write("test")
    with open("test.txt") as f:
        print(f.read())
except IOError:
    print("file error")
finally:
    if os.path.exists("test.txt"):
        os.remove("test.txt")

# input loop
while True:
    try:
        num = int(input("number (0 to quit): "))
        if num == 0: break
        print(100 / num)
    except ValueError:
        print("not a number")
    except ZeroDivisionError:
        print("can't divide by zero")
    except:
        print("unknown error")
        raise

# common exceptions
try:
    import missing_module
except ImportError:
    print("no module")

try:
    {}["key"]
except KeyError:
    print("no key")

try:
    "text" + 42
except TypeError:
    print("wrong types")

# validation
def check_age(age):
    if age < 0:
        raise ValueError("age can't be negative")
    return age >= 18

try:
    print(check_age(25))
    print(check_age(-5))
except ValueError as e:
    print("error:", e)

# file handle
f = None
try:
    f = open("test.txt", "w")
    f.write("test")
except IOError:
    print("write error")
finally:
    if f: f.close()
    print("file closed")

# alternative approaches
if os.path.exists("file.txt"):
    with open("file.txt") as f:
        print(f.read())
else:
    print("no file")

try:
    with open("file.txt") as f:
        print(f.read())
except IOError:
    print("file error")

# input validation
def get_positive():
    while True:
        try:
            num = float(input("positive number: "))
            if num <= 0:
                raise ValueError("must be positive")
            return num
        except ValueError as e:
            print(f"error: {e}. try again")

print(get_positive())