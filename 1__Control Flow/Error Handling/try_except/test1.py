import json,requests,sqlite3
import time
from threading import Thread
import asyncio
import logging
try:

    f= open("data.txt", "r")
    content = f.read()
    f.close()
except:
    print("файл не открылся...")
    try:
        f=open("data.txt", "w")
        f.write("Дефолтные данные")
        f.close()
    except:
        print("Беда с файлом")


print("=======================================json===")

data='{"name": "Вася", "age": 30}'
try:
    parsed=json.loads(data)
    print(parsed['name'])
except json.JSONDecodeError:
    print("Json is litl wrong")
except KeyError:
    print("where is the name?")

print("=======================================requests===")
try:
    response=requests.get('https://api.example.com/data')
    data=response.json()#тут тоже может будет ошибка
except requests.ConnectionError:
    print("internet drop down")
except:
    print("request didn`t workd")

print("=======================================sqlite===")
conn= None
try:
    conn=sqlite3.connect('test.db')
    cursor =conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
except sqlite3.OperationalError:
    print("Theres no table  Do u wanna create one?")
except:
    print("brrrrrrrr freezing   Чёт база глючит")
finally:
    if conn:#закрываем соединение если оно открылось
        conn.close()

print("=======================================threading,time===")
def worker():
    try:
        time.sleep(1)
        print("working")
    except:
        print("error in tred")

try:
    t=Thread(target=worker)
    t.start()
    t.join()#ждемс завершения
except:
    print("потоки не запустились")
#c асинхронностью продолжить
print("=========================asyncio============")
async def test():
    try:
        print("Starting")
        await asyncio.sleep(1)
        1/0#специально ломаем
    except:
        print("Асинхронная ошибка")
try:
    asyncio.run(test())
except:
    print("whole code is drop down")

print("=========================logging============")

logging.basicConfig(filename='errors.log')
#def risky_operation():#функция, которая может сломаться
#    num = random.randint(0, 2)
#    if num== 0:
#        1/0  
#    elif num== 1:
#        int("abc")  
#    else:
#        raise RuntimeError("случайная ошибка")



try:
   pass # risk_operation()
except Exception as e:#ZeroDivisionError:
#    print("no zero division!")
#except ValueError:
#    print("this is not a number")
#except Exception as e:  
#    print(f"unknown error: {e}")
    logging.error(f"error: {e}")
    print("check errors.log")
    

class User:
    def __init__(self, name,age):
        if not isinstance(name,str):
            raise ValueError("Name shold be a string")
        if age < 0:
            raise ValueError("age cannot be negative")
        self.name = name
        self.age=age
try:
    user=User(123, -6)
except ValueError as e:
    print(f"wrong data: {e}")
