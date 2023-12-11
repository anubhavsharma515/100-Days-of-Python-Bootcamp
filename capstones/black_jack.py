#Implementation
# 1. See if user want's to play
# 2. If they do, deal them two cards
# 3. If they do, deal the computer one card
# 4. Everytime they are dealt cards, update their current score
# 5. If their current score > 21, they lose. end game
# 6. If they don't want to play, deal a computer card
# 7. Calculate comp score.
# 8. If current score < 17, deal another card. If > 17 and their diff to 21 < player's computer wins. Else user wins. If same diff, end in draw.


import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
hands = {'User': { 'Cards': [], 'Score': 0, 'Bust': False }, 'Computer': { 'Cards': [], 'Score': 0, 'Bust': False }}
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
play = True


def check_ace(cards):

  if 11 in cards:
    return True
  
  return False

def deal_cards(player, num_cards):
  for _ in range(1, num_cards+1):
    dealt_card = cards[random.randint(0, 12)]
    hands[player]['Cards'].append(dealt_card)
    print(hands[player]['Cards'])

def validate_score(player):
  hands[player]['Cards'].remove(11)
  hands[player]['Cards'].append(11)

def calculate_score(player):
  hands[player]['Score'] = sum(hands[player]['Cards'])

def check_winner():
  for player in hands.keys():
    if (hands[player]['Score'] == 21 and hands[player]['Cards'] == 2):
      return True
    elif (hands[player]['Score'] > 21):
      return True

  return False

def check_bust(player):
  if hands[player]['Score'] > 21:
    if check_ace(hands[player]['Cards']):
      validate_score('User')
      calculate_score('User')
      check_bust('User')
    return True

  return False
   

def play(player=['User', 'Computer'], first_round=False, cards=1):
  
  if first_round:
    for player in hands.keys():

      print(player)
      deal_cards(player, cards)
      calculate_score(player)
      print(f"Your Score: {hands[player]['Score']}")
      print(f"Your Cards: {hands[player]['Cards']}")
  else:
    deal_cards(player, cards)
    calculate_score(player)
    print(f"Your Score: {hands[player]['Score']}")
    print(f"Your Cards: {hands[player]['Cards']}")

  if check_winner():
    return
  elif check_bust('User'):
    return
  else:
    continue_game = input("Do you wan't another card? Type 'y' or 'n': ")
    if continue_game == 'y':
      play(player='User')
    else:
      if hands['Computer']['Score'] < 16:
        play(player='Computer')
      
      
if start_game == 'y':
  play(first_round=True, cards=2)
else:
  print("Okay, see you soon!")

