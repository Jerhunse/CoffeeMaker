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

# Calculate customers payment
def process_coin():
    print("Please insert coins")
    quater = input("How Many Quarter: ")
    dime = input("How Many Dime: ")
    nickle = input("How Many Nickle: ")
    penny = input("How Many Penny: ")

    total = (float(quater) * .25) + \
            (float(dime) * .10) + \
            (float(nickle) * .05) + \
            (float(penny) * .01)
    return total


# Promp user for what they want to drink
def pick_a_coffee(drink, pay):
    refund = 0
    if drink == "espresso".lower():
        price = MENU["espresso"]["cost"]
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]

        if pay < price:
            print("Sorry You dont have enough money")
        else:
            refund = pay - price
            print(f"Enjoy your espresso! Your refund is $ {refund}")
            resources["water"] -= water
            resources["coffee"] -= coffee

    elif drink == "latte".lower():
        price = MENU["latte"]["cost"]
        water = MENU["latte"]["ingredients"]["water"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        milk = MENU["latte"]["ingredients"]["milk"]

        if pay < price:
            print("Sorry You dont have enough money")
        else:
            refund = pay - price
            print(f"Enjoy your espresso! Your refund is $ {refund}")
            resources["water"] -= water
            resources["coffee"] -= coffee
            resources["milk"] -= milk

    elif drink == "cappuccino".lower():
        price = MENU["cappuccino"]["cost"]
        water = MENU["cappuccino"]["ingredients"]["water"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]

        if pay < price:
            print("Sorry You dont have enough money")
        else:
            refund = pay - price
            print(f"Enjoy your espresso! Your refund is $ {refund}")
            resources["water"] -= water
            resources["coffee"] -= coffee
            resources["milk"] -= milk








# Keep asking the user for coffee
ask_again = True

while ask_again == True:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    process_coin()

# Report to show how much supplies are left
def report():
    current_report = {}
    return 0


