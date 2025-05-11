print("----------------------------------------------------------------------------------1---------")
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7]
print("Original list:", numbers)
print("Without duplicates:", remove_duplicates(numbers))


print("----------------------------------------------------------------------------------2---------")
def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7]
print("Original list:", numbers)
print("Without duplicates:", remove_duplicates(numbers))

print("----------------------------------------------------------------------------------3---------")


words = ["banana", "apple", "cherry", "blueberry", "grape"]
sorted_words = sorted(words, key=len)
print("Sorted by length:", sorted_words)
print("-----------------------------------------------------------------------------------4--------")


def split_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]

numbers = list(range(1, 21))
print("Original list:", numbers)
print("Splitted list:", split_list(numbers, 5))


print("------------------------------------------------------------------------------------5-------")

def find_pairs(lst, target):
    pairs = []
    seen = set()
    for num in lst:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
target_sum = 10
print("Pairs with sum", target_sum, ":", find_pairs(numbers, target_sum))



print("-----------------------------------------------------------------------------------6--------")


import random

random_numbers = [random.randint(1, 100) for _ in range(20)]
even_numbers = [num for num in random_numbers if num % 2 == 0]

print("Random numbers:", random_numbers)
print("Even numbers:", even_numbers)

print("----------------------------------------------------------------------------------7---------")

from collections import Counter

def most_frequent(lst):
    count = Counter(lst)
    return count.most_common(1)[0]

numbers = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7, 2, 2]
print("Most frequent element:", most_frequent(numbers))
print("----------------------------------------------------------------------------------8---------")

from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))

numbers = [1, 2, 3]
print("Permutations:", generate_permutations(numbers))
print("----------------------------------------------------------------------------------9---------")
def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Spiral order:", spiral_order(matrix))

print("---------------------------------------------------------------------------------10----------")
def is_sublist(lst, sub):
    n, m = len(lst), len(sub)
    for i in range(n - m + 1):
        if lst[i:i + m] == sub:
            return True
    return False

main_list = [1, 2, 3, 4, 5, 6, 7, 8]
sub_list = [4, 5, 6]
print("Is sublist present?", is_sublist(main_list, sub_list))

print("----------------------------------------------------------------------------------11---------")
def rpn_calculator(expression):
    stack = []
    operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}

    for token in expression.split():
        if token in operators:
            b, a = stack.pop(), stack.pop()
            stack.append(operators[token](a, b))
        else:
            stack.append(float(token))
    
    return stack[0]

expr = "3 4 + 2 * 7 /"
print("RPN result:", rpn_calculator(expr))
print("----------------------------------------------------------------------------------12---------")
nums = [10, 3, 8, 6, 9, False, "World", 3.14, [2, 4, 6]]

nums[0] = 99
nums[5] = 2.71

print(nums[-1][0])  # Выведет первый элемент вложенного списка


# Функции списков
values = [8, 3, 6]
values.append(42)  
values.insert(2, False)  # Вставляем элемент в позицию 2

extra_values = [1, 5, 9]
values.extend(extra_values)  # Расширяем список другим списком

values.sort() 
values.pop(1)  # Удаляем элемент по индексу
values.remove(5)  # Удаляем первый встреченный элемент 5

# print(values.count(False))  
# print(len(values))
print("---------------------------------------------------------------------------------13----------")
a = [
    a + b
    for a in "list"
    if a != "s"  # исключаем "s"
    for b in "soup"
    if b != "u"  # исключаем "u"
]
print(a)
print("----------------------------------------------------------------------------------14---------")


print("-" * 82 + "1" + "-" * 50)

def unique_elements(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

nums = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7]
print("Original:", nums)
print("No duplicates:", unique_elements(nums))

print("-" * 82 + "2" + "-" * 50)

def unique_elements(lst):
    return list(set(lst))

nums = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7]
print("Original list:", nums)
print("Without duplicates:", unique_elements(nums))

print("-------------------------------------------------------------------------------15------------")

print("-" * 82 + "3" + "-" * 50)

fruits = ["banana", "apple", "cherry", "blueberry", "grape"]
sorted_fruits = sorted(fruits, key=len)
print("Sorted by length:", sorted_fruits)

