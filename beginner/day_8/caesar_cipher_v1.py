

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(code_string, offset, direction):

  encrypted_string = ''
  encrypted_letter_index = 0

  if direction == 'decrypt':
    offset *= -1

  for letter in code_string:
    letter_index = alphabet.index(letter)
    if letter_index + offset > 26 or letter_index + offset < 0:
      encrypted_letter_index = 26 % offset
    else:
      encrypted_letter_index = letter_index + offset

    encrypted_string += alphabet[encrypted_letter_index]

  return encrypted_string
    
continue_cipher = True

while continue_cipher:

  cipher_choice = input("Type encrypt, or decrypt: ")
  string_to_encrypt = input("Enter string: ")
  offset = int(input("Enter offset: "))
  encrypted_string = caesar(code_string=string_to_encrypt, offset=offset, direction=cipher_choice)
  print(f"New string: {encrypted_string}")
  continue_cipher = False

