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