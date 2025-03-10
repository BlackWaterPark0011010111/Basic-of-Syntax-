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
