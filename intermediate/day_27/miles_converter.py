from tkinter import *

def convert():
    miles = int(miles_entry.get())
    km = 1.6 * miles
    km_entry.config(text=f"{km:.0f}")

window = Tk()
window.title('Mile to Km Converter')
window.config(padx=20, pady=30)

miles_entry = Entry(width=5)
miles_entry.grid(row=0, column=1)
miles_entry.focus()

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)

equals_entry = Label(text='is equal to')
equals_entry.grid(row=1, column=0)

km_entry = Label(text='0')
km_entry.grid(row=1, column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=convert)
calculate_button.grid(row=2, column=1)

window.mainloop()



