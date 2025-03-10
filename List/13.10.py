
import pprint

students = {
    'student1' : ['Anna', 'Berlin', {'k':'v','m':'s'}],
    'student2' : 'Paul',
    'student3': 'Daniel',
    'student4' : 'Sami',
    'drinks':{
            'coffee': 'caffee lattee',
            'beer': 'pilsner',
            'wine': 'New zeeland'
    }  
}
print(students['drinks']['wine'])

print(students['student1'][0])
print('-------------------------------------------')
print(students['student1'][2]['m'])
 
students = {
'student1': 'Anna',
'student2': 'peet',
'student3': 'Kole',
'student4' : 'Sami',
'Language': ['Python', 'c#', 'Java']

}

print(students['student4'])
print(students['Language'])

fruits = {
    'red' : ['cherry' , 'apple' , 'strawberry'],
    'orange' : ['orange', 'mango', 'peach'],
    'yellow' : ['banana', 'lemon']
    }
for key, value in fruits.items():
    for x in value:
        print(x)
print('----------------------------------------2---')

for k, v in fruits.items():
    print(k, v)
    print('--------------------------------------3-----')


for value in fruits.items():
    print(value[0])
    print('--------------------------------------3-----')

for k, v in fruits.items():
    print(k, v)



for  value in fruits.items():
    print( value[0])# выводит apple, orange, banana



for  value in fruits.items():
    print( value[:]) # выводит все 



fruits['green'] = 'watermelon'
print(fruits)
fruits.update({'green': ['cherryes', 'cherries2']})
fruits.pop('yellow')
print(fruits)



# stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
# stuff.insert(0, stuff[:])
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(stuff)
# [   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
#     'spam',
#     'eggs',
#     'lumberjack',
#     'knights',
#     'ni']
# pp = pprint.PrettyPrinter(width=41, compact=True)
# pp.pprint(stuff)
# [['spam', 'eggs', 'lumberjack',
#   'knights', 'ni'],
#  'spam', 'eggs', 'lumberjack', 'knights',
#  'ni']
# tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
# ('parrot', ('fresh fruit',))))))))
# pp = pprint.PrettyPrinter(depth=6)
# pp.pprint(tup)
print('=====================================================')
data = {
    'student': #это список словарей
            [
        {
        'name': 'Josephine',
        'subject':
        [
            {
            'name': 'English',
            'teacher': 'Mr. Hoover'

        }
    ]
    },
    {
        'name': 'Luke',
        'subject': [
           {
               'name': 'History',
               'teacher': 'Mr. Peters'
           } 
        ]
    },
    {
        'name': 'Julia',
        'subject': [
            {
            'name': 'Chemistry',
            'teacher': 'Mrs. Fauci'
                }
            ]
        }
    ]
}
print(data)
print(data["student"][2]['subject'][0]['teacher'])

print(data.get('student'))
print(data.setdefault('anything', "{'key':'value'}"))#return value #or writes a default key-value

print(data)


def get(data, query):
     keys = query.split(".")
     print(keys)
     key1, key2, key3, key4, key5 = keys #unpacking variables from a list
     print(data[key1][int(key2)][key3][int(key4)][key5])

get(data, 'student.0.subject.0.teacher')
get(data, 'student.1.subject.0.name')
get(data, 'student.2.subject.0.name')

dict1 = {'a': 1, 'b': 2}

dict2 = {'b': 2, 'a': 1}
print('The dict1 and dict2 are have the samecontents: ', dict1==dict2)
print('The dict1 and dict2 are the same : ', dict1 is dict2)

dict3 = {'new key': 'new value', 'a' : 110}
# merging of two dictionaries using the update() method
dict1.update(dict3)
print('Merge dict1 and dict3: ', dict1)
print('-----------------------------------------------------')

##########HW
dict1 = {
  'a': 4,
  'b': 16,
  'c': 3
}

dict2 = {
  'a': 8,
  'b': 2,
  'c': 3
}

result = sum(dict1[key] * dict2[key] for key in dict1)

print("Sum of products:", result)
print('-----------------------------------------------------')


def convert_keys_to_lower_case(input_dict):
    return {key.lower(): value for key, value in input_dict.items()}

natural_case = {
  'Company name': 'Digital Career Institute',
  'Street': 'Vulkanstraße',
  'House Number': 1,
  'City': 'Berlin'
}

result = convert_keys_to_lower_case(natural_case)
print(result)
print('-----------------------------------------------------')
color_names = ['red', 'green', 'blue']
color_hex = ['#FF0000', '#00FF00', '#0000FF']

ziplist = zip(color_names, color_hex)
pt = list(ziplist)
print(pt)
print('------------------------------------------------22-----')

week = [ 'monday','tuesday','wednesday','thursday', 'friday']
print(week.index('tuesday'))#индекс tuesday
print(week[2])#индекс wednesday
print(week.count('monday'))
#посчитать сколько понедельников в списке
print(week)


week.pop([ 'monday'])
print(week)
print('------------------------------------------------23-----')
