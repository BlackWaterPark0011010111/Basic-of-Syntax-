import json
import os
from pathlib import Path
import time
import psycopg2
from psycopg2 import pool
from contextlib import contextmanager
import requests
import pandas as pd
import numpy as np
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
import asyncio
import aiohttp
print(aiohttp.__version__)
import traceback
import logging

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

"""Custom exception for data validation"""
class ValidationError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

def validate_user_data(data):
    errors = []
    if not data.get("username"):
        errors.append("Missing username")
    if len(data.get("password", "")) < 8:
        errors.append("Password too short")
    if errors:
        raise ValidationError("Invalid user data", errors)

try:
    user_data = {"username": "johndoe", "password": "123"}
    validate_user_data(user_data)
except ValidationError as e:
    print(f"Validation failed: {', '.join(e.errors)}")
    #logger.error(f"Validation errors: {e.errors}")
    #user_data["is_valid"] = False

    #error_details = {
    #    "error": str(e),
    #    "details": e.errors,
    #    "timestamp": datetime.now().isoformat()
    #}

    #user_data.setdefault("username", "guest")
    #user_data["password"] = "defaultPassword123"
    #validate_user_data(user_data)

from concurrent.futures import ThreadPoolExecutor, as_completed

def process_item(item):
    try:
        return item * 2
    except Exception as e:
        return f"Error processing {item}: {str(e)}"

items = [1, 2, "three", 4, None, 5]
with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [executor.submit(process_item, item) for item in items]
    results = []
    for future in as_completed(futures):
        try:
            results.append(future.result())
        except Exception as e:
            results.append(f"Future failed: {str(e)}")

    #results = list(executor.map(process_item, items))

    #from concurrent.futures import ProcessPoolExecutor
    #with ProcessPoolExecutor() as executor:
    #    results = list(executor.map(process_item, items))

    #import asyncio
    #async def async_process():
    #    return await asyncio.gather(
    #        *(async_process_item(item) for item in items),
    #        return_exceptions=True
    #    )
    #results = asyncio.run(async_process())

print("Processing results:", results)

class DatabaseTransaction:
    def __enter__(self):
        self.conn = psycopg2.connect(DB_URL)
        self.conn.autocommit = False
        return self.conn.cursor()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
            #logger.error(f"Transaction failed: {exc_val}")
            #if isinstance(exc_val, DeadlockDetected):
            #    time.sleep(1)
            #    return True  #retry by suppressing exception
            
        self.conn.close()
        return False  #re-raise 

try:
    with DatabaseTransaction() as cursor:
        cursor.execute("UPDATE accounts SET balance = balance - 100 WHERE id = 1")
        cursor.execute("UPDATE accounts SET balance = balance + 100 WHERE id = 2")
        #raise Exception("Random failure")
except Exception as e:
    print(f"Transaction failed: {e}")
    #if isinstance(e, psycopg2.DatabaseError):
    #    send_alert_to_dba(str(e))
else:
    print("Transaction succeeded")

try:#TODO:
    #try:  
        #import missing_package
    #except ImportError as e:
        raise RuntimeError("Dependency missing") from e
except RuntimeError as e:
    print(f"Main error: {e}")
    print(f"Caused by: {e.__cause__}")
    #import traceback
    #Traceback.print_exc()
    
    #class ApplicationError(Exception):
    #    def __init__(self, message, cause=None):
    #        super().__init__(message)
    #        self.cause = cause
    #raise ApplicationError("Config failed", e)
class DataTransformError(Exception):
    pass

def transform_data(raw_data):
    if not raw_data:
        raise DataTransformError("Данные пусты!")
    
    processed = {
        "filename": raw_data.get("filename"),
        "content": raw_data.get("content", "").upper()
    }
    return processed

def process_files(file_list):
    results = []
    for filename in file_list:
        try:
            with open(filename, 'r') as f:
                try:
                    data = json.load(f)
                    try:
                        processed = transform_data(data)
                        results.append(processed)
                    except DataTransformError as e:
                        print(f"Transform failed for {filename}: {e}")
                except json.JSONDecodeError:
                    print(f"Invalid JSON in {filename}")
        except IOError as e:
            print(f"Can't process {filename}: {e}")
            continue
        except Exception as e:
            print(f"Unexpected error with {filename}: {e}")
            raise
    
    return results

file_list = ["data1.json", "data2.json", "invalid.txt"]
try:
    output = process_files(file_list)
except KeyboardInterrupt:
    print("Processing interrupted by user")
    # save_partial_results(output)
    raise
except Exception as e:
    print(f"Fatal processing error: {e}")
    #send_critical_alert(f"Processing crashed: {e}")
else:
    print(f"Successfully processed {len(output)} files")
finally:
    print("Processing complete")
    #cleanup_temporary_files()


