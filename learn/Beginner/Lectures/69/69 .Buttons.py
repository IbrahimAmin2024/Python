# Button = an widget, u click, then it does stuff.
from tkinter import *
count = 0

def Clicking():
    global count
    count+=1
    print("You clicked me :",count)

my_screen = Tk()
#===========
like = PhotoImage(file='like.png')

button = Button(my_screen,
                text="Click me...",
                font=("Comic Sans",13,"bold"),
                fg="blue",
                bg="black",
                activeforeground="blue",
                activebackground="black",
                command=Clicking,
                state=ACTIVE,
                image=like,
                compound=TOP
                ).pack()


#===========
my_screen.mainloop()