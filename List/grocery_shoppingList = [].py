grocery_shoppingList = []
prices = []
total = 0

while True:
    food = input("Please enter a food to buy(q to quit): ")
    if food.lower() =="q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        grocery_shoppingList.append(food)
        prices.append(price)
        print("======WELCOME TO WALMART====")
        for food in grocery_shoppingList:
            print(food, end=" ")
            for price in prices:
                total+=price
                print()
                print(f"your total is :${total}")