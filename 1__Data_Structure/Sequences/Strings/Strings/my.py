print("----------------------------------------------------------------1---")

# Task 1
# Your task is to create a variable called city to store the data: London, then print the content of the city variable on the screen.
city = "London"
print(city)
print("--------------------------------------------------------------2-----")

# Task 2
# Your task is to create two variables, the first variable to be called city and will store the data: berlin, and the second variable to be called population and will store the data: 3645000.
# Then print the content of the city and population using a colon (:) in between. Make sure you capitalize the content of the city variable.
city = "berlin"
population = 3645000
print(f"{city.capitalize()}: {population}")
print("----------------------------------------------------------------3---")

# Task 3
# Your task is to create two variables, the first variable to be called city and will store the data: london, and the second variable to be called population and will store the data: 9000000.
# Then print the content of the city and population using their labels as shown in the output below. Make sure you check if the content of the city is a text.
# Print the appropriate results on screen as shown below.
city = "london"
population = 9000000
print(f"City: {city.capitalize()} ({isinstance(city, str)})")
print(f"Population: {population}")
print("----------------------------------------------------------------4---")

# Task 4
# Create a variable called text to store the data: Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.
# Your task is to check if the word capital is included in the text, if so, print the index of the location inside the text string.
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
word = "capital"
if word in text:
    print(f"{word}: {text.index(word)}")
print("----------------------------------------------------------------5---")

# Task 5
# Create a variable called text to store the data: Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau.
# Your task is to split the content of the text variable and store it in a list.
text = "Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau."
text_list = text.split()
print(text_list)
print("----------------------------------------------------------------6--")

# Task 6
# Create a variable called text to store the data: Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.
# Your task is to replace the word capital with the phrase capital of Germany.
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
updated_text = text.replace("capital", "capital of Germany")
print(updated_text)
print("----------------------------------------------------------------7---")




#Задача 10. Генерация случайного пароля
#Программа должна сгенерировать случайный пароль из 10 символов, включая буквы, цифры и символы.
#Random Password Generator
#Write a program that generates a random password of a given length using letters, digits, and special characters.

import random
import string

def generate_password(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

print("Ваш случайный пароль:", generate_password())

print("----------------------------------------------------------------8---")


#Phone Number Validation
#Write a program that checks whether a phone number follows the format +7(XXX)XXX-XX-XX using regular expressions.

import re
# Проверка корректности номера телефона
phone = input("Введите номер телефона: ")
pattern = r"^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$"

if re.match(pattern, phone):
    print("Номер корректен")
else:
    print("Некорректный номер")

print("----------------------------------------------------------------9---")



#Сохранение и загрузка текста
#Напишите программу, которая сохраняет введенный текст в файл и затем считывает его обратно.
#Saving and Loading Text
#Write a program that saves the user-inputted text to a file and then reads it back from the file.

filename = "text.txt"

text = input("Введите текст для сохранения: ")
with open(filename, "w", encoding="utf-8") as file:
    file.write(text)

with open(filename, "r", encoding="utf-8") as file:
    print("Сохраненный текст:", file.read())

print("----------------------------------------------------------------10---")


#Напишите программу, которая берет текущую дату и выводит ее в формате "01 января 2025".
#Current Date Formatting
#Write a program that retrieves the current date and displays it in the format "01 January 2025".


from datetime import datetime

months = {
    "01": "января", "02": "февраля", "03": "марта", "04": "апреля", "05": "мая", "06": "июня",
    "07": "июля", "08": "августа", "09": "сентября", "10": "октября", "11": "ноября", "12": "декабря"
}

today = datetime.today()
formatted_date = f"{today.day} {months[today.strftime('%m')]} {today.year}"
print(formatted_date)

print("----------------------------------------------------------------11---")



#Find and Replace
#The user enters a text, a word to search for, and a replacement word. The program replaces all occurrences of the searched word and outputs the modified text.
#Поиск и замена
#Пользователь вводит текст, слово для поиска и слово для замены. Программа заменяет все вхождения и выводит измененный текст.

text = input("Введите текст: ")
search = input("Какое слово заменить? ")
replace = input("На что заменить? ")

print(text.replace(search, replace))
print("----------------------------------------------------------------12---")



#Кодирование текста (шифр Цезаря)
#Напишите программу, которая запрашивает строку и сдвигает каждую букву в алфавите на 3 позиции вправо.
#Text Encoding (Caesar Cipher)
#Write a program that takes an input string and shifts each letter in the alphabet by 3 positions to the right.

def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

text = input("Введите текст: ")
print(caesar_cipher(text))