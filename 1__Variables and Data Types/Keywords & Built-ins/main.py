import math
import keyword

print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
 'try', 'while', 'with', 'yield']


global_value = 10

def outer():
    nonlocal_var = "внешняя"
    
    def inner():
        nonlocal nonlocal_var  
        nonlocal_var = "изменено из inner"
        print("nonlocal_var =", nonlocal_var)
    inner()
    return nonlocal_var

class Sandwich:
    def __init__(self, filling):
        self.filling = filling
    def eat(self):
        try:
            assert self.filling != "", "Без начинки?!"
            print(f"Бутерброд с {self.filling}")
        except AssertionError as e:
            print("Ошибка:", e)
        finally:
            print("Приятного аппетита!\n")
def check_numbers(nums):
    for n in nums:
        if n % 2 == 0 and n != 0:
            print(n, "— чётное число")
        elif n == 0:
            continue
        else:
            print(n, "— нечётное число")
    else:
        print("Проверка завершена!\n")

def generator(n):
    for i in range(n):
        yield i ** 2  
async def async_func():
    import asyncio
    await asyncio.sleep(0.1)
    print("Асинхронный вызов выполнен!\n")


if __name__ == "__main__":
    global_value = 10  
def change_value():

    global global_value  
    global_value = 20
    change_value()

    print(global_value)

    result = outer()

    print("Результат outer():", result, "\n")
    s1 = Sandwich("колбасой")
    s2 = Sandwich("")
    s1.eat()
    s2.eat()
    nums = [1, 2, 3, 4, 0]
    check_numbers(nums)

    print("Генератор квадратов:")
    for value in generator(5):
        print(value, end=" ")
    print("\n")

    import asyncio
    asyncio.run(async_func())

    # пример lambda
    square = lambda x: x * x
    print("Квадрат 7 через lambda:", square(7), "\n")

    # пример is / in
    text = "бутерброд"
    if "б" in text and text is not None:
        print("Слово содержит букву 'б'!\n")

    # пример del
    del text

    # пример pass
    def future_function():
        pass

    print("Конец программы!")
  