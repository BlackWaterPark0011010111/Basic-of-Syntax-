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
