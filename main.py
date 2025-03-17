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
machine_running = True
total = 0
def coffee_making(coffee_type):

    #resource checking
    for ingredients,amt in MENU[coffee_type]["ingredients"].items():
        if resources[ingredients] < amt:
            return f"Sorry we don't have enough {ingredients}"

    #resource deduct
    for ingredients,amount in MENU[coffee_type]["ingredients"].items():
        resources[ingredients] -= amount

    return f"Here is your {coffee_type}! Enjoy!!"

def money(coffee_type):

    pennies = int(input("Pennies: "))
    nickel =  int(input("Nickels: "))
    dimes = int(input("Dimes: "))
    quarter = int(input("Quarters: "))
    global total
    total = (0.01*pennies)+(0.05*nickel)+(0.10*dimes)+(0.25*quarter)
    if total >= MENU[coffee_type]["cost"]:
        if total > MENU[coffee_type]["cost"]:
            change= total - MENU[coffee_type]["cost"]
            print(f"Here is your change ${round(change,2)}")
        return "Transaction Successful."
    else:
        return f"Not enough money, refunded amount ${round(total,2)}"

def coffee_machine():
    global machine_running
    while machine_running:
        coffee_type = input("What would you like to have? ")

        if coffee_type.lower() == "turn off":
            machine_running = False

        elif coffee_type.lower() == "report":
            print(resources)
        elif coffee_type not in MENU:
            print("Sorry, we don't have this!")
            pass
        else:
            print(money(coffee_type))
            if total < MENU[coffee_type]["cost"]:
                pass
            else:
                print(coffee_making(coffee_type))
        #done
coffee_machine()