print("-" * 82 + "4" + "-" * 50)

def split_into_chunks(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

nums = list(range(1, 21))
print("Original:", nums)
print("Chunked:", split_into_chunks(nums, 5))

print("---------------------------------------------------------------------------------16----------")


print("-" * 82 + "5" + "-" * 50)

def find_sum_pairs(lst, target):
    seen = set()
    pairs = []
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)
    return pairs

nums = [1, 3, 5, 7, 9, 2, 4, 6, 8]
target_sum = 10
print("Pairs summing to", target_sum, ":", find_sum_pairs(nums, target_sum))

print("-------------------------------------------------------------------------------------17------")


print("-" * 82 + "6" + "-" * 50)

import random

random_vals = [random.randint(1, 100) for _ in range(20)]
even_vals = [num for num in random_vals if num % 2 == 0]

print("Random values:", random_vals)
print("Even values:", even_vals)

print("------------------------------------------------------------------------------------18-------")


print("-" * 82 + "7" + "-" * 50)

from collections import Counter

def most_common_element(lst):
    counter = Counter(lst)
    return counter.most_common(1)[0]

nums = [1, 2, 3, 2, 4, 5, 1, 6, 4, 7, 2, 2]
print("Most frequent element:", most_common_element(nums))
print("----------------------------------------------------------------------------------19---------")

print("-" * 82 + "8" + "-" * 50)

from itertools import permutations

def generate_permutations(lst):
    return list(permutations(lst))

nums = [1, 2, 3]
print("Permutations:", generate_permutations(nums))

print("--------------------------------------------------------------------------------20-----------")

print("-" * 82 + "9" + "-" * 50)

def traverse_spirally(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Spiral traversal:", traverse_spirally(matrix))

print("--------------------------------------------------------------------------------21-----------")

print("-" * 82 + "10" + "-" * 50)

def is_sublist_of(lst, sub_lst):
    n, m = len(lst), len(sub_lst)
    for i in range(n - m + 1):
        if lst[i:i + m] == sub_lst:
            return True
    return False

main_list = [1, 2, 3, 4, 5, 6, 7, 8]
sub_list = [4, 5, 6]
print("Sublist exists?", is_sublist_of(main_list, sub_list))
print("---------------------------------------------------------------------------------22----------")

print("-" * 82 + "11" + "-" * 50)

def reverse_polish_calculator(expr):
    stack = []
    operators = {"+": lambda x, y: x + y, "-": lambda x, y: x - y, "*": lambda x, y: x * y, "/": lambda x, y: x / y}

    for token in expr.split():
        if token in operators:
            b, a = stack.pop(), stack.pop()
            stack.append(operators[token](a, b))
        else:
            stack.append(float(token))
    
    return stack[0]

expression = "3 4 + 2 * 7 /"

print("RPN result:", reverse_polish_calculator(expression))


print("-------------------------------------------------------------------------------23------------")

print("-" * 82 + "12" + "-" * 50)

nums = [10, 3, 8, 6, 9, False, "World", 3.14, [2, 4, 6]]

nums[0] = 99
nums[5] = 2.71

print(nums[-1][0])  # Outputs the first element of the nested list

# List operations
values = [8, 3, 6]
values.append(42)
values.insert(2, False)  # Insert False at index 2

extra_values = [1, 5, 9]
values.extend(extra_values)  # Extend list with another list

values.sort()
values.pop(1)  # Remove element at index 1
values.remove(5)  # Remove first occurrence of 5

# print(values.count(False))
# print(len(values))

print("-------------------------------------------------------------------------------24------------")

print("-" * 82 + "13" + "-" * 50)

a = [
    a + b
    for a in "list"
    if a != "s"
    for b in "soup"
    if b != "u"
]
print(a)

print("-" * 82)
print("-------------------------------------------------------------------------------25------------")
""" You are given a two dimensional list of numbers. Calculate the mean of those numbers by implementing a mean method that takes a list as an argument. """


def mean(numbers):
    total = sum(sum(row) for row in numbers)
    count = sum(len(row) for row in numbers)
    return total / count if count else 0

numbers = [[5, 6, 3], [8, 3, 1], [9, 10, 4], [8, 4, 2]]
print(mean(numbers))