
class CoffeeMaker:

  UNITS = {
    'water': 'ml',
    'milk': 'ml',
    'coffee': 'g'
  }

  def __init__(self):
    self.ingredients = {
      'water': 300,
      'milk': 200,
      'coffee': 100
    }
    
  def report(self):
    for ingredient in self.ingredients:
      print(f"{ingredient}: {self.ingredients[ingredient]}{self.UNITS[ingredient]}")

  def check_stock(self, choice):
    can_make = True
    for item in choice.ingredients:
      if choice.ingredients[item] > self.ingredients[item]:
        print(f"Sorry there is not enough {item}.")
        can_make = False

    return can_make

  def make_drink(self, choice):
    print(f"Here is your {choice.name}.")
    for item in self.ingredients:
      self.ingredients[item] -= choice.ingredients[item]
  
