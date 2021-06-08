from coffeeInfo import MENU
from coffeeInfo import resources


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

    elif drink == "report".lower():
        return resources

# check resources
def check_resources():
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]

    if current_coffee <= 0:
        print("Sorry we are out of resources to make that")
    elif current_milk <= 0:
        print("Sorry we are out of resources to make that")
    elif current_water <= 0:
        print("Sorry we are out of resources to make that")

# Keep asking the user for coffee
ask_again = True

while ask_again:

    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee == "latte".lower():
        check_resources()
        pay = process_coin()
        pick_a_coffee(coffee, pay)
    elif coffee == "espresso".lower():
        check_resources()
        pay = process_coin()
        pick_a_coffee(coffee, pay)
    elif coffee == "cappuccino".lower():
        check_resources()
        pay = process_coin()
        pick_a_coffee(coffee, pay)
    elif coffee == "off":
        ask_again = False
    elif coffee == "report".lower():
        current_resources = resources
        print(current_resources)
    else:
        print("Invalid Entry")
