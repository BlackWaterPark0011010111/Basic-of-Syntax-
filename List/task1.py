"""Представь, что ты работаешь в компании MatrixCorp, которая занимается обработкой изображений. 
Твой менеджер дал тебе задание создать простую программу, которая поможет анализировать и модифицировать матрицы, 
представляющие изображения в оттенках серого.

Задача:
Написать программу на Python, которая:

Создаёт матрицу (представляющую изображение) размером 5×5, заполненную случайными значениями от 0 до 255 (где 0 - черный, 255 - белый, а числа между ними - оттенки серого).
Отображает матрицу в виде чисел, имитируя пиксели изображения.
Позволяет пользователю выбрать действие:
Инвертировать цвета (заменить все значения x на 255 - x).
Размытие (заменить каждый элемент на среднее значение его соседей).
Найти самый яркий пиксель (вывести максимальное значение и его координаты).
Выход из программы.
 Как работает код?
Создаётся матрица 5×5 со случайными значениями от 0 до 255.
Программа выводит её на экран.
Пользователь может выбрать одно из действий:
Инвертировать цвета (заменяет x на 255 - x).
Применить размытие (заменяет значение каждого элемента на среднее значение его соседей).
Найти самый яркий пиксель и его координаты.
Выйти из программы.
После каждого действия матрица обновляется и снова отображается на экране."""
"""Imagine you work for MatrixCorp, an image processing company. 
Your manager has given you the task of creating a simple program that will help you analyse and modify the matrices 
that represent images in shades of grey.

Task:
Write a Python programme that:

Creates a 5×5 matrix (representing an image) filled with random values from 0 to 255 (where 0 is black, 255 is white, and the numbers in between are shades of grey).
Displays the matrix as numbers, mimicking the pixels of an image.
Allows the user to select an action:
Invert colours (replace all x values with 255 - x).
Blur (replace each element with the average of its neighbours).
Find the brightest pixel (output the maximum value and its coordinates).
Exit the programme.
 How does the code work?
A 5×5 matrix with random values from 0 to 255 is created.
The programme displays it on the screen.
The user can choose one of the actions:
Invert colours (replaces x with 255 - x).
Apply blur (replaces the value of each element with the average of its neighbours).
Find the brightest pixel and its coordinates.
Exit the programme.
After each action, the matrix is updated and displayed on the screen again.‘’‘’’

Translated with DeepL.com (free version)"""



import random
#to create matrices with gray results (from 0 to 255)
#для создания матрицы с оттенками серого (от 0 до 255)
def create_matrix(rows, cols):
    return [[random.randint(0, 255) for _ in range(cols)] for _ in range(rows)]

#для вывода матрицы to display the matrix
def print_matrix(matrix):
    for row in matrix:
        #align the output of numbers
        print(" ".join(f"{val:3}" for val in row))  #выравниваем вывод чисел

#инвертирование цветов
def invert_colors(matrix):#invert colors

    return [[255 - val for val in row] for row in matrix]


def blur_matrix(matrix):#для размытия
    rows, cols = len(matrix), len(matrix[0])
    new_matrix = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):

        for j in range(cols):

            neighbors = [matrix[i][j]]
            for di in [-1, 0, 1]:

                for dj in [-1, 0, 1]:

                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        neighbors.append(matrix[ni][nj])
            new_matrix[i][j] = sum(neighbors) // len(neighbors)
    return new_matrix

#функция поиска самого яркого пикселя
#brightest pixel search function
def find_brightest_pixel(matrix):

    max_val = -1
    max_pos = (0, 0)
    
    for i in range(len(matrix)):

        for j in range(len(matrix[0])):

            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_pos = (i, j)
    
    return max_val, max_pos

#main
rows, cols = 5, 5

#create a matrix
image_matrix = create_matrix(rows, cols)  #cоздаём матрицу

while True:
    print("\nORIGINALE IMAGE (matrix):")
    print_matrix(image_matrix)

    print("\nSELECT ACTION:")
    print("1. INVERT COLORS")
    print("2. BLUR THE IMAGE")
    print("3. FIND THE BRIGHTEST PIXEL")
    print("4. EXIT")

    choice = input("ENTER A NUMBER OF ACTION: ")

    if choice == "1":
        image_matrix = invert_colors(image_matrix)
        print("\nTHE COLORS ARE INVERTED")
    elif choice == "2":
        image_matrix = blur_matrix(image_matrix)
        print("\nTHE IMAGE IS BLURRY")
    elif choice == "3":
        bright_value, bright_pos = find_brightest_pixel(image_matrix)
        print(f"\nBRIGHEST PIXEL: {bright_value} ON A POSITION {bright_pos}")
    elif choice == "4":
        print("EXIT.")
        break
    else:
        print("WRONG CODE, TRY  AGAIN.")
