
import os
import random
import json
import time
from functools import wraps
from pathlib import Path


def save_to_file(filename, *data_lines, **file_options):
  
    #with open(filename, 'w') as f:
    #    for line in data_lines:
    #        f.write(line + '\n')
    if Path(filename).exists() and not file_options.get('overwrite', False):
        raise FileExistsError(f"Файл {filename} уже существует! Используйте overwrite=True.")

    encoding = file_options.get('encoding', 'utf-8')

    mode = 'a' if file_options.get('append') else 'w'
    
    with open(filename, mode, encoding=encoding) as f:
        for line in data_lines:
            #f.write(line)
            f.write(line + '\n')

    print(f"Данные сохранены в {filename}!")

def retry_on_error(max_retries=3, delay=1):
   
    
    def decorator(func):
        @wraps(func)  #сохранить имя исходной функции
        def wrapper(*args, **kwargs):
            retries = 0
            last_error = None
            
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_error = e
                    retries += 1
                    print(f"Ошибка: {e}. Попытка {retries}/{max_retries}...")
                    time.sleep(delay)
            
            raise last_error if last_error else Exception("Неизвестная ошибка")
        
        return wrapper
    return decorator

#@retry_on_error(max_retries=5)
@retry_on_error(max_retries=3, delay=2)
def fetch_data(url, **params):

    if random.random() < 0.6:
        raise ConnectionError("Сервер не отвечает :(")
    return f"Данные с {url}: {params}"




class DataProcessor:
   
    def __init__(self, default_format='json'):
        self.default_format = default_format
        self.settings = {'verbose': False}

    def update_settings(self, **new_settings):
        valid_keys = {'verbose', 'output_dir', 'debug_mode'}
        for key in new_settings:
            if key not in valid_keys:
                print(f"Предупреждение: неизвестная настройка {key}!")
        self.settings.update(new_settings)

    def process(self, *data_sources, **options):
      
        results = []
        format_type = options.get('format', self.default_format)

        #for source in data_sources:
        #    results.append(f"Обработано: {source}")

        for source in data_sources:
            if not self._validate_source(source):
                print(f"Пропускаем невалидный источник: {source}")
                continue

            processed = f"{source.upper()} -> в формате {format_type}"
            if self.settings.get('verbose'):
                processed += f" (детали: {options})"
            results.append(processed)

        return results

    def _validate_source(self, source):
        return bool(source)  
    #пустые строки пропускаем


def calculate_safe(*numbers): #обраю ошибок
   
    if not numbers:
        print("Ошибка: нет чисел для расчёта!")
        return None

    try:
#cначала было просто sum(numbers)/len(numbers), но...
#oказалось,это может сломаться на пустом списке
        return round(sum(numbers) / len(numbers), 2)
    except TypeError as e:
        print(f"Ошибка: не все аргументы — числа! ({e})")
        return None
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        return None

if __name__ == "__main__":
    try:
        save_to_file("test.txt", "Строка 1", "Строка 2", overwrite=True)
        #без overwrite ловит ошибку (так и задумано)
    except Exception as e:
        print(f"ooopssss: {e}")

    try:
        data = fetch_data("https://google.com", params={"id": 42})
        print(data)
    except Exception as e:
        print(f"Не удалось загрузить данные: {e}")


    processor = DataProcessor()
    processor.update_settings(verbose=True, debug_mode=False)
    results = processor.process("FILE1", "FILE2", "", format="csv")
    print("Результаты обработки:", results)
    print("Среднее:", calculate_safe(1, 2, 3, "oops", 5))  #ошибка типа
    print("Среднее (нормальные данные):", calculate_safe(10, 20, 30))