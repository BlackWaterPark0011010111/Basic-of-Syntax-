

mylist = ["dog", "cat", "mouse", "elephant"]
animal = "cat"
if  animal in mylist:
   print("My favorite animal is: ", animal)

   this_list = ["apple", "blackcurrant", "cherry", "pineapple"]
   this_list[1:3] = ["blackcurrant", "watermelon"]
   print(this_list)
   thislist = ["apple", "banana", "cherry"]
   thislist[1:2] = ["sraww"]
   print(thislist)

   thislist = [1,2,3,4,5,6]
   thislist.insert( 1 , "watermelon")
print(thislist)


animals = {
'Alligator': 1,
'Tiger': 6,
'Parrot': 2,
'Hamster': 5,
'Dolphin': 8

}
for name, count in animals.items():
   if name.endswith('r'):
      animals.pop(name)

print(animals)