"""Описание кода: Student Grades System
Этот код представляет собой простую систему управления оценками студентов с обработкой исключений.

Что делает программа?
Читает оценки из файла – Пользователь вводит имя файла, программа пытается открыть его и считать оценки.
Обрабатывает ошибки – Если файл отсутствует или содержит некорректные данные (нечисловые значения), программа сообщает об ошибке.
Вычисляет средний балл – Если данные корректны, программа считает среднюю оценку.
Выводит результат – Показывает средний балл или сообщает о невозможности расчета.
Код защищает программу от сбоев, обрабатывая различные исключения (FileNotFoundError, ValueError).
Функция read_grades(filename)

Открывает файл и читает его содержимое.
Проходит по строкам, пытаясь преобразовать их в float.
Если встречается ошибка (ValueError), выводит предупреждение.
Если файл пуст или в нем нет корректных оценок, вызывает исключение.
Обрабатывает FileNotFoundError, если файл отсутствует.
Функция calculate_average(grades)

Вычисляет средний балл.
Проверяет деление на ноль (ZeroDivisionError).
Основная программа

Запрашивает у пользователя имя файла.
Вызывает read_grades().
Если список оценок не пуст, вычисляет и выводит средний балл.
"""
"""Code Description: Student Grades System
This code is a simple student grade management system with exception handling.

What the programme does.
Reads grades from a file - The user enters a file name, the program tries to open the file and read the grades.
Handles errors - If the file is missing or contains incorrect data (non-numeric values), the programme reports an error.
Calculates the average grade - If the data is correct, the programme calculates the average grade.
Outputs the result - Shows the average grade or reports that the calculation was not possible.
The code protects the programme from failures by handling various exceptions (FileNotFoundError, ValueError).
Function read_grades(filename)

Opens a file and reads its contents.
It goes through the lines trying to convert them to float.
If an error (ValueError) is encountered, it displays a warning message.
If the file is empty or has no valid evaluations, throws an exception.
Handles FileNotFoundError if the file is missing.
Function calculate_average(grades)

Calculates the average grade.
Checks division by zero (ZeroDivisionError).
Main programme

Requests a file name from the user.
Calls read_grades().
If the list of grades is not empty, calculates and outputs the average grade.
"""
import os


current_dir = os.path.dirname(os.path.realpath(__file__))
new_directory = os.path.join(current_dir)
os.chdir(new_directory)
def read_grades_from_file(filename):
    try:
        if not os.path.exists(filename):
            print(f"Error: The file {filename} was not found.")
            return []
        with open(filename, "r") as file:
            grades = file.readlines()
            grades = [int(grade.strip()) for grade in grades]
            return grades
    except ValueError:
        print("Error: File contains non-numeric data.")
        return []

def calculate_average(grades):
    try:
        if not grades:
            raise ValueError("No grades available to calculate the average.")
        avg = sum(grades) / len(grades)
        return avg
    except ValueError as e:
        print(f"Error: {e}")
        return None

def main():
    print(f"Current working directory: {os.getcwd()}")
    filename = input("Enter the filename containing student grades: ")
    
    grades = read_grades_from_file(filename)
    
    if grades:
        average = calculate_average(grades)
        if average is not None:
            print(f"The average grade is: {average:.2f}")
        else:
            print("Failed to calculate the average.")
    else:
        print("No grades were read. Exiting program.")

if __name__ == "__main__":
    main()
