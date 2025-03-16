"""Лямбда-функции

Они анонимны, но все же являются представителями первого
гражданами первого класса и могут быть присвоены переменной.Они имеют свой собственный синтаксис.
● В них используется лямбда вместо def.
● У них нет имени.
● Им не нужны круглые скобки.
● В них не используется ключевое слово return.
● Они не могут использовать несколько строк.
Лямбда-функции - это специальные анонимные функции, определяемые как выражения"""

"""Lambda functions.
They are anonymous, but are still representatives of the first citizens of the first class and can be assigned 
to a variable.They have their own syntax.
● They use lambda instead of def.
● They do not have a name.
● They don't need parentheses.
● They don't use the return keyword.
● They cannot use multiple strings.
Lambda functions are special. 
anonymous functions defined asexpressionsTranslated with DeepL.com (free version)"""
add1 = lambda x: x + 1(add1(1))
2
# This is equivalent
 # Это эквивалентно
def add1(x):
    return x + 1
 
    print(add1(1))





add1 = lambda x: x + 1
"""input parameters. Input parameters can be any number or 0.
Output parameter.
"""
"""входные параметры. В качестве входных параметров может 
быть любое число или 0.
Выходной параметр.
"""




"""They can take any number of arguments.
They can take any number of arguments.
They help make code more 
succinct.
Defining a lambda function and assigning it 
immediately to a variable name is not recommended 
is not recommended by the PEP-8 style guide.
Lambda functions"""
"""Они могут принимать любое количество аргументов.
Они могут принимать любое количество аргументов.
Они помогают сделать код более 
лаконичным.
Определение лямбда-функции и присвоение ее 
сразу же присвоить ее имени переменной не рекомендуется 
не рекомендуется руководством по стилю PEP-8.
Лямбда-функции"""
multiply = lambda x, y: x * y
print(multiply(1, 0))
0
print(multiply(3, 9))
27
def printer(bar):
    return lambda x: f"{bar}, {x}!"

greet = printer("Hello")
print(greet("John"))



"""
Often used in closures and decorators, or as arguments to pass to higher-order functions.
Lambda functions
They help make code more concise and prevent the creation of a variable name that is not needed.
"""
"""
Часто используется в закрытиях и декораторах или 
в качестве аргументов для передачи в функции более высокого порядка 
функциям более высокого порядка.
Лямбда-функции
Они помогают сделать код более 
лаконичность и предотвращают создание 
имени переменной, которое не требуется.
"""
def make_uppercase(func):
    return lambda x: func().upper()

@make_uppercase
def greeting():

    return "Hello World!"
print( greeting() )




"""That we can call functions both from within another function, and 
as well as from within the same function.● That recursive functions must define a base case to 
recursion termination.
● That they work in two stages: deepening and backward computation computation.
● That functions can be nested and contained within other functions. functions.
● That functions are first class citizens and can be assigned to to variables and pass them as arguments.
● That closures are functions that return a function, and that function has access to the first scope of the function.
● That decorators are closures that take a function as an argument to a function 
argument.
● How to work with function arguments and decorators.
● How to create anonymous functions using lambda functions functions""" 



"""Что мы можем вызывать функции как изнутри другой функции, так и 
так и из той же функции.
● Что рекурсивные функции должны определять базовый случай, чтобы прекращения рекурсии.
● Что они работают в два этапа: углубление и обратное вычисление вычисления.
● Что функции могут быть вложенными и содержаться внутри других функций.функции.
● Что функции являются гражданами первого класса и могут присваиваться переменным и передавать их в качестве аргументов.
● Что закрытия - это функции, которые возвращают функцию, и эта функция имеет доступ к первой области видимости функции.● Что декораторы - это закрывающие функции, принимающие в качестве аргумента функцию 
аргумент.
● Как работать с аргументами функций и декораторов.
● Как создавать анонимные функции с помощью лямбда-функций 
функции"""
























