
mylist = [1,2,3, 'Me', 'Myself', {'name': 'Kelly','age': 21}]
mydict = {

    'name' : 'Me',
    'lastname' : 'Ford',
    'age': 28,
    'hascoffee' : False

}



users = [
    mydict,
    {
  
    'name' : 'Me', 
    'lastname' : 'Ford',
      'age': 28,
      'hasCoffee ' : False
    },
    {
  
    'name' : 'myself', 
    'lastname' : 'Just',
      'age': 20,
      'hasCoffee ' : True
    },
    {
  
    'name' : 'andi', 
    'lastname' : 'make',
      'age': 11,
      'hasCoffee ' : False
    },

]
print(users)
#print mylist
#for loop- looping through a list:
#print(i) output each dict
#for loop for list
for i in users:
 print(i)
#for loop- looping through a list:

for key,value in i.items():
  
  if key== 'age':
    if value <=18:
      
      print(f'u r:  {key} is {value}, u r not old enough')
    else:
    

     print('ure age, u can drink')




def funk1(list):
       print('funk1 fired', list)
       for user in list:
          age = user['age']
          name = user.get('name')
          print(age)
          if age<=18:
               print(f'{age}, u r too young to drink, u r {age}')

funk1(users)


def coffee(list):

    for user in list:
        name = user.get('name')
        hadCoffee = user.get('hasCoffee')
        if hadCoffee == True:
            print(f'{name} u`ve had coffee' )
        else:
            print(f'{name} no coffee')

coffee(users)


















#print(mylist[5])

#print(mylist[-1]['name']['age'])
#print(mydict)
#print(mydict['lastname'])


#for key, value in mydict.items():
 #print(value, key)