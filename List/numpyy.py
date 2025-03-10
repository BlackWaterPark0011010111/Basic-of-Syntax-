
new_list = list("This is my first list using a constructor")
print(new_list)

listoflist = [["Heading1","Heading2","Heading3"], 
               [1,2,3],
               [True, False, True]]
print(listoflist[0])
print(listoflist[1][-2])#вывести часть листа, 
#позицию мы указываем [-2],сразу после того
                       #как указали номер списка


print(listoflist[1:2][0:2])
print(listoflist[0:3][0:2])# выводим первые два списка
#выводим первый список по индексу с 0 до  и второй с нуля
#  по 2й индекс

list1 = ["Guitars", "Drums", "Basses", "Trumpets"]
print(list1[-1])
print(list1[-2:])# возвращает другой лист, подлист с -2-го значения
#  до последнего
# ¨:¨ - всегда возвращает лист
print(list1[::-1])# реверс листа, обратно противополодный лист
print(list1[::])#  просто выводим лист
print(list1[::2])
print(list1[:2])# вы водим все что в списке до второго индекса
#print(list1.index("Basses", 3)) тут ошибка, почему
print(list1.reverse())
print(list1)
list1.sort()
print("The effect of sort method of list: ", list1)
list1.sort(reverse=True)
print("Descanding sort using sort(reverse true) method: ",list1)

list2 = [123,456,789]
list2[0:2] = [444,333]
print(list2)


list3 = [123,456,789]
list3[2] = [444,333]
print(list3)


list4 = [123,456,789]
list4[0:2] = [444]
print(list4)

list5 = [123,456,789]
list5[2] = [444]
print(list5)



# разделение строки с помощью Split  метода
ourstring = "Lets use a split method again"
print(ourstring.split(" "))




list8 = [

    ["Heading1","Heading2","Heading3","Heading4"],
    [123,456,789,888],
    [333,444,555,444]
]
#print(list8[0:2])
print(list8)
print(list8[2][2])# покажет 555

#numpy array что это

import numpy 
import numpy as np


my_list = numpy.array(list8)
print(my_list)
#работает с одинаковым колличсетвом набора символов в листе, у нас
#4 headings, и такое же колличество должно быть и в друнрм подчисте



my_list = my_list[:,0:2]
my_list = my_list[0:3,0:2]# first rows then columns
print(my_list)

print("---------------------------------------------------10--")





list = ["Yogurt","Potatoes", "Cucumbers","Onion", "Beers"]
print(list)
list.append("Soda")
print(list[2:])
print("---------------------------------------------------15---")


liist = ["wine", "vodka"]
liiist = liist + list
print(liiist)
list.insert(0, "Apples") # добавляем Apples на 1-е место
print(list)



# list.pop(0)# .pop(и внутри индекс), удаляет первое название, у нас яблоки
# print(list)
print("---------------------------------------------------1---")

vegies = ["Yogurt","Potatoes", "Cucumbers","Onion", "Beers"]
vegies1 =["Yogurt","Potatoes", "Cucumbers","Onion", "Beers"]   
print(vegies==vegies1)



print("---------------------------------------------------1---")

if vegies==vegies1:
    print("Two lists are identical in content elements")
else:
    print("Two lists are not identical in content or position of elements")
    print(vegies is vegies1)



if vegies is vegies1:
    print("Эти списки ссылаются на один и тот же адрес в памяти: ", id(vegies))
else:
    print("Оба списка ссылаются на разные адреса в памяти: ",id(vegies),id(vegies1))
print("---------------------------------------------------1---")

print(vegies==vegies1.reverse())
print(vegies)
print(vegies1)
print(id(vegies))# смотрим id
print(id(vegies1)) # смотрим id

# посмотреть лист в w3schools
# sorting,key ,comprehension,list methods
# numpy

# unpuck tuples