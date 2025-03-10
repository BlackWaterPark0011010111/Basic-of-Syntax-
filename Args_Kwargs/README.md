\\\\
RU
\\\\

они  помогают писать гибкий и масштабируемый код. Они позволяют передавать в функции разное количество аргументов, 
если нужно складывать неограниченное количество,можно писать:


def q(a, b, c, d, e):
    return a + b + c + d + e
Но это неудобно: если нужно сложить шесть чисел, код уже не сработает.

Здесь  нужен *args. Он позволяет передавать любое количество значений в функцию без необходимости заранее знать их количество. и по стандарту принимает class tuple. Когда  ставим *args, это означает, что все переданные аргументы собираются в кортеж еоторый не подлежит изменениям.


Аналогично, **kwargs нужен, когда мы не знаем, какие именно именованные аргументы (передаваемые в формате ключ=значение) попадут в функцию dictionary ВСЕГДА

**kwargs это аналог *args, но для именованных аргументов (то есть переданных в формате ключ=значение).

✅ перед функцией ставим **kwargs, это означает, что все переданные именованные аргументы собираются в словарь.
полезно когда количество передаваемых аргументов заранее неизвестно.
Когда функция должна обрабатывать любое количество входных данных.



def show(**kwargs):
    print(kwargs)

show(name="Алиса", age=25, city="Berlin")
#  {'name': 'Алиса', 'age': 25, 'city': 'Berlin'}
Все переданные именованные параметры попали в словарь, и мы можем к ним обращаться распаковывать

 полезно Когда количество и названия аргументов заранее неизвестны.Когда нужно передавать параметры в виде "ключ=значение".Когда функция должна работать с разными наборами данных.

\\\\
EN
\\\\

 They help write flexible and scalable code. They allow passing a different number of arguments into functions.

If you need to add an unlimited number of things, you could write something like this:

```
def q(a, b, c, d, e):
    return a + b + c + d + e
```


But that's kinda inconvenient: if you need to add six numbers, the code just won’t work.

This is where *args comes in. It lets you pass any number of values into a function without needing to know how many beforehand. By default, it accepts a class tuple. When we put *args, it means all the arguments passed are collected into a tuple, which can’t be changed.

Similarly, **kwargs is needed when we don’t know exactly what named arguments (passed in key=value format) will get into the function. It’s always a dictionary.

**kwargs is like *args but for named arguments (that is, passed in key=value format).

 When we put **kwargs before a function, it means that all the passed named arguments are collected into a dictionary. It’s useful when the number of arguments isn’t known beforehand. When the function needs to handle any number of input data.

```
def show(**kwargs):
    print(kwargs)
show(name="Alice", age=25, city="Berlin")
#  {'name': 'Alice', 'age': 25, 'city': 'Berlin'}
```
All the passed named parameters went into the dictionary, and we can access them or unpack them.

It’s useful when the number and names of arguments are unknown in advance. When you need to pass parameters as "key=value". When the function should work with different sets of data.