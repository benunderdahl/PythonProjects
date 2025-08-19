from faulthandler import is_enabled

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
is_on = True

while is_on:
    choice = input(f"What would you like to drink? {menu.get_items()} ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        selection = menu.find_drink(choice)
        if money_machine.make_payment(selection.cost) and coffee_maker.is_resource_sufficient(selection):
            coffee_maker.make_coffee(selection)