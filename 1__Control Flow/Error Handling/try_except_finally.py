try:
    x = 10 / 2
except ZeroDivisionError:
    print("Деление на ноль")

#x = 10 / 2 if 2 != 0 else print("Деление на ноль")

try:
    with open("data.txt", "r") as f:
        text = f.read()
except FileNotFoundError:
    print("Файл не найден")
except IOError:
    print("Ошибка чтения")

#text = open("data.txt").read() if os.path.exists("data.txt") else print("Нет файла")

try:
    num = int("123")
except ValueError:
    print("Не число")
else:
    print("Число:", num)

#if "123".isdigit(): num = int("123"); print("Число:", num)
#else: print("Не число")

conn = None
try:
    conn = connect_to_db()
    data = conn.get_data()
except ConnectionError:
    print("Нет соединения")
finally:
    if conn: conn.close()

#with connect_to_db() as conn: data = conn.get_data()

class MyError(Exception): pass

try:
    raise MyError("Ошибка!")
except MyError:
    print("Поймал свою ошибку")

#raise Exception("Просто ошибка")

try:
    try:
        [][1]
    except IndexError:
        print("Индекс за границами")
except Exception:
    print("Общая ошибка")

#if len([]) > 1: [][1]
#else: print("Индекс за границами")

try:
    import missing_lib
except ImportError:
    pass

#import missing_lib 

try:
    "строка" + 42
except TypeError:
    print("Несовместимые типы")
    raise

#try: "строка" + 42
#except TypeError as e: raise e

try:
    {}["ключ"]
except LookupError:
    print("Ключ не найден")

#try: {}["ключ"]
#except KeyError: print("Нет ключа")

def test():
    try:
        return 42
    finally:
        print("Finally выполняется")

test()

#def test(): return 42  

try:
    a = input("Введите число: ")
    res = 10 / int(a)
except ValueError:
    print("Это не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    print(f"Результат: {res}")

#res = 10 / int(a) if a.isdigit() and int(a) != 0 else print("Ошибка")

try:
    with open("data.json", "r") as f:
        data = json.load(f)
except FileNotFoundError:
    print("Файл не найден, создаем новый")
    data = {}
except json.JSONDecodeError:
    print("Ошибка формата файла")
    data = {}

#if os.path.exists("data.json"):
#    try: data = json.load(open("data.json"))
#    except: data = {}

try:
    response = requests.get("https://api.example.com/data", timeout=5)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.Timeout:
    print("Сервер не отвечает")
except requests.exceptions.HTTPError as err:
    print(f"Ошибка HTTP: {err.response.status_code}")
except Exception as e:
    print(f"Неизвестная ошибка: {e}")

#data = requests.get(url).json() if requests.get(url).status_code == 200 else None

try:
    conn = psycopg2.connect(dbname="test", user="postgres")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
except psycopg2.OperationalError:
    print("Ошибка подключения к БД")
except psycopg2.DatabaseError as e:
    print(f"Ошибка в запросе: {e}")
finally:
    if 'conn' in locals():
        conn.close()

#with psycopg2.connect(dbname="test") as conn:
#    rows = conn.cursor().execute("SELECT * FROM users").fetchall()

async def fetch_data():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                return await resp.json()
    except aiohttp.ClientError as e:
        print(f"Ошибка сети: {e}")
    except asyncio.TimeoutError:
        print("Таймаут соединения")

#data = await session.get(url).json() if await session.get(url).status == 200 else None

try:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(some_function)
        result = future.result(timeout=10)
except concurrent.futures.TimeoutError:
    print("Функция выполняется слишком долго")
except Exception as e:
    print(f"Ошибка в потоке: {e}")

#result = executor.submit(some_function).result() if not None else None

try:
    big_array = [0] * (10**8)
except MemoryError:
    print("Недостаточно памяти")
else:
    process_data(big_array)
finally:
    if 'big_array' in locals():
        del big_array

#big_array = [0] * (10**8) if sys.maxsize > 10**8 else None

try:
    res = math.sqrt(-1)
except ValueError:
    print("Недопустимое значение для sqrt")
    
try:
    res = math.exp(1000)
except OverflowError:
    print("Результат слишком велик")

#res = math.sqrt(x) if x >= 0 else None

try:
    dt = datetime.strptime("2023-13-01", "%Y-%m-%d")
except ValueError as e:
    print(f"Некорректная дата: {e}")

#dt = datetime.fromisoformat(date_str) if validate_date(date_str) else None

try:
    match = re.search(r"(\d+)", "abc123")
    num = int(match.group(1))
except AttributeError:
    print("Цифры не найдены")
except ValueError:
    print("Ошибка преобразования числа")

#num = int(re.findall(r"\d+", text)[0]) if re.search(r"\d", text) else None

try:
    arr = np.array([1, 2, 'a'])
    res = arr.astype(float)
except ValueError:
    print("Невозможно преобразовать массив")

#res = np.array(lst, dtype=float) if all(isinstance(x, (int, float)) for x in lst) else None

try:
    df = pd.read_csv("data.csv")
    avg = df["column"].mean()
except FileNotFoundError:
    print("Файл не найден")
except KeyError:
    print("Столбец не существует")
except pd.errors.EmptyDataError:
    print("Файл пуст")

#avg = pd.read_csv("data.csv")["column"].mean() if os.path.exists("data.csv") else None

try:
    img = Image.open("photo.jpg")
    img.verify()
except PIL.UnidentifiedImageError:
    print("Невозможно открыть изображение")
except Exception as e:
    print(f"Ошибка изображения: {e}")

#img = Image.open(path) if path.endswith(('.jpg','.png')) else None

while True:
    try:
        age = int(input("Ваш возраст: "))
        if not (0 < age < 120):
            raise ValueError
        break
    except ValueError:
        print("Введите корректный возраст!")

#age = int(input()) if input().isdigit() and 0 < int(input()) < 120 else None

try:
    with open("log.txt", "a") as f:
        f.write("Запись\n")
except IOError as e:
    print(f"Ошибка записи: {e.errno}")

#if os.access("log.txt", os.W_OK): open("log.txt", "a").write("Запись\n")

try:
    sock = socket.socket()
    sock.connect(("example.com", 80))
    sock.sendall(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    data = sock.recv(1024)
except socket.error as e:
    print(f"Сетевая ошибка: {e}")
finally:
    if 'sock' in locals():
        sock.close()

#with socket.create_connection(("example.com", 80)) as sock:
#    data = sock.recv(1024)

try:
    subprocess.run(["ls", "-l"], check=True, timeout=10)
except subprocess.TimeoutExpired:
    print("Команда выполнялась слишком долго")
except subprocess.CalledProcessError:
    print("Команда завершилась с ошибкой")

#output = subprocess.getoutput("ls -l") if os.name == 'posix' else None

try:
    with zipfile.ZipFile("archive.zip") as z:
        z.extractall()
except zipfile.BadZipFile:
    print("Некорректный zip-файл")
except zipfile.LargeZipFile:
    print("Слишком большой архив")

#if zipfile.is_zipfile("archive.zip"): zipfile.ZipFile("archive.zip").extractall()

try:
    with io.StringIO() as buffer:
        buffer.write("Тест")
        content = buffer.getvalue()
except io.UnsupportedOperation:
    print("Операция не поддерживается")
except Exception as e:
    print(f"Ошибка ввода-вывода: {e}")

#content = io.StringIO("Тест").getvalue() if hasattr(buffer, 'getvalue') else None