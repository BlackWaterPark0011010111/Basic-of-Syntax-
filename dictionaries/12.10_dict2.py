dict = {}
print(type(dict))

dict = {
    'name':'Paul',
        'surname':'Polansky'
        }
print(dict)


students = {
    'student1' : 'Anna',
    'student2' : 'Paul',
    'student3': 'Daniel',
    'student4' : 'Sami'
  
}

print(students['student1'][0][3]) # выводим букву 'a'- последнюю буквк в слове Anna, [3]- 
# это ее индекс
print(students['student1'])#чтобы вывксти определенного студента
#по ключу
#открываем внетри квадратные скобки и он покажет нам что включает
# # нам student1
print(students['student1'][0]) # 0 мы ставим если в Anna выглядел 
#бы как лист, например
'student1' : [ 'Anna','Berlin' ]
'student1' : [ 'Anna','Berlin', {'k':'v', 'm':'s'} ]
#ксли нам нужно досткчатся др K V M s до словаря внетри словаряб
# # мы указываем
print(students['student1'][0][2]['m']) # 2 значит индекс словар

#внетри словаря который равен "2", 
#и потом указыванм то что там нам нудно найти

students = {
    'student1' : ['Anna','Berlin',{'key':'value','m':'s'}],
    'student2' : 'Paul',
    'student3': 'Daniel',
    'student4' : 'Sami'
  
}
print(students['student1'][0][2]['m'])





students = {
    'student1' : 'Anna',
    'student2' : 'Paul',
    'student3': 'Daniel',
    'student4' : 'Sam',
    'Language' : ['python', 'Java', 'c#'] 
}

print(students['Language'][0])



students = {
    'student1' : 'Anna',
    'student2' : 'Paul',
    'student3': 'Daniel',
    'student4' : 'Sam',
    'Language' : ['python', 'Java', 'c#'] ,
    'drinks' :{ 
            'coffee': 'coffee latte',
            'beer': 'pilsner',
            'wine': 'New zeeland'      
    } 
}
print(students['drinks']['wine'])


dict2 =dict(['one', 'two'])
dict2 = dict(list1) # нельзя вот так вставить лист


#сначала 
dict = {}
dict2 = dict.fromkeys('name', 'surname', 'profession')
print(dict2)


#adding new elements to dict
fruits = { 
'red' : [ 'apple', 'cherry', 'strawberry'],
'orange': ['orange', 'mango', 'peach'],
'yellow' : ['banana', 'lemon']
}


#looping over lists as values
for key, value in fruits.items():# выводит все values  
    for x in value:
        print(x)




for k, v in fruits.items():
    print(k, v)



for  value in fruits.items():
    print( value[0])# выводит apple, orange, banana



for  value in fruits.items():
    print( value[:]) # выводит все 



for  value in fruits.items():
    print( value[-1]) #выводит strawbery, peach, lemon

fruits['green'] = 'watermelon'#добавляем
print(fruits)

fruits['green'] = ['watermelon']
print(fruits)
fruits.update({'green': ['cherryes', 'cherries2']})
fruits.pop('yellow')
print(fruits)


dict3 = {
'name1' : 'Anna',
'name2': 'Paul',
'name3' : 'Sami'


}
#looping over dicts
for x in dict3:
    print(x, y)

#the same effect with dict.item() method
for x in dict3.items():
    print(x, y)


for key in dict3: # выводит асе значения ключей, то есть Anna. Paul. Sami
    print(dict3[key])

    
for key in dict3: # выводит 
    print(key, dict3[key])


for key, value in dict3: # выводит асе значения и значений и  ключей 
    print(key, value)

 #simpler result
for value in dict3.values():
    print(value)


for key in dict3.values():
    print(key)

for v in dict3.values():
    print(v)
        
for k in dict3.values():
    print(k) 

