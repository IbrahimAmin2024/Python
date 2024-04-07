# frame = a container to group and hold widgets
from tkinter import *
my_screen = Tk()
#===========
my_screen.geometry("220x144")
my_screen.config(bg="black",)
frame = Frame(my_screen,bg="black",bd=5,relief=SUNKEN)
frame.place(x=0,y=0)

Button(frame,text="W", font=("Comics Sans",25,"bold"),width=3).pack(side=TOP)
Button(frame,text="A", font=("Comics Sans",25,"bold"),width=3).pack(side=LEFT)
Button(frame,text="S", font=("Comics Sans",25,"bold"),width=3).pack(side=LEFT)
Button(frame,text="D", font=("Comics Sans",25,"bold"),width=3).pack(side=LEFT)

#===========
my_screen.mainloop()