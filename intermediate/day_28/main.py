from tkinter import *
from time import time, strftime, gmtime, sleep
from datetime import datetime, timedelta

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.2
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='Timer')
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    global reps
    reps += 1
    if reps % 8 == 0:
      title_label.config(text='Break', fg=RED)
      countdown(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
      title_label.config(text='Break', fg=PINK)
      countdown(SHORT_BREAK_MIN * 60)
    else:
      title_label.config(text='Work', fg=GREEN)
      countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(time_left):
    time_format = strftime("%M:%S", gmtime(time_left))
    canvas.itemconfig(timer_text, text=time_format)
    if time_left > 0: 
        global timer
        timer = window.after(1000, countdown, time_left -1)
    else:
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, 'normal'))
title_label.grid(column=1, row=0)
# Canvas is specifically to overlay widgets in a window
# Also helps that all elements will be packed together
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text='00:00', fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# Start
start_button = Button(text='Start', command=start, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset
reset_button = Button(text='Reset', command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

# Check round
check_marks = Label(text="✓", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
