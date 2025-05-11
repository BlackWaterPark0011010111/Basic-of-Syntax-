
  #function
def firstFunction():
    print("This is my first function")
    print('its doesnt not do anything')
    print('but it demonstrates how to avoid repetion of print function')
    

firstFunction()
funcTest = firstFunction()
print(funcTest)
print(type(funcTest))


def power(x,y):
      z = x**y
      return z
result = power(2.45, 3)
print( result)
print(type(result))

arg1 = input('Please specify the value you want to take to the power..')
arg2 = input('Please specify the value of x to which we willraise')
arg1 = float(arg1)
arg2 = float(arg2)
result = power(int(arg1), int(arg2))
print(result)
def add_number(num1, num2):
     sum = num1 + num2
     print('Sum: ', sum)
     

add_number(arg1, arg2)


print("-------------------------------------------------------------------------------2--")
"""ead book_titles.txt.
Use list comprehension to clean the titles:
Remove numbers.
Capitalize the first letter of each word.
Write the cleaned titles to cleaned/cleaned_book_titles.txt.
Bonus:

Find the 3 most common words in the titles and their counts.
Convert your function into a generator to handle large data sets efficiently.
Hint: Use split() and Counter from the collections module."""

import re
from collections import Counter

# Read the file 
with open('book_titles.txt', 'r') as file:
    raw_titles = file.readlines()

# Clean the titles using list comprehension
cleaned_titles = [
    ' '.join([word.capitalize() for word in re.sub(r'\d+', '', title).split()]) 
    for title in raw_titles
]

# Write the cleaned titles to a new file
with open('cleaned/cleaned_book_titles.txt', 'w') as file:
    file.write('\n'.join(cleaned_titles))

#top 3 most common words
words = ' '.join(cleaned_titles).split()
word_counts = Counter(words)

print("Top 3 most common words and their counts:")
for word, count in word_counts.most_common(3):
    print(f"{word}: {count}")
