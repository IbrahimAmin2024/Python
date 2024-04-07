#grid : geometry manager that organize widgets in a table structure in parent
from tkinter import *
my_screen = Tk()
#===========
my_screen.config(bg="black",pady=5,padx=5)

#title
Label(my_screen, text= "Enter Your info",font=("Comics Sans",20),bg="black",fg="white").grid(row=0,column=0,columnspan=2,pady=5)
#first_name (label,entry)
Label(my_screen,text="First Name : ",bg="black",fg="white").grid(row=1,column=0)
Entry(my_screen,bg="black",fg="white").grid(row=1,column=1,pady=5)
#last_name (label,entry)
Label(my_screen,text="Last Name : ",bg="black",fg="white").grid(row=2,column=0)
Entry(my_screen,bg="black",fg="white").grid(row=2,column=1,pady=5)
#email (label,entry)
Label(my_screen,text="Email : ",bg="black",fg="white").grid(row=3,column=0)
Entry(my_screen,bg="black",fg="white").grid(row=3,column=1,pady=5)
#submit Button
Button(my_screen,text="Submit").grid(row=4,column=0,columnspan=2,pady=5)
#===========
my_screen.mainloop()
