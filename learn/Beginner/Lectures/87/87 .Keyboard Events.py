#Keyboard Events : can bind key event/ widget, when pressed a key
#                  we trigger a function to be called
import tkinter
from tkinter import *
from tkinter.ttk import *

def show(event):
    print("Pressed", event.keysym)
    # label.config(text="Pressed : " + event.keysym)
    text.set("Pressed : " + event.keysym)

my_screen = Tk()
#===========
my_screen.config(bg="black",pady=5,padx=5)

text = StringVar()

# label = tkinter.Label(my_screen,bg="black",fg="white",font=("Comic Sans",35,"bold"))
# label.pack()

tkinter.Label(my_screen,bg="black",fg="white",font=("Comic Sans",35,"bold"),textvariable=text).pack()

my_screen.bind("<Key>",show) #Return {Enter},w,e,s,Up,Down, Key :for nay key pressed
#===========
my_screen.mainloop()
