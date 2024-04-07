# Radio-Button = an widget, that u can select one from group
from tkinter import *

def Display():
    if x.get() == 0:
        print("You will order :", "Pizza")
    elif x.get() == 1:
        print("You will order :", "Hamburger")
    elif x.get() == 2:
        print("You will order :","Hotdog")
    else:
        print("WTF ?!")

my_screen = Tk()
#===========
food = ['pizza','hamburger','hotdog']

pizza = PhotoImage(file='pizza.png')
hamburger = PhotoImage(file='hamburger.png')
hotdog = PhotoImage(file='hotdog.png')

food_image = [pizza,hamburger,hotdog]
x = IntVar()

for i in range(len(food)):
    Radio_Button = Radiobutton(my_screen,
                               text=food[i],
                               font=("Comic Sans",43,"bold"),
                               image=food_image[i],
                               compound=LEFT,
                               variable=x,
                               value=i,
                               indicatoron=0,
                               width=350,
                               pady=20,
                               padx=30,
                               command=Display,
                               )
    Radio_Button.pack(anchor=W)
#===========
my_screen.mainloop()