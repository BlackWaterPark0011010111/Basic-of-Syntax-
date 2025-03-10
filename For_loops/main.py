print("-----------------------------------------------------------------------1-----")

# multiplication table
# Запрашиваем число у пользователя и выводим таблицу умножения от 1 до 10

num = int(input("Input a number: "))
print("\nResults of multiplication by", num, ":\n")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("----------------------------------------------------------------------2------")

# pattern with loop
# Выводим пирамиду чисел, где каждая строка содержит повторяющееся число

for i in range(1, 10):
    print(str(i) * i)

print("-----------------------------------------------------------------------3-----")

#  reverse word
# Запрашиваем слово и выводим его в обратном порядке, используя цикл

word = input("Input a word to reverse: ")
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

print("Reversed word:", reversed_word)

print("--------------------------------------------------------------------4--------")

#  upper letters
# Меняем каждую букву 'o' на 'O' в введённой строке

text = input("input a text: ")
modified_text = ""

for char in text:
    if char == "o":
        modified_text += "O"
    else:
        modified_text += char

print(modified_text)

print("-----------------------------------------------------------------------5-----")

# count digits and letters
# Считаем количество букв и цифр в введённом пользователем тексте

text = input("input your characters: ")
letters = 0
digits = 0

for char in text:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1

print("number of digits: ", digits)
print("number of letters: ", letters)

print("-------------------------------------------------------------------6---------")
#- sum of even and odd numbers separately
# Запрашиваем у пользователя число и считаем сумму всех четных и нечетных чисел до него
num = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0

for i in range(1, num+1):
    if i % 2 == 0:
        even_sum+= i
    else:
        odd_sum +=i

print(f"summ of even num: {even_sum}")
print(f"sum of odd num: {odd_sum}")
print("---------------------------------------------------------------------7-------")


num = int(input("enter a number: "))
is_prime = True

if num> 1:
    for i in range(2, int(num ** 0.5)+ 1):
        if num% i == 0:
            is_prime = False
            break

else:
    is_prime = False

print(f"{num} is {'a prime' if is_prime else 'not a PRIME'} NUMBER.")

print("--------------------------------------------------------------------8--------")


#  Fibonacci sequence
# Генерируем n чисел последовательности Фибоначчи

n = int(input("ENTER THE NUMBER OF FIBONACCI: "))
a,b = 0,1

for _ in range(n):
    print(a, end=" ")
    a,b=b,a+b
print("----------------------------------------------------------------------9------")
#pyramid pattern
# Рисуем пирамиду звездочек заданной высоты

rows = int(input("ENTER NUMBER OF ROWS FOR PYRAMID: "))
for i in range(1, rows + 1):
    print(" "* (rows -1) + "*" *i)

print("---------------------------------------------------------------------10-------")

#reverse a number
# Переворачиваем число, используя цикл

num = int(input("ENTER A NUMBER: "))
reversed_num = 0

while num>0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print("REVERSED NUMBER: ", reversed_num)        
print("--------------------------------------------------------------------11--------")

# count vowels and consonants
# Подсчитываем количество гласных и согласных в строке

text = input("ENTER A STRING: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count +=1
        else:
            consonant_count +=1

print(f" VOWELS: {vowel_count}, CONSONANTS: {consonant_count}")

print("---------------------------------------------------------------------12-------")
 
 #find the largest digit in a number
# Находим самую большую цифру в числе
int = input("ENTER A NUMBER: ")
larg_dig = max(int(digit) for digit in num)

print("LARGEST DIGIT: ", larg_dig)

print("--------------------------------------------------------------------13--------")
 #  remove duplicates from a list
# Убираем дубликаты из списка

number = [int(x) for x in input("ENTER NUMBERS SEPARATED BY SPACE: "). split()]
unique_num = []

for num in number:
    if num not in unique_num:
        unique_num.append(num)


print("LIST WITHOUT DUPLICATES: ", unique_num)

print("--------------------------------------------------------------------14--------")

# check if a string is a palindrome
# Проверяем, является ли строка палиндромом
text = input("ENTER A STRING: "). lover()
is_palidrome = True

for i in range(len(text) // 2):

    if text[i] != text[-(i +1)]:
        is_palidrome= False
        break

print(f"THE STRING IS {'A PALIDROME' if is_prime else 'NOT A PALIDROME'}")

print("----------------------------------------------------------------------15------")

# count occurrences of a character
# Подсчитываем количество вхождений определенного символа в строке


text = input("ENTER A STRING: ")
char_count = input("ENTER THE CHARACTER TO COUNT: ")

count = 0

for char in text:
    if char == char_count:
        count+=1
print(f"CHARACTER '{char_count}' AAPEARS {count} TIMES IN THE TEXT")
print("------------------------------------------------------------------16----------")

# sum of digits in a number
# Вычисляем сумму всех цифр в числе

num = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in num)

print("Sum of digits:", digit_sum)

print("---------------------------------------------------------------------17-------")

# find the first repeating element in a list
# Находим первый повторяющийся элемент в списке

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
seen = set()
first_repeating = None

for num in numbers:
    if num in seen:
        first_repeating = num
        break
    seen.add(num)

print("First repeating element:", first_repeating if first_repeating is not None else "None")

print("---------------------------------------------------------------------18-------")

# print numbers in a spiral order
# Выводим числа в виде спирали (матрицы NxN)

N = int(input("ENTER SIZE OF MATRIX: "))
matrix = [[0] * N for _ in range(N)]
num = 1
left,right, top, bottom = 0, N -1, 0, N - 1

while num <= N * N:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1

for row in matrix:
    print(" ".join(f"{x:2}" for x in row))
    print("-----------------------------------------------------------------19-----------")

#print Pascal's triangle
# Выводим треугольник Паскаля

rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

print("---------------------------------------------------------------------20-------")
#find pairs with given sum in a list
# Находим все пары чисел в списке, сумма которых равна заданному числу

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
target = int(input("Enter target sum: "))

print(f"Pairs with sum {target}:")

found_pairs = set() # we need to use set - to get rid of duplicates
seen_numbers = set() 

for num in numbers:
    complement = target - num
    if complement in seen_numbers:
        pair = tuple(sorted((num, complement)))
        if pair not in found_pairs:
            print(pair)
            found_pairs.add(pair)
    seen_numbers.add(num)

print("----------------------------------------------------------------------------")
