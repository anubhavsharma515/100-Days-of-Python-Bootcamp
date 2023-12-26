

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(code_string, offset):

  encrypted_string = ''
  encrypted_letter_index = 0

  for letter in code_string:
    letter_index = alphabet.index(letter)
    if letter_index + offset > 25:
      encrypted_letter_index =  offset - (26 % letter_index)
    else:
      encrypted_letter_index = letter_index + offset

    encrypted_string += alphabet[encrypted_letter_index]

  return encrypted_string
    

def decrypt(code_string, offset):

  decrypted_string = ''
  decrypted_letter_index = 0

  for letter in code_string:
    letter_index = alphabet.index(letter)
    if letter_index - offset <= 0:
      decrypted_letter_index = letter_index - offset
    else:
      decrypted_letter_index = letter_index - offset

    decrypted_string += alphabet[decrypted_letter_index]

  return decrypted_string

continue_cipher = True

while continue_cipher:

  cipher_choice = input("Type encrypt, or decrypt: ")
  if cipher_choice == 'encrypt':
    string_to_encrypt = input("Enter string to encrypt: ")
    offset = int(input("Enter offset: "))
    encrypted_string = encrypt(code_string=string_to_encrypt, offset=offset)
    print(f"Encrypted string: {encrypted_string}")
    continue_cipher = False
  else:
    string_to_decrypt = input("Enter string to decrypt: ")
    offset = int(input("Enter offset: "))
    decrypted_string = decrypt(code_string=string_to_decrypt, offset=offset)
    print(f"Decrypted string: {decrypted_string}")
    continue_cipher = False
