class MoneyMachine:

  DENOMINATION = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01, 
  }

  def __init__(self):
    self.profit = 0;
    self.money_received = 0;

  def report(self):
    """
    Prints the total money made so far.
    """
    print(f"Money: ${self.profit}")

  def process_coins(self):
    """
    Requests the user to specify how many coins they want to pay with,
    and processes the value of those coins into dollars. 
    """
    for coin in DENOMINATION:
      self.money_received += int(input(f"How many {coin}? ")) * self.DENOMINATION[coin]

  def make_payment(self, cost):
    """
    Processes the payment made by the user. If it is greater than cost, the payments
    is successfully ptocessed, and profit is accounted for (price of item is the profit).
    """
    self.process_coins()
    if self.money_received >= cost:
      change = round(self.money_received - cost, 2)
      print(f"Here's your ${change} in change")
      self.profit += cost
      self.money_received = 0
      return True
    else:
      print("Sorry that's not enough money.")
      self.money_received = 0
      return False
      
