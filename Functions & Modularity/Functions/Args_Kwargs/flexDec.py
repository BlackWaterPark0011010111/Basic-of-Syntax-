import functools
import logging

logging.basicConfig(level=logging.DEBUG)

def log_function(*args, **kwargs):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logging.debug(f"Calling function {func.__name__} with arguments: {args}, {kwargs}")
            result = func(*args, **kwargs)
            logging.debug(f"Function {func.__name__} returned: {result}")
            return result
        return wrapper
    return decorator

@log_function('info', level='debug')
def add(a, b):
    return a + b

@log_function('warn', level='error')
def subtract(a, b):
    return a - b

add(5, 3)
subtract(10, 4)


