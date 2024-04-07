# Color-Chooser = a simple pop-up Dialog which contains many messages type
from tkinter import *
from tkinter import colorchooser #sub-module
def click():
    color = colorchooser.askcolor()
    color_Hax = color[1]
    my_screen.config(bg=color_Hax)
    # print(color)
my_screen = Tk()
#===========
my_screen.config(bg="black",
                 pady=25,
                 padx=25)
my_screen.geometry("500x500")

button_1 = Button(my_screen,
                command=click,
                text="Change Background Color of the Screen",
                font=("Comic Sans",13,"bold"))
button_1.pack(pady=10)

#===========
my_screen.mainloop()