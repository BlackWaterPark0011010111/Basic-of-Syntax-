
products = ["Pumpkin", "Watermelon", "Aloe", "Pomegranate", "Potatoes", "Carrot"]
call = ["1$","2$","3$","6.50$","2.50$","4.30$"]
amount = [1,2,3,4,5,6]
print(*zip(products,call,amount))

print("binary numbers starting with 0b1...")
print(0b01)
print(0b11)
print(0b10)
print(0b111)
print(0b10100)
print(0b00101)
print(0b00001000)
print(0b00001100)
print(0xfff)
print(0x1)
print(bin(1000))
print("using int function")
print(int("1000001", 16))
print(int("FFFFFFFF", 16))
print(0b00000000000000000000000000000000000000000000000)

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b: 
  print("hiii")
else:
  print("a greater than b")
n = 10

a = 1.5
if a ==True:
       print("тлалтвлоатмвмш")
       a = bool("string")
       if a == True:
          print("A is a True ")


#for loop with a range function
print(range(10,20,2))

for x in range(10):
 for x in range(0,10,2):

  print(x)

list1 = ["First", "Second", "Third", "Fourth", "fifth"]
list2 = [1,2,3,4,5,6,7]
for x in list1:
   if x =="Fourth":
 
     continue
   print(x)
   for y in list2:
      print(y)

else:
   print("The loop has finished...")


#x = 10
#while x >= 0:
   #print(x)
  # x+= 1 # why does it ended on 7  и что значит -=1
#for y in range(10):
  # print(x + y)
  # x -= 1
   print("**************************1***********************************")

x = 27
print(bin(x))

print("******************************2********************************")

bin = 11011
print(int(x))

print("******************************3********************************")

i = 27
h = hex(i)
print(h)

print("*******************************4*******************************")

i = 0x1b
h = int(i)
print(h)

print("*******************************5*******************************")

i = 0b11011
h= hex(i)
print(h)

print("*******************************6*******************************")

x = 0b11011
i = int(x)
print(i)
print("*******************************7*******************************")

i = 27
y = oct(27)
print(y)

print("*******************************7*******************************")


i = oct(27)
y = int(27)
print(y)
print("******************************8*******************************")


x = input("Enter a number")
x = int(x)
print(type (x))
if x % 2==0:
   
   print("Even number")
else:
   
   print("Odd number")








   
mydict = {"name": "jordan", "surname": "stanley", "prof": "guitarist"}
for x in mydict:
   print(x)
   print(mydict[x])
   
   print("thank u")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
answer = input("Enter  your month: ")
if answer in months:#если условие после if не True, то все что с отступом выполняться не будет
     if answer in ["January", "March",  "May", "July", "August", "October", "December"]:
     
      print("Ure month is: " + answer + " and it has" + str(31) + " days")
       

     if answer not in ["January", "March",  "May", "July", "August", "October", "December"] and answer != "February": 
    
      print("Ure month is: " + answer + " and it has" + str(30) + " days")
       
     if answer == "February":
        print("Ure month is: " + answer + " and it has " + str(28) + " days")
else:
      
      print("GOFUCKYOURSELF")
   

   