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

list= [
    {
        "products": "carrot",
        "number" :5, 
        "price" :"2.5$"
    },

    {
        "products": "onion",
        "number" :3, 
        "price" :"3.9$"
    } ]

shopping_list.extend(list)


shopping_list.pop(1)
shopping_list[3]["number"] = 3

print(shopping_list)


print("-----------------------------------------2---")

def get_score(name):
    #  приводим имя к нижнему регистру для сравнения с ключами в словаре
        # Converting the name to lowercase for comparison with dictionary keys

    name_lower = name.lower()
    
    
    if name in participants:
        # Если участник найден, выводим его результат
        # If the participant is not found in the list
        print(f'{name} scored {scores[name_lower]} points')
    else:
       
        print(f'{name} did not participate')

# Данные
participants = ['Brian', 'Britney', 'Ben']
scores = {
    'brian': 25,
    'britney': 80,
    'ben': 50
}


get_score('Paul') 
get_score('Britney') 
