


def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def divide(n1, n2):
  return n1 / n2

def multiply(n1, n2):
  return n1 * n2

num1 = int(input("What's the first num? "))
num2 = int(input("What's the second num? "))

operations = {
  "*": multiply,
  "+": add,
  "-": subtract,
  "/": divide
}

for symbol in operations:
  print(symbol)

operation_symbol = input("What operation would you like to carry out? ")


function = operations[operation_symbol]
result = function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {result}")
