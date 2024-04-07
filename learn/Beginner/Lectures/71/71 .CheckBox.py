# Check-box = an widget, that have checker
from tkinter import *

def display():
    if clicked.get():
        print("I agree the terms")
    else:
        print("I disagree the terms")

my_screen = Tk()
#===========
image = PhotoImage(file='cato.png')

clicked = BooleanVar()
check_button = Checkbutton(my_screen,
                           text="I Agree to the term",
                           font=("Comic Sans",23,"bold"),
                           bg="black",
                           fg="blue",
                           activeforeground="blue",
                           activebackground="black",
                           padx=20,
                           pady=15,
                           variable=clicked,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           image=image,
                           compound=LEFT)
check_button.pack()


#===========
my_screen.mainloop()