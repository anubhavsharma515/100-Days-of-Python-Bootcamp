import random
from game_data import data
from art import logo, vs



user_score = 0
user_lost = False
celebrities = len(data)

def compare(a, b):
  if a > b:
    return 'A'
  else:
    return 'B'

def check(user_choice, answer):
  if user_choice == answer:
    return True

  return False

while not(user_lost):

  print(logo)
  if user_score == 0:
    celebrity_a = data[random.randint(0, celebrities)]
    celebrity_b = data[random.randint(0, celebrities)]
  elif celebrity_a == celebirty_b:
    celebrity_b = data[random.randint(0, celebrities)]
  else:
    celebrity_b = data[random.randint(0, celebrities)]

  print(f" Compare A: {celebrity_a['name']}, a {celebrity_a['description']} from {celebrity_a['country']}.")
  print(vs)
  print(f" Compare B: {celebrity_b['name']}, a {celebrity_b['description']} from {celebrity_b['country']}.")
  user_choice = input("Who has more followers? A or B?: ")
  user_celebrity = celebrity_a if user_choice == 'A' else celebrity_b
  answer = compare(celebrity_a['follower_count'], celebrity_b['follower_count'])
  if check(user_choice, answer):
    celebrity_a = user_celebrity
    user_score += 1
    print(f"Correct! Current Score: {user_score}")
  else:
    print(f"Sorry, that's incorrect! Final score: {user_score}")
    user_lost = True
  
