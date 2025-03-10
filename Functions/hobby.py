hobby1 = input('Please specify ure favorite hobby')
hobby2 = input('Please specify ure second favorite hobby')
hobby3 = input('Please specify ure 3rd favorite hobby')
holidays = input('Enter ure holidays')
print(hobby1)
print(hobby2)
print(hobby3)
print(holidays)
def manageHobbies(hobby1,hobby2, hobby3): 
    costofhobbies = 300 
    displaySeparators()
    print('My favorite hobby is: ', hobby1)
    print('My second favorite hobby is: ', hobby2)
    print('My third favorite hobby is:' , hobby3)
    print( 'i spend' + holidays + 'days doing my hobby')


    cost = int(holidays) * int(costofhobbies)
    print('the cost is' , cost)
def displaySeparators():
     print("***********************************")

displaySeparators()


costofhobbies = manageHobbies(hobby1, hobby2, hobby3)
print(type(costofhobbies))
print('The cost of my holidays last year was', str(holidays) + str(costofhobbies))


displaySeparators()