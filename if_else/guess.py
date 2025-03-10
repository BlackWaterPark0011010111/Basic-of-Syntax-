'''mynumber = 6
 # бесконечный цикл while
while True:
    a = input('Please guess a number between 1 and 10  ') # выводится только значения  типа "строка" и чтобы вывести число нужно поставить int
    if int(a) == mynumber:
        print('u r guess that')
   
        break# остановить цикл 

    print('u r wrong, try again')
print('The end of the loop') 
'''

print('++++++++++++++++++++++++++++++++++++++++++++++++++')


a = float(input('Enter first one: '))
b= float(input('Enter the second one: '))


if a > b:
    print('u`re result is: ',  (a-b)*2)

else:
    print('u`re result is: ', abs(a-b) )

print('++++++++++++++++++++++++++++++++++++++++++++++++++')
