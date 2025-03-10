import json
import os

FILE_PATH = "passwords.json"

# Загрузка паролей из файла
def load_passwords():
    if not os.path.exists(FILE_PATH):
        return {}
    with open(FILE_PATH, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

# Сохранение паролей в файл
def save_passwords(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)