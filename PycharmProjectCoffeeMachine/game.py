from coffee_data import MENU, resources
from logos import logo1,logo2,logo3
from intro import intro
def is_ingredients(drink_ingredients,resources):
    for i in drink_ingredients:
        if drink_ingredients[i]>resources[i]:
            print(f"sorry! we cant make this item.")

    return True
def is_transaction():
    total=0
    total+=int(input("Enter the Quarter($0.25):"))*0.25
    total += int(input("Enter the Dims($0.10):")) * 0.10
    total += int(input("Enter the Nikel($0.05):")) * 0.05
    total += int(input("Enter the Penny($0.01):")) * 0.01
    return total
def transaction_suc(total,dc):

    if total>=dc:
        global profit
        change = 0
        change = round(total - dc, 2)
        profit += total - change
        print(f"change is ${change}")
        return True
    else:
        remaining=0
        remaining=round(dc-total,2)
        print(f"sorry!! you need ${remaining} to sip it")
        return False
def make_coffee(drink_name,order_ingrediants,name):
    for items in order_ingrediants:

        resources[items]-=order_ingrediants[items]
    if drink_name=="espresso":
       print(logo1)
       print(f"{name },your {drink_name} is ready")
    elif drink_name=="latte":
        print(logo2)
        print(f"{name},your {drink_name} is ready")
    else:
        print(logo3)
        print(f"{name},your {drink_name} is ready")
profit=0
game_on=True
while game_on:
    print(intro)
    name=input("Enter your name:").title()
    choice=input("Enter your choice :")
    if choice=="off":
        game_on=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink=MENU[choice]
        drink_ingredients=drink["ingredients"]
        if is_ingredients(drink_ingredients,resources):
            print("Pay the bill for the item: ")
            total =is_transaction()
            if transaction_suc(total,dc=drink["cost"]):
                make_coffee(choice,drink_ingredients,name)




