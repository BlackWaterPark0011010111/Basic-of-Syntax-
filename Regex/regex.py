import re
import calendar

text = 'The cost of tomatoes is 23 Dollars and the cost of potatoes is 12 dollars.\tSo the value of these products in your basket is amount 35 dollars'
pattern = '[0-9]'

matches = re.findall(pattern,text)
print(matches)

print('--------------------------------------------1-')


text = 'The cost of tomatoes is 23 Dollars and the cost of potatoes is 12 dollars.\tSo the value of these products in your basket is amount 35 dollars'
pattern = '\d'

matches = re.findall(pattern,text)
print(matches)
print('-------------------------------------------2--')



text = 'The cost of tomatoes is 23 Dollars and the cost of potatoes is 12 dollars.\tSo the value of these products in your basket is amount 35 dollars'
pattern = '\D'

matches = re.findall(pattern,text)
print(matches)

print('-------------------------------------------3--')

text = 'The cost of tomatoes is 23 Dollars and the cost of potatoes is 12 dollars.\tSo the value of these products in your basket is amount 35 dollars'
pattern = '\s'

matches = re.findall(pattern,text)
print(matches)

print('-------------------------------------------4--')

text = 'The cost of tomatoes is 23 Dollars and the cost of potatoes is 12 dollars.\tSo the value of these products in your basket is amount 35 dollars'
pattern = '\S'

matches = re.findall(pattern,text)
print(matches)
print('-------------------------------------------5--')

text = 'The cost of tomatoes is 23 Dollars and the cost of potatoes is 12 dollars.\tSo the value of these products in your basket is amount 35 dollars'
print(text)
pattern = '\W'
#includes punctuation
pattern = '\S'
matches = re.findall(pattern,text)
print(matches)


print('-------------------------------------------6--')
#bounder delimiter
text = 'The cost of tomatoes is 23 Dollars and the cost of potatoes is 12 dollars.\tSo the value of these products in your basket is amount 35 dollars'
print(text)
pattern = 'toes\b'
matches = re.findall(pattern,text)
print(matches)

print('-----------------------------------------7----')
#bounder delimiter - HINT please use raw string in regex pattern for it to work
text = r'The cost of tomatoes is 23 Dollars and the cost of potatoes is 12 dollars.\tSo the value of these products in your basket is amount 35 dollars'
print(text)
pattern = r'toes\b'
matches = re.findall(pattern,text)
print(matches)
print('----------------------------------------8---')
#metachars

pattern = '.*'

matches = re.findall(pattern,text)
print(matches)

print('---------------------------------------9---')

text = 'Hello'
pattern = 'H.*o'# показывает все слово которок ищем 

matches = re.findall(pattern,text)
print(matches)


print('---------------------------------------------10----')

text = 'Hello'
pattern = 'H.+o'# показывает все слово которок ищем 

matches = re.findall(pattern,text)
print(matches)

print('----------------------------------------11----')

text = 'colour'
pattern = 'colou?r'# показывает слово от начала Н до конца о 

matches = re.findall(pattern,text)
print(matches)
print('----------------------------------------12----')

from re import (
  findall,
  split,
  sub,
  search,
  IGNORECASE
) 

poem="Away, get your thee away; good friend, be goneThy comforts can do me no good at all.Thee they may hurt."
#use findall() function
mylist = findall('.', poem)
print(mylist)
#search
my_search=search('your', poem, flags=IGNORECASE)

#print(start_end_index)
print(my_search)
#split()
my_split = split('/n', poem)
print(my_split)

#sub
my_sub = sub('your', 'my', poem, flags=IGNORECASE)
print(my_sub)



print('----------------------------------------13----')

text = "Berlin is a world city of culture, politics, media and science"
matches = re.search(' ', text)
print(matches)
print('----------------------------------------14----')

text= "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.."
matches = re.search("Frankfurt", text)
print(matches)
print('----------------------------------------15---------')
text= "Berlin is a city of culture.."
matches = re.sub("\s", "-", text)
print(matches)
print('----------------------------------------16---')               

text="Berlin is a city of culture"
matches = re.search("in", text)
print(matches)
print('----------------------------------------17----')

text="Berlin is a city of culture"
matches = findall("[A-Z]", text)
print(matches)

print('----------------------------------------18----')


text = "The rain in Spain"


x = re.findall(r"\Bai", text)
print(x)






 

print("----------------------------------------25----------")

def remove_leading_trailing_zeros(input_str):
   
    stripped_str = input_str.strip('0')
    
    return stripped_str

input_str1 = "0023.0760023070"
input_str2 = "hello world"
input_str3 = "01230"

result1 = remove_leading_trailing_zeros(input_str1)
result2 = remove_leading_trailing_zeros(input_str2)
result3 = remove_leading_trailing_zeros(input_str3)

print(result1)  # Output: "23.0762307"
print(result2)  # Output: "hello world"
print(result3)  # Output: "1230"
print("----------------------------------------25----------")



text="Berlin is a city of culture."
matches = re.search(' ', text)
print(matches)
print('----------')




year = int(input("Enter your year: "))

if calendar.isleap(year):
    

    print("Your year is: ")

else:
    print("Your  year is not  ") 

mok = "0023.07623070, hello world, 01230"# тут мы убираем ноль

mok= mok.replace('0', '')
print(mok)