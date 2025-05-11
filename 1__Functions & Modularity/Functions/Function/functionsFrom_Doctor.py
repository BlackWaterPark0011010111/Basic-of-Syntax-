#assiging function declaration (header) to a variable
def simpleFunc():
    return "I am a simple function"

retVal = simpleFunc

print(retVal)
print(type(retVal))

print(retVal())
print(simpleFunc())


#passing a function to a function
def wrapper(func):
    print(func)
    x = func() #To execute a function that is passed store it in variable
    return x * 10

outcome = wrapper(simpleFunc)
print(outcome)

#Nested functions
def outer_function():
    x = 10
    def inner_function():
        print("I am an inner function")
    inner_function()
    print(x)

outer_function()


#returning a function from a function
def outer_function():

    def inner_function():
        return "I am an inner function"
    
    return inner_function

receivedFunction = outer_function()
print(receivedFunction)
print(receivedFunction())

#closure
def outer_function(x):

    def inner_function():
        return "I am an inner function " + str(x)
    
    return inner_function

receivedFunction = outer_function(1234)
print(receivedFunction)
print(receivedFunction())


#decorator - design patterns
# 1. nested functions
# 2. return an inner function from the outer function
# 3. pass a function to an outer function
# 4. execute a passed function within the inner function
# 5. provide some useful functionality before or after executing a passed function
# This useful functionality is known as a decoration
def helloDec():
    return "Hello Decorators!"

def outer_function(func):

    def inner_function():
        print("The execution of the function helloDoc started at 12:01...")
        message = func()
        print(message)
        print("The execution of the function helloDoc finished successfuly at 12:02...")
        return "I am an inner function"
    
    return inner_function

receivedFunction = outer_function(helloDec)
print(receivedFunction)
print(receivedFunction())
