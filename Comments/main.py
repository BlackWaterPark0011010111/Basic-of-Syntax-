# RUS



#  Однострочные комментарии



# docstring comments
"""
с двойными кавычками  with double quotes
"""

'''
как  с одинарными кавычками as with single quotes
'''


# 3. комментарии внутри функций или класса
def greet(name):
    """
    Эта функция принимает имя и возвращает приветствие.
    Многострочные строки внутри функций и классов служат документацией.
    This function takes a name and returns a greeting.
    Multi-line strings inside functions and classes serve as documentation.
    """
    return f"Hello, {name}!"

print(greet("May"))  # Вызов функции  Calling a function

# 4.  TODO  коммент
# TODO: Добавить проверку на пустую строку в функции greet  
# TODO: Add check for empty string in greet function



