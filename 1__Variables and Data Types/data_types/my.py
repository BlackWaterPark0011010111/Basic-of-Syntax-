# decimal to binary
decimal_number = 27
binary_number = bin(decimal_number)
print("Binary:", binary_number)

print("-----------------------------------------------------------------------------1-------")

#binary to decimal
binary_str = "0b11011"
decimal_from_binary = int(binary_str, 2)
print("Decimal:", decimal_from_binary)

print("-----------------------------------------------------------------------------2-------")

#decimal to hexadecimal

hexadecimal_number = hex(decimal_number)
print("Hexadecimal:", hexadecimal_number)

print("----------------------------------------------------------------------------3--------")

#hexadecimal to decimal
hex_str = "0x1b"
decimal_from_hex = int(hex_str, 16)
print("Decimal:", decimal_from_hex)

print("-------------------------------------------------------------------------4-----------")

#binary to hexadecimal
hex_from_binary = hex(int(binary_str, 2))
print("Hexadecimal from Binary:", hex_from_binary)

print("-------------------------------------------------------------------------5-----------")

# hexadecimal to binary
binary_from_hex = bin(int(hex_str, 16))
print("Binary from Hexadecimal:", binary_from_hex)

print("-------------------------------------------------------------------------6-----------")

#decimal to octal
octal_number = oct(decimal_number)
print("Octal:", octal_number)

print("--------------------------------------------------------------------------7----------")

#octal to decimal
octal_str = "0o33"
decimal_from_octal = int(octal_str, 8)
print("Decimal from Octal:", decimal_from_octal)

print("---------------------------------------------------------------------------8---------")


int = 10
float_value = float(int)  
string = str(int)  
bool = bool(int)  

print("Integer:", int, type(int))
print("Float:", float_value, type(float_value))

print("String:", string, type(string))
print("Boolean:", bool, type(bool))

print("----------------------------------------------------------------------------9--------")


print("Welcome to the data type checker!")

user_input = input("Enter something (number, text, boolean, etc.): ")

if user_input.isdigit():
    converted_value = int(user_input)

    print(f"You entered an integer: {converted_value} (Type: {type(converted_value)})")
elif user_input.replace(".", "", 1).isdigit():
    converted_value = float(user_input)

    print(f"You entered a float: {converted_value} (Type: {type(converted_value)})")
elif user_input.lower() in ["true", "false"]:

    converted_value = bool(user_input.capitalize())
    print(f"You entered a boolean: {converted_value} (Type: {type(converted_value)})")
else:

    converted_value = str(user_input)
    print(f"You entered a string: {converted_value} (Type: {type(converted_value)})")

print("----------------------------------------------------------------------------10--------")


print("converting data types:")

if isinstance(converted_value, int):
    print(f"Integer {converted_value} as string: {str(converted_value)}")
    print(f"Integer {converted_value} as float: {float(converted_value)}")

elif isinstance(converted_value, float):
    print(f"Float {converted_value} as string: {str(converted_value)}")

    print(f"Float {converted_value} as integer: {int(converted_value)}")

elif isinstance(converted_value, str):
    print(f"Length of string '{converted_value}': {len(converted_value)}")

print("End of program!")

print("----------------------------------------------------------------------------11--------")


print("Welcome to the calculator!")


num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

if num1.replace(".", "", 1).isdigit() and num2.replace(".", "", 1).isdigit():
    num1 = float(num1) if "." in num1 else int(num1)
    num2 = float(num2) if "." in num2 else int(num2)

    print(f"Addition: {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction: {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")

    if num2 != 0:
        print(f"Division: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero is not allowed!")

else:
    print("Invalid input. Please enter numbers only!")

print("-----------------------------------------------------------------------------12-------")


print("test logical operations.")


bool1 = input("Enter first booln value (True/False): ").capitalize()
bool2 = input("Enter second bool value (True/False): ").capitalize()

if bool1 in ["True", "False"] and bool2 in ["True", "False"]:
    bool1 = bool(bool1 == "True")
    bool2 = bool(bool2 == "True")

    print(f"{bool1} AND {bool2} = {bool1 and bool2}")
    print(f"{bool1} OR {bool2} = {bool1 or bool2}")
    print(f"NOT {bool1} = {not bool1}")
    print(f"NOT {bool2} = {not bool2}")

else:
    print("Invalid boolean values entered!")

print("End of program!")

print("-----------------------------------------------------------------------------13-------")
