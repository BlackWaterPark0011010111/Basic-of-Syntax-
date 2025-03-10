# RUS



#  Однострочные комментарии



# docstring comments
"""
с двойными кавычками
"""

'''
как  с одинарными кавычками
'''


# 3. комментарии внутри функций или класса
def greet(name):
    """
    Эта функция принимает имя и возвращает приветствие.
    Многострочные строки внутри функций и классов служат документацией.
    """
    return f"Привет, {name}!"

print(greet("May"))  # Вызов функции

# 4.  TODO  коммент
# TODO: Добавить проверку на пустую строку в функции greet




# EN
# 1. Single-line comments


# 2. Docstring comments
"""
double quotes 
"""

'''
single quotes 
'''

# 3. Docstring inside functions
def greet(name):
    """
    This function takes a name and returns a greeting.
    Multi-line strings inside functions and classes serve as documentation.
    """
    return f"Hello, {name}!"

print(greet("May"))  # Function call

# 4. Using TODO
# TODO: Add a check for an empty string in the greet function

# 5. Commented-out code (will not execute)
# print("This code will not run because it is commented out")
