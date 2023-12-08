import math

def paint_calc(height, width, coverage):
  paint_cans = math.ceil(((height * width) / coverage))
  print(f"You'll need {paint_cans} cans.")

test_h = int(input("Enter Height: "))
test_w = int(input("Enter Width: "))
coverage = 5

paint_calc(height=test_h, width=test_w, coverage=coverage)

