import pandas as pd

nato_df = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {}
for _, value in nato_df.iterrows():
    nato_dict[value.letter] = value.code

name = input('Enter the name you want to encode: ')

encoded = [nato_dict.get(letter.upper()) for letter in name]
print(encoded)

