from tkinter import *

def update_label():
    my_label.config(text=entry.get())

window = Tk()
window.minsize(width=500, height=500)
window.title('Miles to KM Converter')

my_label = Label(text='I am a Label')
my_label.pack()
    
but = Button(text="Click Me!", command=update_label)
but.pack()

entry = Entry(width=10)
entry.pack()

window.mainloop()

