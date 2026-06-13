from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
menu= Menu()
coffee_maker = CoffeeMaker()

is_activated = True
while is_activated:
    options = menu.get_items()
    choice = input(f"What would you like to have ? ({options}) \n") . lower()
    if choice == "off":
        is_activated = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        print(coffee_maker.is_resource_sufficient(drink))
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)