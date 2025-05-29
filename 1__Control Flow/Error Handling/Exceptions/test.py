try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero man")
    #result = float('inf')

    #try:
    #    result = 10 / 0
    #except ZeroDivisionError:
    #    print("Oops")
    #else:
    #    print(result)
    #def safe_divide(a, b):
    #    try:
    #        return a / b
    #    except ZeroDivisionError:
    #        return None
    #result = safe_divide(10, 0)

try:
    with open("config.json") as f:
        settings = json.load(f)
except FileNotFoundError:
    print("Config file missing")
    #settings = {"default": True}
    #with open("config.json", "w") as f:
    #    json.dump(settings, f)
    #if os.path.exists("config.json"):
    #    with open("config.json") as f:
    #        settings = json.load(f)
    #else:
    #    settings = {}
    #config_path = Path("config.json")
    #if config_path.exists():
    #    settings = json.loads(config_path.read_text())
except json.JSONDecodeError:
    print("Invalid JSON format")
    #with open("config.json") as f:
    #    try:
    #        settings = json.loads(f.read().strip())
    #    except:
    #        settings = {}
    #try:
    #    import yaml
    #    with open("config.json") as f:
    #        settings = yaml.safe_load(f)
    #except:
    #    settings = {}

max_retries = 3
for attempt in range(max_retries):
    try:
        conn = psycopg2.connect(DB_URL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        break  # Success!
    except psycopg2.OperationalError as e:
        print(f"Attempt {attempt + 1} failed: {e}")
        if attempt == max_retries - 1:
            raise  # Re-raise on last attempt
        time.sleep(2 ** attempt)  # Exponential backoff
    finally:
        if 'conn' in locals():
            conn.close()

    #from psycopg2 import pool
    #conn_pool = pool.SimpleConnectionPool(1, 10, DB_URL)
    #conn = conn_pool.getconn()
    #try:
    #    cursor = conn.cursor()
    #    cursor.execute("SELECT * FROM users")
    #finally:
    #    conn_pool.putconn(conn)