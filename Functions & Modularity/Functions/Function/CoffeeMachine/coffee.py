class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.money = money
        self.coffee_recipes = {
            "espresso": {"water": 50, "milk": 0, "coffee_beans": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee_beans": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee_beans": 24, "cost": 3.0},
            "americano": {"water": 150, "milk": 0, "coffee_beans": 18, "cost": 2.0},
            "macchiato": {"water": 100, "milk": 50, "coffee_beans": 20, "cost": 2.7}
        }

    def get_report(self):
        print(f"Water: {self.water} ml")
        print(f"Milk: {self.milk} ml")
        print(f"Coffee beans: {self.coffee_beans} g")
        print(f"Money: ${self.money}")

    def turn_off(self):
        print("Turning off the coffee machine...")
        exit()

    def check_resources(self, water_needed, milk_needed, beans_needed):
        if self.water < water_needed:
            print("Sorry, not enough water!")
            return False
        if self.milk < milk_needed:
            print("Sorry, not enough milk!")
            return False
        if self.coffee_beans < beans_needed:
            print("Sorry, not enough coffee beans!")
            return False
        return True

    def make_coffee(self, coffee_type):
        if coffee_type in self.coffee_recipes:
            recipe = self.coffee_recipes[coffee_type]
            if self.check_resources(recipe["water"], recipe["milk"], recipe["coffee_beans"]):
                if self.check_transaction(recipe["cost"]):
                    self.serve_coffee(coffee_type, recipe)
        else:
            print("Invalid coffee type.")

    def insert_coins(self):
        print("Please insert coins.")
        total = float(input("Enter the total amount in dollars: $"))
        return total

    def check_transaction(self, cost):
        money_received = self.insert_coins()
        if money_received >= cost:
            change = round(money_received - cost, 2)
            if change > 0:
                print(f"Here is your change: ${change}")
            self.money += cost
            return True
        else:
            print("Sorry, not enough money. Money refunded.")
            return False

    def serve_coffee(self, coffee_type, recipe):
        self.water -= recipe["water"]
        self.milk -= recipe["milk"]
        self.coffee_beans -= recipe["coffee_beans"]
        print(f"Here is your {coffee_type}. Enjoy!")

    def check_resource_alert(self):
        if self.water < 50:
            print("Warning: Low water level!")
        if self.milk < 50:
            print("Warning: Low milk level!")
        if self.coffee_beans < 18:
            print("Warning: Low coffee beans level!")

def main():
    coffee_machine = CoffeeMachine(water=1000, milk=500, coffee_beans=200, money=0)

    while True:
        coffee_machine.check_resource_alert()
        action = input("What would you like?\n1. Espresso\n2. Latte\n3. Cappuccino\n4. Americano\n5. Macchiato\n6. Report\n7. Off\n\nChoose an option: ").strip()
        if action == "7" or action.lower() == "off":
            coffee_machine.turn_off()
        elif action == "6" or action.lower() == "report":
            coffee_machine.get_report()
        elif action == "1" or action.lower() == "espresso":
            coffee_machine.make_coffee("espresso")
        elif action == "2" or action.lower() == "latte":
            coffee_machine.make_coffee("latte")
        elif action == "3" or action.lower() == "cappuccino":
            coffee_machine.make_coffee("cappuccino")
        elif action == "4" or action.lower() == "americano":
            coffee_machine.make_coffee("americano")
        elif action == "5" or action.lower() == "macchiato":
            coffee_machine.make_coffee("macchiato")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
