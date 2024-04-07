# Text Widget = can enter multiple line of text, (not only 1 line like Entry)
from tkinter import *

def clicking():
    texts = text.get("1.0",END)
    print("My text :", texts)
my_screen = Tk()
#===========
my_screen.config(
    bg="black",
    pady=25,
    padx=25,
)

text = Text(my_screen,
            fg="white",
            bg="black",
            font=("Ink Free",19,"bold"),
            height=10,
            width=45,
            )
text.pack(pady=10)

button = Button(my_screen,
                text="Show Me Texts",
                command=clicking)
button.pack()
#===========
my_screen.mainloop()