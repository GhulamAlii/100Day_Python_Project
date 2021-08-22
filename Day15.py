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


# def order():
#     user_order = input("what would you like to drink\n a: espresso \n b: latte \n c: cappuccino \n Press the button to process")
#     if user_order == "a":
#         return "espresso"
#     elif user_order == "b":
#         return "latte"
#     elif user_order == "c":
#         return "cappuccino"
#
# def resourse_check():
#
#     drink = order()
#     report = input("Would like to see our resourse Report If yes Type \"R\"\n")

def resources_check(order_resourse):
    for item in order_resourse:
        if item >= order_resourse[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def Transaction():
    print("Please Insert THe Coin")
    total = input("enter The amount of Coin")
    return total
is_on = True


while is_on:
    user_order = input("what would you like to drink"
                       "\n a: espresso \n b: latte \n c: cappuccino \n"
                       "Press the button to process \n")
    if user_order == "off":
        is_on = False

    elif user_order == "r":
        for resources, value in resources.items():
            print(f"{resources} : {value}")

    else:
        drink = MENU[user_order]
        if resources_check(drink["ingredients"]):
            amount = Transaction()
            if amount >= drink["cost"]:
                profit =+ drink["cost"]
                if amount > drink["cost"]:
                    change = amount - drink["cost"]
                    print(f"here your change{change}")
            else:

