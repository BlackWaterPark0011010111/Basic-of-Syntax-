import requests
import csv
import json
import sqlite3
import threading
from PIL import Image
import aiohttp
from datetime import datetime
import math
import numpy as np
import os
import sys
from io import StringIO
import concurrent.futures
import asyncio
import re
import zipfile
import socket
import subprocess
import yaml  #альтернатива обработки конфигов
import psycopg2  # для PostgreSQL
from pathlib import Path  
from contextlib import contextmanager


#API
response = None
try:
    response = requests.get('https://api.example.com/data', timeout=3)
    data = response.json()
except requests.exceptions.RequestException:
    print('api не отвечает')

if response and response.status_code == 200:
    print(data.get('results'))

#CSV
try:
    with open('data.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['name'])
except FileNotFoundError:
    print('нет такого файла')
except KeyError:
    print('в файле нет колонки name')

#парсинг JSON
json_data = '{"name": "John", "age": 30}'
try:
    data = json.loads(json_data)
    print(data['name'])
except json.JSONDecodeError:
    print('битый json')
except KeyError:
    print('нет поля name')

#с БД
conn = None
try:
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
except sqlite3.Error as e:
    print(f'ошибка базы: {e}')
finally:
    if conn:
        conn.close()

def worker():
    try:
        pass
    except Exception as e:
        print(f'ошибка в потоке: {e}')

thread = threading.Thread(target=worker)
thread.start()

try:
    img = Image.open('photo.jpg')
    img.rotate(45).save('rotated.jpg')
except PIL.UnidentifiedImageError:
    print('нечитаемый файл')
except OSError:
    print('проблема с файлом')

def validate_email(email):
    try:
        if '@' not in email:
            raise ValueError('не похоже на email')
        return True
    except ValueError as e:
        print(e)
        return False

validate_email('testexample.com')

async def fetch_data():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()
    except aiohttp.ClientError:
        print('сетевая ошибка')

try:
    date = datetime.strptime('2023-13-01', '%Y-%m-%d')
except ValueError:
    print('некорректная дата')

try:
    result = math.sqrt(-1)
except ValueError:
    print('нельзя извлечь корень')

try:
    arr = np.array([1, 2, 'a'])
    mean = arr.mean()
except TypeError:
    print('неправильные типы')