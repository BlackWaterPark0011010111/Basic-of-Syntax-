import time
#  decor to achieve logging and timing.
def log_func_call(func):
    def wrapper(*args, **kwargs):
        print(f"Func {func.__name__} called.")
        return func(*args, **kwargs)
    return wrapper
    
    #decor for changin a time working function
def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time= end_time - start_time
        print(f"Func {func.__name__} took {execution_time: .4f} seconds to execute.")
        return result
    return wrapper




# decorr for asking password before function
def secure_func(func):
    def wrapper(*args, **kwargs):
        password = input("Enter the password to run the function: ")
        if password == "secure123":
           return func(*args, **kwargs)
        else:
            print("Accesws denied")
    return wrapper


#decor
@log_func_call
@calculate_time
def simple_func():
    time.sleep(2) #funktion working 2 seconds

@secure_func
def secret_func():
    print("Secret datat displayed")


# TESTING
simple_func()
secret_func()