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

def deal_cards(player, hands):
  for i in range(1, hands):
    dealt_card = cards[random.randint(0, 13)]
    hands[player]['Cards'].append(dealt_card)

def validate_score(player)

  if hands[player]['Score'] > 21:
    has_ace = check_ace(hands[player]['Cards'])
    if has_ace:
      ace_index = hands[player]['Cards'].index(11)
      hands[player]['Cards'][ace_index] = 1
    else: 
      hands[player]['Bust'] = True

def calculate_score(player):
  hands[player]['Score'] = sum(hands[player]['Cards'])

def check_winner():


def play(player, cards, first_round=False):
  
  if first_round:
    deal_cards('User', cards)
    calculate_score('User')

    deal_cards('Computer', cards)
    calculate_score('Computer')
  else:
    deal_cards(player, cards)
    calculate_score(player)

  check_winner()
  if not(hands['User']['Bust']) and hands['User']['Score'] > 21:
    calculate_score('User')
  else: 
    if hands['Computer']['Score'] < 17:
      play(0, 2, False)


if start_game == 'y':
  play(2, True)
else:
  print("Okay, see you soon!")



