from tkinter import *
import random

# ---------------------------- CONSTANTS ------------------------------- #

FILE = 'passwords.txt'

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

NUM_LETTERS = len(LETTERS) - 1
NUM_DIGITS = len(DIGITS) - 1
NUM_SYMBOLS = len(SYMBOLS) - 1

LETTERS_REQ = 7
DIGITS_REQ = 4
SYMOBLS_REQ = 5

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    password_chars = []
    for _ in range(0, NUM_LETTERS):
        random_letter = LETTERS[random.randint(0, NUM_LETTERS)]
        password_chars.append(random_letter)

    for _ in range(0, NUM_DIGITS):
        random_digit = DIGITS[random.randint(0, NUM_DIGITS)]
        password_chars.append(random_digit)
        
    for _ in range(0, NUM_SYMBOLS):
        random_symbol = SYMBOLS[random.randint(0, NUM_SYMBOLS)]
        password_chars.append(random_symbol)

    random.shuffle(password_chars)
    password_string = ''.join(password_chars)

    if len(password.get()) > 0:
        password_entry.delete(0, END)

    password_entry.insert(0, password_string)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    password_log = f'{website} | {email} | {password}'

    with open(FILE, 'a') as f:
        f.write(password_log)
        f.write('\n')

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.minsize(width=500, height=500)
window.config(padx=30, pady=50)
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100,image=logo)
canvas.grid(column=1, row=0)

# Strings
password = StringVar()

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

id_label = Label(text='Email/Username:')
id_label.grid(column=0, row=2)

password_label = Label(text='Passowrd:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry(width=17, textvariable=password)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text="Generate Password", width=12, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
