hobby1 = input("Please specify your favourite hobby!")
hobby2= input("Please specify your second favourite hobby!")
hobby3= input("Please specify your third favourite hobby!")
holidays = input("Please specify the number of days used for your hobbies last year...")

print(hobby1)
print(hobby2)
print(hobby3)
print(holidays)

def displaySeparators():
    print("***********************************")

def manageHobbies(hobby1, hobby2, hobby3, holidays):
    costOfHolidaysPerDay = 300
    displaySeparators()
    print("My favourite hobby is: ", hobby1)
    print("My second favourite hobby is: ", hobby2)
    print("My third favourite hobby is: ", hobby3)
    print("I spent " + holidays + " days doing my hobby last year...")
    cost = int(holidays) * int(costOfHolidaysPerDay)
    print("The cost of my hobby last year was ", cost)
    displaySeparators()
    return cost

costOfHobbies = manageHobbies(hobby1, hobby2, hobby3, holidays)
print(type(costOfHobbies))
print("The cost of my hobby last year was: " + str(costOfHobbies) + " and this year the cost might be: " + str(costOfHobbies*1.2))
