from tkinter import *
from typing import List
import pandas as pd
import random

# ----------------------- Constants ----------------------- #
BACKGROUND_COLOR = "#B1DDC6"
FRENCH_LABEL = 'French'
ENGLISH_LABEL = 'English'
words_asked = 0
current_word_index = 0

# ----------------------- Word Corpus ---------------------- #

words_df = pd.read_csv('data/french_words.csv')
words_list = []
for _, row in words_df.iterrows():
    french_word = row['French']
    english_word = row['English']
    words_list.append((french_word, english_word))

# ------------------- Event Callback --------------- #
def word_known(knew_word: bool):

    global current_word_index, words_list, words_asked
    if words_asked > 0 and knew_word: 
        words_list.pop(current_word_index)
    
    new_word()
    words_asked += 1
    
def new_word():
    """
      Generates a random french/english word pair.
      Updates the canvas with the french word first,
      waits 3 seconds then updates the canvas with it's translation.
    """
    global current_word_index
    current_word_index = random.randint(0, len(words_list) - 1)
    random_pair = words_list[current_word_index]
    french_word = random_pair[0]
    english_word = random_pair[1]

    update_canvas(french_word, FRENCH_LABEL)
    window.after(3000, update_canvas, english_word, ENGLISH_LABEL)

def update_canvas(word, language):
    """
      Update the word, language text and color of canvas card.
    """
    card_canvas.itemconfig(language_label, text=language)
    card_canvas.itemconfig(word_label, text=word)
    card_canvas.itemconfig(card_image, image=card_front_image)
    if language == 'English': 
        card_canvas.itemconfig(card_image, image=card_back_image)

# ----------------------- UI ----------------------- #

# Main Window
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Images
card_back_image = PhotoImage(file='images/card_back.png')
card_front_image = PhotoImage(file='images/card_front.png')

right_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

# Buttons
correct_button = Button(image=right_image,  highlightthickness=0, command=lambda: word_known(True))
correct_button.grid(column=0, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda: word_known(False))
wrong_button.grid(column=1, row=1)

# Card Canvas
card_canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card_canvas.create_image(400, 263, image=card_front_image)
card_canvas.grid(column=0, row=0, columnspan=2)

# Card Label
language_label = card_canvas.create_text(400, 150, text='Welcome', font=('Ariel', 30, 'italic'))
word_label = card_canvas.create_text(400, 250, text='To Flashy', font=('Ariel', 70, 'bold'))

window.mainloop()

