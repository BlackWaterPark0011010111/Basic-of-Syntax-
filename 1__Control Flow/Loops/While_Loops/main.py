import requests
import time
import random
count = 0
while count < 5:
    print(f"Это строка №{count+1}")
    count += 1  

password = ""
while password != "12345":  
    password = input("пароль: ")
print("Добро пожаловать!")

while True:#ошибки в цикле
    try:
        num = int(input("Введите число: "))
        break
    except ValueError:
        print("Это не число! Попробуйте ещё раз")

choice = ""
while choice != "4":
    print("\n1.  время\n2. дата\n3. Шутка\n4. Выход")
    choice = input("Выберите пункт: ")
    if choice == "1":
        print("Сейчас  день")
    elif choice == "2":
        print("сегодня 2025 год")
    elif choice == "3":
        print("программист на рыбалке... while True: try_to_catch()")






file = open("test.txt", "w")# файлы
lines_written = 0
while lines_written < 10:
    file.write(f"строка {lines_written}\n")
    lines_written += 1
    print(f"записано строк: {lines_written}")
file.close()





#Угадай число
number = random.randint(1, 100)
guess = 0
attempts = 0
while guess != number:
    guess = int(input("Угадай число (1-100): "))
    attempts += 1
    if guess < number:
        print("Больше!")
    elif guess > number:
        print("Меньше!")
print(f"Победа! Попыток: {attempts}")




# Чтение с условием
total = 0
with open("data.txt") as f:
    while (line := f.readline()) and total < 1000:  #моржовый оператор
        total += int(line.strip())
        
        print(f"Текущая сумма: {total}")






timeout = 10  # секунд
start_time = time.time()
success = False
while not success and time.time() - start_time < timeout:
    print("пытаюсь подключиться ")
    time.sleep(1)
    if random.random() > 0.7:  # 30% успеха
        success = True
        print("подключено!")
else:
    if not success:
        print("время вышло!")

#API с пагинацией
page = 1
results = []


while True:
    response = requests.get(f"https://api.example.com/data?page={page}")
    
    data = response.json()
    if not data["results"]:
        break

    results.extend(data["results"])
    
    page += 1
    print(f"Загружено страниц: {page}")

#мини-интерпретатор
variables = {}
print("Мини-калькулятор (для выхода введите 'exit')")

while True:
    cmd = input(">>> ").strip()

    if cmd.lower() == "exit":
        break
    
    try:
        if "=" in cmd: 
            var, expr = cmd.split("=", 1)
            variables[var.strip()] = eval(expr.strip(), {}, variables)

        else:  #вычисление
            print(eval(cmd, {}, variables))
    except Exception as e:

        print(f"Ошибка: {e}")