value = 15
if value > 10:
    print("Above threshold")
else:
    print("Below threshold")

#print("Above" if value > 10 else "Below")

num = -5
if num >= 0:
    print("Positive")
else:
    print("Negative")

#print("Positive" if num >= 0 else "Negative")

score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

#if score >= 90: print("A")
#elif score >= 80: print("B")
#else: print("C")

username = "root"
password = "secret"
if username == "root":
    if password == "secret":
        print("Login successful")
    else:
        print("Invalid password")
else:
    print("Unknown user")

#if username == "root" and password == "secret":
#    print("Authenticated")
#else:
#    print("Access denied")

items = ["apple", "banana", "orange"]
if "banana" in items:
    print("Banana available")

#for item in items:
#    if item == "banana":
#        print("Found banana")
#        break

#if any(item == "banana" for item in items):
#    print("Has banana")

config = {"version": 3, "mode": "production"}
if "version" in config:
    print(f"Version: {config['version']}")

#if config.get("version"):
#    print(f"Version: {config['version']}")

x, y, z = 5, 10, 3
if x > y and x > z:
    print("X is greatest")
elif y > z:
    print("Y is greatest")
else:
    print("Z is greatest")

#print(f"Greatest: {max(x, y, z)}")

input_data = "test"
if type(input_data) == str:
    print("String type")

#if isinstance(input_data, str):
#    print("String type")

result = None
if result == None:
    print("Empty result")

#if result is None:
#   print("No result")

message = "hello world"
size = len(message)
if size > 5:
    print(f"Message size: {size}")

#if (size := len(message)) > 5:
#    print(f"Size: {size}")

#print(f"Size: {len(message)}" if len(message) > 5 else "")
pw = "Secure123"
if len(pw) >= 8 and any(c.isupper() for c in pw) and any(c.isdigit() for c in pw):
    print("Strong password")

#if len(pw) < 8: print("Too short")
#elif not any(c.isupper() for c in pw): print("Need uppercase")
#elif not any(c.isdigit() for c in pw): print("Need digit")
#else: print("Strong")

temp = 22.5
if temp > 30:
    print("Heat warning")
elif temp < 5:
    print("Freeze warning")
else:
    print("Normal range")

#(print("Hot") if temp > 30 else print("Cold") if temp < 5 else print("OK"))

filename = "report.pdf"
if filename.endswith('.pdf'):
    print("PDF file")
elif filename.endswith('.docx'):
    print("Word file")
else:
    print("Unknown format")

#match filename.split('.')[-1]:
#    case 'pdf': print("PDF")
#    case 'docx': print("Word")
#    case _: print("Unknown")

cart_total = 350
items_count = 7
if cart_total > 500:
    print("30% discount")
elif cart_total > 300 and items_count > 5:
    print("20% discount")
else:
    print("No discount")

#discount = 30 if cart_total > 500 else 20 if cart_total > 300 and items_count > 5 else 0
#print(f"{discount}% off")

role = "editor"
if role == "admin":
    print("Full access")
elif role == "editor":
    print("Edit access")
elif role == "viewer":
    print("Read only")
else:
    print("No access")

#permissions = {
#    "admin": "Full",
#    "editor": "Edit",
#    "viewer": "Read"
#}
#print(f"{permissions.get(role, 'No')} access")

num = 7
if num > 0 and num % 2 != 0 and num < 10:
    print("Small positive odd")

#props = []
#if num > 0: props.append("positive")
#if num % 2 != 0: props.append("odd") 
#if num < 10: props.append("small")
#print(' '.join(props) if props else "No properties")

from datetime import datetime
hour = datetime.now().hour
if 5 <= hour < 12:
    print("Good morning")
elif 12 <= hour < 18:
    print("Good afternoon")
else:
    print("Good evening")

#print("Morning" if 5 <= hour < 12 else "Afternoon" if 12 <= hour < 18 else "Evening")

numbers = [3, 7, 2, 9, 5]
if numbers and all(n > 0 for n in numbers):
    print("All positive")

#if not numbers: print("Empty list")
#elif any(n <= 0 for n in numbers): print("Contains non-positive")
#else: print("All good")

text = "Python"
if text.startswith('P') and text.endswith('n') and len(text) > 3:
    print("Valid name")

#checks = [
#    text.startswith('P'),
#    text.endswith('n'),
#    len(text) > 3
#]
#print("Valid" if all(checks) else "Invalid")