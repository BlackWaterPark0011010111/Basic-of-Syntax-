import random

def guess_number_game():
    secret = random.randint(1, 10)
    attempts = 3
    
    print("Угадай число от 1 до 10. У тебя 3 попытки!")
    
    for attempt in range(1, attempts+1):
        guess = int(input(f"Попытка {attempt}: "))
        if guess == secret:
            print("Ты угадал! Молодец!")
            break
        print("Неверно!")
    else:
        print(f"Ты проиграл! Число было: {secret}")

# Тест
guess_number_game()


import requests

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Ошибка запроса: {err}")
    else:
        print("Данные успешно получены!")
        return response.json()
    finally:
        print("Запрос завершен")

# Тест
data = fetch_data("https://api.example.com/data")
if data:
    print(f"Получено {len(data)} записей")