# по базовому исключению
class MyEx(Exception): pass
raise MyEx("чё-то не так")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("на ноль делить низя")



try:
    "строка" + 123
except TypeError:
    print("типы не совпадают")# на типы

d = {"name": "вася"}
try:
    print(d["age"])
except KeyError:
    print("нет такого ключа")

try:
    int("abc")#число блядь нужно,уже проверка
except ValueError:
    print("это не число")

try:
    import blablaaaaaafuck
except ImportError:
    print("модуль не найден")

try:
    open("файл.txt")
except FileNotFoundError:
    print("файл потерялся")

try:
    open("/etc/shadow")  #в моем линуксе
except PermissionError:
    print("нет доступа")

try:
    while True: pass
except KeyboardInterrupt:
    print("выходим...")

class Test:
    def method(self):
        raise NotImplementedError("потом доделаю")

try:
    "строка".qwerty()
except AttributeError:
    print("нет такого метода")

#if True print("ой")  
#def test():
#print("плохо")  # так нельзя

try:
    pass
except (TypeError, ValueError):#ловить несколько ошибок сразу

    print("или тип не тот, или значение")

try:
    pass
except Exception as e:
    print(f"случилось {e}")

try:
    f = open("file.txt")
except:
    print("ошибка")
finally:#finally выполнится всегда

    print("убираем за собой")
    # f.close()  

try:#else если не было ошибок

    print("всё ок")
except:
    print("ошибка")
else:
    print("значит ошибок не было")