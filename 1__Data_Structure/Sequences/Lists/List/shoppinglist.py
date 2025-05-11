products = ["Pumpkin", "Watermelon", "Aloe", "Pomegranate", "Potatoes", "Carrot"]
call = ["1$","2$","3$","6.50$","2.50$","4.30$"]
amount = [1,2,3,4,5,6]
print(*zip(products,call,amount))