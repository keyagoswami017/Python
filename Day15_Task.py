from Day15_MenuData import *

money = 0.0
# What would you like? (espresso/latte/cappuccino):
# Turn off the machine by typing "off"
# Report Format
#   Water: 100ml
#   Milk: 50 ml
#   Coffee: 76g
#   Money: $2.5

# Coffee Machine
#  TODO:  1. Print Report
def coffee_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

#  TODO:  2. Check resources sufficient?
def coffee_match(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry,there is not enough {item}")
            return False
    return True

#  TODO:  3. Process Coins ($0.25 - quater, $0.10 - dime, $0.05 - nickles, $0.01 - pennies)
def process_coins():
    print("Please insert coins.")
    quarters = float(input("How many quarters?:"))
    dimes = float(input("How many dimes?:"))
    nickles = float(input("How many nickles?:"))
    pennies = float(input("How many pennies?:"))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total

#  TODO:  4. Check Transactions Successful?
def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry,there is not enough money")
        return False

#  TODO:  5. Make Cofee
def complete_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")

def coffee_select(select):
    if select == "espresso" or select == "latte" or select == "cappuccino":
        if coffee_match(MENU[select]["ingredients"]):
            total = process_coins()
            if is_transaction_successful(total, MENU[select]["cost"]):
                complete_coffee(select,MENU[select]["ingredients"])
    elif select == "report":
       coffee_report()
    else:
        print("Wrong Choice!!!")

def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino):")
        if choice == "off":
            is_on = False
        else:
            coffee_select(choice)


coffee_machine()