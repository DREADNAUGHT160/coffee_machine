# importing station

from art import coffee_logo
import os
from time import sleep


def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: print report
def report(money_in):
    print(f"Water : {resources['water']}ml")
    print(f"Milk  : {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money : ${money_in}")


# TODO: TO CALCULATE THE CHANGE
def change(user_money, mrp_price):
    if user_money > mrp_price:
        change1 = user_money - mrp_price
        return change1
    else:
        return 0


# TODO: MONEY ACCEPTED
def money():
    print("Please insert coins.")
    quarters = float(input("how many quarters?: ")) * 0.25
    dimes = float(input("how many dimes? ")) * 0.10
    nickles = float(input("how many nickles? ")) * 0.05
    pennies = float(input("how many pennies? ")) * 0.01
    total_money = quarters + dimes + nickles + pennies
    return total_money


# TODO: cappuccino
def cappuccino(balance_def):
    resources["water"] -= 250
    resources["milk"] -= 100
    resources["coffee"] -= 24
    print(f"Here is ${round(balance_def, 2)} in change")
    print("Here is your cappuccino ☕ ENJOY !!!")


# TODO: espresso
def espresso(balance_def):
    resources["water"] -= 50
    resources["coffee"] -= 18
    print(f"Here is ${round(balance_def, 2)} in change")
    print("Here is your espresso ☕ ENJOY !!!")


# TODO: LATTE
def latte(balance_def):
    resources["water"] -= 200
    resources["milk"] -= 150
    resources["coffee"] -= 24
    print(f"Here is ${round(balance_def, 2)} in change")
    print("Here is your latte ☕ ENJOY !!!")


# TODO: CHECKING RESOURCES
def checking(water, coffee, milk):
    if water > resources["water"]:
        print("insufficient resource -water is low")
    elif coffee > resources["coffee"]:
        print("insufficient resource -coffee is low")
    elif milk > resources["milk"]:
        print("insufficient resource -milk is low")
    else:
        return True


# TODO: MAIN PROGRAM
print(coffee_logo)


def repeat():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100
    end = 0
    money_in = 0
    while end != 1:
        user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        if user_choice == "off":
            end == 1
            sleep(5)
            print("turing of ....................")
            screen_clear()
        elif user_choice == "report":
            report(money_in)
        elif user_choice == "cappuccino":
            money_main = money()
            if money_main < MENU["cappuccino"]["cost"]:
                print("insufficient fund. reorder")
            else:
                if checking(MENU["cappuccino"]["ingredients"]["water"], MENU["cappuccino"]["ingredients"]["coffee"],
                            MENU["cappuccino"]["ingredients"]["milk"]):
                    balance = change(user_money=money_main, mrp_price=MENU["cappuccino"]["cost"])
                    cappuccino(balance)
                    money_in += MENU["cappuccino"]["cost"]
        elif user_choice == "latte":
            money_main = money()
            if money_main < MENU["latte"]["cost"]:
                print("insufficient fund. reorder")
            else:
                if checking(MENU["latte"]["ingredients"]["water"], MENU["latte"]["ingredients"]["coffee"],
                            MENU["latte"]["ingredients"]["milk"]):
                    balance = change(user_money=money_main, mrp_price=MENU["latte"]["cost"])
                    latte(balance)
                    money_in += MENU["latte"]["cost"]
        elif user_choice == "espresso":
            money_main = money()
            if money_main < MENU["latte"]["cost"]:
                print("insufficient fund. reorder")
            else:
                if checking(MENU["espresso"]["ingredients"]["water"], MENU["espresso"]["ingredients"]["coffee"], 0):
                    balance = change(user_money=money_main, mrp_price=MENU["espresso"]["cost"])
                    espresso(balance)
                    money_in += MENU["espresso"]["cost"]
        else:
            print("refilling......................")
            repeat()


if input("do you want turn on the coffee machine? Y or N\n").lower() == "y":
    repeat()
else:
    print('invalid command')
