## Coffee Machine - made using OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():

    # This is the menu
    menu = Menu()
    cm = CoffeeMaker()
    mm = MoneyMachine()

    while True:
        drinks = menu.get_items()
        choice = input(f"What drink would you like? We serve {drinks} ")
        if choice == "off":
            print("Coffee machine turning off...")
            return
        elif choice == "report":
            cm.report()
            mm.report()
            continue
        else:
            # Check user selected a valid drink
            drink = menu.find_drink(choice)
            if drink == 'e': # error catcher
                continue
            if cm.is_resource_sufficient(drink):
                if mm.make_payment(drink.cost):
                    cm.make_coffee(drink)
                else:
                    continue
            else:
                continue




if __name__ == '__main__':
    main()
