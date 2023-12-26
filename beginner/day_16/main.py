from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


start = True

menu = Menu()
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()

while start:

  choice = input(f'What would you like? ({menu.get_items()}): ').lower()
  drink = menu.find_drink(choice)
  can_make = coffee_machine.check_stock(drink)
  if drink and can_make:
    money_machine.process_coins(drink)
    if money_machine.make_payment(drink['cost']): 
      coffee_machine.make_drink(drink)
  elif choice == 'report':
    coffee_machine.report()
    money_machine == 'report'

