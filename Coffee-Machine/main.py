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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# process coins
def calculate_coins():
    """ this function helps you to calculate the total amount of money received """
    print("Please Enter coins: ")
    total = int(input("Enter the total Quarter coins")) * 0.25
    total += int(input("Enter the total Dime coins")) * 0.1
    total += int(input("Enter the total Nickle coins")) * 0.05
    total += int(input("Enter the total Penny coins")) * 0.01
    return total

transaction_successful= False

# check if transaction is successful?
def is_transaction_successful( total_money, cost ):
    """ this function helps you to determine if the transaction is successful """
    if total_money >= cost:
        change = total_money-cost
        print(f"Here is your change {change}")
        global profit
        profit += cost
        return True
    else :
        return False



def print_report():
    print(f" Water = {resources['water']}")
    print(f" Milk = {resources['milk']}")
    print(f" Coffee = {resources['coffee']}")
    print(f"Money: ${profit}")

def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is no enough {item}\n")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    global profit
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. \n ENJOY!")


#  this is the main function
machine_status= True
while machine_status:
    choice = input("What would you like to have ? (Espresso / Latte / Cappuccino) \n") . lower()
    if choice == "off":
        machine_status = False
    elif choice == "report":
        print_report()
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = calculate_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

