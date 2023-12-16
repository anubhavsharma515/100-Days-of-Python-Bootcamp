import random

report = {
  'Water': 300,
  'Milk': 200,
  'Coffee': 100,
  'Cost': 0
}

units = {
  'Water': 'ml',
  'Milk': 'ml',
  'Coffee': 'g',
  'Cost': '$',
}

wallet = {
  'Quarters': 0,
  'Dimes': 0,
  'Nickles': 0,
  'Pennies': 0,
}

def update_wallet():
  for denomination in wallet.keys():
    wallet['Quarters'] = int(input(f"How many {denomination}? "))

def set_item(water=0, milk=0, coffee=0, cost=0):
  item = {}
  item['Water'] = water
  item['Milk'] = milk
  item['Coffee'] = coffee
  item['Cost'] = cost
  return item

def print_report():
  for item in report.keys():
    print(f"{item}: {report[item]}{units[item]}")

def update_stock(choice):
  for item in report.keys():
    change = 1
    if item != 'Cost':
      change = -1
    report[item] += (change * choice[item])

def sufficient_funds(cost):
  deposit = 0.25 * wallet['Quarters'] + 0.1 * wallet['Dimes'] + 0.05 * wallet['Nickles'] + 0.01 * wallet['Pennies']
  if deposit >= cost:
    return True

  return False

def check_stock(choice):
  for ingredient in report.keys():
    if choice[ingredient] > report[ingredient] and ingredient != 'Cost':
      return False

  return True

latte = set_item(water=200, milk=150, coffee=24, cost=2.5)
espresso = set_item(water=50, coffee=18, cost=1.5)
cappuccino = set_item(water=250, milk=100, coffee=24, cost=3.0)

menu = {'Latte': latte, 'Espresso': espresso, 'Cappuccino': cappuccino}

shop = True

while shop: 
  choice = input("What would you like?  ").capitalize()
  if choice == 'Report':
    print_report()
  elif choice == 'Done':
    shop = False
  else:
    if check_stock(menu[choice.capitalize()]):
      update_wallet()
      if sufficient_funds(menu[choice]['Cost']):
        update_stock(menu[choice])
        print(f"Here is your {choice}, enjoy!")
      else:
        print("Not enough funds")
    else:
      print("Sorry, not enough in stock")

