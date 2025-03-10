print("----------------------------------------------1---")
"""Create a variable called fruits and one after another add the elements Apples, Cherries and Strawberries. Loop over the list fruits and print every element to the screen.
"""
fruits = []
fruits.append('Apples')

fruits.append('Cherries')
fruits.append('Strawberries')
for fruit in fruits:
    print(fruit)
print("----------------------------------------------2---")
"""Create a variable cities which holds a list with the cities London, Paris, Berlin and Amsterdam. Print the sentence The capital city of Germany is: Berlin to the screen, using the string Berlin from the cities array.
"""
cities = ["Paris", "Berlin",  "London","Amsterdam"]

print("The capital city of Germany is: ", cities[2])

print("----------------------------------------------3---")
"""Store the colors cyan, magenta, green, yellow, black and white in a list called colors. Remove the colors green and white. Print the remaining colors to the screen.
"""
colors = ["cyan","magenta","green","yellow","black","white"]
colors.remove('green')
colors.remove("white")
for color in colors:
    print(color)
print("----------------------------------------------4---")
"""Store the letters p, e, n, g, u, i, n in a list. Combine those letters into a single string penguin. Capitalize that string and print it to the screen.
"""
letters = ["p","e","n","g","u","i","n",""]
penguin_word = "". join(letters).capitalize()
print(penguin_word)


print("----------------------------------------------5---")
"""You are given a list and two indizes. Implement a method swap that takes the list and the two indizes as arguments, swaps the values at the given indizes and returns the list."""
def swap(lst, index1,index2):
    lst[index1], lst[index2]= lst[index2], lst[index1]
    return lst

swap_list = [23,65,19,90]
print(swap(swap_list, 1, 3))


print("----------------------------------------------6---")
"""You are given a list of strings. Some of those strings may contain integers, for example Digital Car33r Institute. Implement a method digit_filter that takes a list of strings as an argument and only returns those strings that don't contain a number."""
def digit_filter(strings):
    return [s for s in strings if not any(char.isdigit() for char in s)]
l33t = ["Digital Car33r Institute", "DCI", "Digital", "Career", "Institut3"]
print(digit_filter(l33t))


print("----------------------------------------------7---")
"""You are given two lists with an unknown amount of elements. Both of those lists may have some elements in common. Implement a method intersection that takes those two lists as arguments and returns a third list only with the elements they have in common.
"""

def intersection(list_1,list_2):
    return list(set(list_1) & set(list_2))
list_1 = [15, 9, 10, 56, 23,78, 5, 4, 9]
list_2 = [9,4,67,455,43,12,535]
print(intersection(list_1, list_2))