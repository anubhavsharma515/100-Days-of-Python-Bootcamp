

word = 'beekeeper'
word_length = len(word)
guesses = ['_' for _ in range(0, word_length)]

wrong_guesses = 0
word_guessed = False

letters_used = []

def check_letter_used(letter: str):
  if letter in letters_used:
    return True
  
  letters_used.append(letter)
  return False

def update_guess(letter: str):
  for i in range(0, word_length): 
    if word[i] == letter: 
      guesses[i] = letter

while wrong_guesses < 6 and not(word_guessed):
  letter = input("Guess a Letter: ")
  if letter in word:
    letter_guessed = check_letter_used(letter)
    if letter_guessed:
      print(f"You already guessed {letter}")
    else:
      update_guess(letter)
      print(guesses)

    if (len(guesses) == word_length):
      word_guessed = True

  else:
    print('XXXXXXXXXXXXX')
    wrong_guesses += 1
    print(f"Guesses left: {6 - wrong_guesses}")
    
