import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_turns(difficulty):
  if difficulty == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def check_guess(answer, guess):
    if guess > answer:
      print("Too high")
      return False
    elif guess < answer:
      print("Too Low")
      return False
    else:
      print(f"You guessed it! The number was {answer}.")
      return True

def game():
  
  print('''
    Welcome to the number guessing game!\n
    I'm thinking of a number between 1 and 100.
  ''')
  answer = random.randint(1, 100)
  difficulty = input("Choose difficulty, 'easy' or 'hard': ")
  turns = set_turns(difficulty)
  game_over = False

  while not(game_over):
    print(f"You have {turns} guesses left.")
    guess = int(input("Make a guess: "))
    if turns == 0:
      game_over = True 
    elif check_guess(answer, guess):
      game_over = True
    else:
      turns -= 1
    
game()
