
word = 'beekeeper'
word_length = len(word)
guesses = ['_' for _ in range(0, word_length)]

lives = 6
end_of_game = False

def update_guess(letter: str):
  for i in range(0, word_length): 
    if word[i] == letter: 
      guesses[i] = letter

while not end_of_game:

  letter = input("Guess a Letter: ")

  if letter in word:
    letter_guessed = check_letter_used(letter)

    if letter_guessed in guesses:
      print(f"You already guessed {letter}")
    else:
      update_guess(letter)
      print(guesses)

    if (len(guesses) == word_length):
      end_of_game = True

  else:
    if lives > 0:
      lives -= 1
      print('XXXXXXXXXXXXX')
      print(f"Guesses left: {6 - lives}")
    else:
      end_of_game = True
      
