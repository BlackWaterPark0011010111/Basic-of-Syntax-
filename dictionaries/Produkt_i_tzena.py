shopping_list =[
    {
 "products": "potato",
 "number" :1, 
 "price" :"2$"
 }, 
 {
  "products": "tomato",
  "number" :1, 
  "price" :"3$"
 },
                        
{
   "products": "pomegranate",
   "number" : 3,
   "price" : "4$"
 },

{                    
   "products" : "pumpkin",
   "number" : 7, 
   "price" : 6,

 },
 {
     "products" : "vanilla",
     "number" : 2,
     "price" : "6$",
 }
]

add_list = [
    {
        "products": "carrot",
          "number" :5, 
          "price" :"2.5$"
          },
            {
                "products": "onion",
                "number" :3, 
                "price" :"3.9$"
                }, ]

shopping_list.extend(add_list)


shopping_list.pop(1)
shopping_list[1]["number"] = 3

print(shopping_list)


 #Array a collection of elements 
#identified by index or key useful for quiqly 
#looking up values based on  a shared index or key
array = ["a", "b", "c", "d"]
print(array[0])

car="ford"
color= "blue"
year= 1967
  
my_car={
  "car": "ford",
  "car_color" : "blue",
   "roof_color": "red",
   "year": 1967

}

#Mapping tipe
# sequence types
#lists
my_car_list=["ford", "blue", "red", 1967]

my_list=[car, color, year, 1232, my_car]
#tuples
tuple(1,2,3,"blue")


#set types

my_set= {1,2,3,4}

my_frozenset= frozenset({1,2,3,4,5,6})
#special Data Types
#files
#functions
#classes