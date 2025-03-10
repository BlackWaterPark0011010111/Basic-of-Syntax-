import re
from datetime import datetime

def Hello_World():
    "this is a documentation"
    print("Hello World")
    print("Hello Python")
    return "Hello world"#мы можем возвращать комментарий????
# евм нужно сначала сделать условие с помощьб сравнения
x = Hello_World()
print(x)
Hello_World()
print("------------------------------------------------------------------------")

def Hello_World():
    "this is a documentation"
    return 123, 124

x = Hello_World()
print(type(x))
print(x)

def anotherFunc():
    Hello_World()#мы вызываем нащу первую функцию внутри второй
    Hello_World()
    Hello_World()

anotherFunc()
print("-------------------------------------------------------------------1-----")


def greet(name):
    return f"Hello {name}!"
greeting = greet("world")
print(greeting)
print("--------------------------------------------------------------------2----")

def printNames(name, surname, profession = "student"):
    return f"Your name is {name} and your surname is {surname}!, my profession is {profession}"#обязательно добавляеи сюда 
                          #все значения из printNames, чтобы мы могли вывксти именно их (name) (surname) и  (profession)
    
    #return "Your name is" + name + "and your surname is" + surname + "and my profession is " + profession +  "!"

x = printNames("Mee ", "Me-again")
print(x)
y = printNames("Rob", "Neer")
print(y)
z = printNames(name = "Me", surname= "And Me ", profession= "student")

print(z) 
print("----------------------------------------------------------------------3--")

# чтобы передать несколько значений иы ставим * в наименовании фенкции
#def fullname(*args):
#return f"{args[0]} {args[1]}!"
#friend = fullname("james", "brown")
#print(friend)

def addnumbers(num1,num2,num3):
    return num1+num2+num3
x = addnumbers(1,2,3)
print(x)

def addnumbers(*numbers):# packing into a list
    nums = 0#  иы определяем ums чтобы потом чтото делать с этим как в строке 64
    for x in numbers:
        nums += x
    return nums
    #return numbers[0]+numbers[1]+numbers[3]+numbers[4]+numbers[5]
x = addnumbers(1, 2, 3)
y = addnumbers(1,2,3,4,5,6)
z = addnumbers(44,2,55,4,66,2,3,54,78)
print(x)
print(y)
print(z)

print("----------------------------------------------------------------------4--")

#unpacking in general
#unpucking of function arguments i.e. unpucking collections

def multiplybytwo(args):
    return args * 2
mylist = [1,2,3,4,345, 34]# сколько (v)  у нас
#  есть столько значений мы и записываем
nm = multiplybytwo(mylist)
v1, v2, v3, v4, v5, v6 = mylist#чтобы сюжа можно было добавить mylist нужно 
 #добавить новую фенкцию multiplybytwo и выводим mylist дважды

print(nm)

def fullname(**kwards):
    return f"Success{kwards['name']}, surname: {kwards['lastname']}"
revival = fullname(name = "pfffff", lastname = "pfffffffffffffff")
print(revival)
print("---------------------------------------------------------------------5---")

 
x1,x2,x3 = ("Berlin","Paris", "London")
print(x1)
print(x2)
print(x3)

cities = ("Berlin","Paris", "London")
x1,x2,x3 = cities
print(x1)
print(x2)
print(x3)
print("---------------------------------------------------")
def display(listofcities):
    print(listofcities)
    
retval = display(cities)
print(retval)



def even_or_odd(number):
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"
  

def fullname(first, last):
      return f"{first}, {last}"
print(fullname(first = "james", last = "brown"))


friend = fullname("brown", "james")
print(friend)

print("---------------------------------------------------")


def getParity(number, parity):
    if parity == "odd":
        return number % 2 != 0
    elif parity == "even":
        return number % 2 == 0
    else:
        return "Parity indicated is unknown"
print("---------------------------------------------------")



a = '1_111'# мы исполюзуем нижний пробел для обозначения большого числа, в то время как float
#при исполнении игнорирукт нижний прочерк и ставит автоматически в свой тип данных сота то есть 111.0
print(float(a))
print("---------------------------------------------------")

list = [1,2,3,4,5,6,7,8,9]

print(list[::-1])

print("---------------------------------------------------")


def greet(name: str, date: datetime):
    
    hour = date.hour

    if hour < 12:
        greeting = "Good Morning"
    elif 12 < hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Night"

    return f"{greeting}, {name}!"
current_time = datetime.now()
name = "Roxy"
greeting_message = greet(name=name, date=current_time)
print(greeting_message)


print("---------------------------------------------------")


def print_user_profile(gender="female", first=None, last="Doe", pictures=[]):
    # Determine the default first name based on gender
    if first is None:
        if gender == "male":
            first = "John"
        else:
            first = "Jane"
    
    
    common_header_picture = "common_header.jpg"
    
    pictures_with_header = [picture] + pictures
    
    # Print the user profile information
    print(f"Name: {first} {last}")
    print("Pictures:")
    for picture in pictures_with_header:
        print(picture)

# Example usage:
print_user_profile(gender="male", last="Smith", pictures=["profile_pic1.jpg", "profile_pic2.jpg"])
#В этой функции мы сначала определяем имя по умолчанию на основе параметра gender.
# Затем мы создаем переменную common_header_picture и добавляем ее в список pictures_with_header, который включает в себя
# общую картинку заголовка вместе с предоставленными картинками.



print("---------------------------------------------------")


my_list1 = [1, 2, 3, 4, 5]
my_list2 = [4, 5, 6, 7, 8]
my_list3 = [9, 10, 11, 12]
sumAll = sum(my_list1)
print(sumAll)
sumAll1 = sum(my_list2)
print(sumAll1)

sumAll3 = sum(my_list3)
print(sumAll3)

print("---------------------------------------------------")


def greet(name: str, date : datetime):


   

    if 0 < date < 12:
        return f"Good morning, {name}"
    if  12 < date < 18:
        return f"Good day, {name}"
    else:
        return f"Good night, {name}"
myname = "roxy"
time = datetime.now().hour
a = greet(myname, time)
print(a)