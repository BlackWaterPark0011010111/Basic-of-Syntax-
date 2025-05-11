import datetime
def greet(name="User", date=datetime.datetime.now()):
    if date.hour < 12:
        return f"Good morning, {name}"
    elif date.hour < 18:
        return f"Good Afternoon, {name}"
    else:
        return f"Good night, {name} !"
    
print(greet(name="john", date= datetime.datetime(2025, 7, 7, 11, 50, 59)))
print(greet(date=datetime.datetime(2025, 9, 7, 12, 0, 1), name="john"))