"""Python Regex
In this exercise, we will focus on the use and manipulation of text in Python, including:


Task 1
Create a variable called text to store the data: Berlin is a world city of culture, politics, media and science. . Then search for the first white space character in the string and print its location using the appropriate label.
Your result should look like this:
The first white-space character is located at position: 6


Task 2
Create a variable called text to store the data: Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital. . Then search for the word Frankfurt in the string .

Your result should look like this: None


Task 3
Create a variable called text to store the data: Berlin is a city of culture. . Replace the spaces with a hyphen.

Your result should look like this: Berlin-is-a-city-of-culture.


Task 4
Create a variable called text to store the data: Berlin is a city of culture. . Search if the phrase in appears inside the string. Print the output of the regex function.

Your result should look like this: <re.Match object; span=(4, 6), match='in'>


Task 5
Use the text variable from the previous task. Create a regular expression to look for any word that starts with an upper case "B". Print the position (start- and end-position) of the first match occurrence.

Your result should look like this: (0, 6)


Task 6
Create a variable called text to store the data: The rain in Spain.. Count how many times the subphrase ai appears in the string. Print the results on the screen.

Your result should look like this: 2

Task 7
remove leading and trailing zeros

Create a function that takes a string input as a number and replaces leading and trailing zeros.

Task8 math
Create a function that takes a string input and checks if it is a mathematical 
expression. Supported operators: +, -, *, /, % and only integers

Task 9
Make any face happy. Create a function that takes a sentence containing sad faces and turn them 
into happy ones! This involves changing only the mouths.
Make sure to only change the face if there are eyes before them, round(3.4) 
wouldn't become round)3.4) (for example).


"""

print("--------------------------------------------------------------------------1----")
import re

text = "Berlin is a world city of culture, politics, media and science."
match = re.search(r'\s', text)
if match:
    print(f"The first white-space character is located at position: {match.start()}")



print("--------------------------------------------------------------------------2----")

text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."
match = re.search(r'Frankfurt', text)
print(match)
print("--------------------------------------------------------------------------3----")
text = "Berlin is a city of culture."
text = re.sub(r'\s', '-', text)
print(text)


print("--------------------------------------------------------------------------4---")
text = "Berlin is a city of culture."
match = re.search(r'in', text)
print(match)
print("--------------------------------------------------------------------------5---")
text = "Berlin is a city of culture."
match = re.search(r'\bB\w+', text)
if match:
    print(match.span())

print("--------------------------------------------------------------------------6----")


text = "The rain in Spain."
matches = re.findall(r'ai', text)
print(len(matches))


print("-------------------------------------------------------------------------7-----")



def remove_zeros(number_str):
    """Removes leading and trailing zeros from a numeric string."""
    if not re.match(r"^\d+(\.\d+)?$", number_str):  
        return number_str 
    number_str = re.sub(r"^0+(\d)", r"\1", number_str) 
    number_str = re.sub(r"\.?0+$", "", number_str) 
    return number_str


print(remove_zeros("0023.07623070"))
print(remove_zeros("hello world"))
print(remove_zeros("01230")) 
print(remove_zeros("0000.500"))
print(remove_zeros("000"))    


print("-------------------------------------------------------------------------8-----")

def is_math_expression(expression):
    pattern = r"^\s*\d+\s*[\+\-\*/%]\s*\d+\s*$"
    return bool(re.match(pattern, expression))


print(is_math_expression("5 + 2"))       
print(is_math_expression("9 * 1"))   

print(is_math_expression("hello world")) 

print(is_math_expression("123"))         

print(is_math_expression("5 + foo"))     

print(is_math_expression("  10  / 2 "))  
print(is_math_expression("7%3"))   

print(is_math_expression("4 ** 2"))   


print("-------------------------------------------------------------------------9-----")

def make_happy(sentence):
    result = []
    for char in sentence:
        if char in [":", "8", "x", ";"]:
            result.append(char)
        elif char == "(" and result and result[-1] in [":", "8", "x", ";"]:
            result[-1] = result[-1] + ")"
        else:
            result.append(char)
    return ''.join(result)


print(make_happy("My current mood: :("))  
print(make_happy("I was hungry 8("))     
print(make_happy("print('x(')"))         
#Here, we go through the characters of the string and if we 
#find a face with a sad mouth (for example, :(, 8(, x(), 
#we change it to a happy one. If it's not a face with a sad mouth, we simply add the character to the result.



