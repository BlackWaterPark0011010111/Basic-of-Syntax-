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

try:
    