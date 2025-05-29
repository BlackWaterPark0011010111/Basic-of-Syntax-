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
    
    #from sqlalchemy import create_engine
    #engine = create_engine(DB_URL)
    #with engine.connect() as conn:
    #    result = conn.execute("SELECT * FROM users")
    #@contextmanager
    #def db_connection():
    #    conn = psycopg2.connect(DB_URL)
    #    try:
    #        yield conn
    #    finally:
    #        conn.close()
    
    #with db_connection() as conn:
    #    cursor = conn.cursor()
    #    cursor.execute("SELECT * FROM users")

try:
    response = requests.get(
        "https://api.example.com/data",
        timeout=(3.05, 27),  # Connect + read timeout
        headers={"Authorization": f"Bearer {API_KEY}"}
    )
    response.raise_for_status()
    data = response.json()
except requests.exceptions.SSLError:
    print("SSL certificate problem")
    #response = requests.get(API_URL, verify=False)
    
    #response = requests.get(API_URL, verify="/path/to/cert.pem")
except requests.exceptions.Timeout:
    print("Request timed out")
    #for _ in range(3):
    #    try:
    #        response = requests.get(API_URL, timeout=5)
    #        break
    #    except requests.exceptions.Timeout:
    #        continue

    #import aiohttp
    #async with aiohttp.ClientSession() as session:
    #    async with session.get(API_URL) as resp:
    #        data = await resp.json()
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    #Alternative 1: Log full error details
    #import traceback
    #traceback.print_exc()

    #send_slack_alert(f"API failed: {str(e)}")

try:
    df = pd.read_csv("big_dataset.csv")
    processed = df.groupby("category").agg({
        "value": ["mean", "std"]
    })
except pd.errors.EmptyDataError:
    print("Empty CSV file")
    #df = pd.DataFrame(columns=["category", "value"])
    
    #processed = None
    #continue  # In a processing loop
except KeyError as e:
    print(f"Missing column: {e}")
    #required_cols = ["category", "value"]
    #if not all(col in df.columns for col in required_cols):
    #    df = df.reindex(columns=required_cols, fill_value=0)
    
    #df = df[["category", "value"]] if "category" in df.columns else None
except MemoryError:
    print("Out of memory")
    #chunk_iter = pd.read_csv("big_dataset.csv", chunksize=10000)
    #results = []
    #for chunk in chunk_iter:
    #    results.append(chunk.groupby("category").mean())
    #processed = pd.concat(results)
    
    #import dask.dataframe as dd
    #ddf = dd.read_csv("big_dataset.csv")
    #processed = ddf.groupby("category").mean().compute()
