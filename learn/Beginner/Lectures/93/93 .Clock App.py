# Clock Program: simple gui showing my time
# Python strftime() ( https://www.programiz.com/python-programming/datetime/strftime )
from tkinter import *
from datetime import datetime
# counter = 0
def Update_Ui():
    # global counter
    # counter+=1
    # time_label.config(text="Counted : "+ str(counter))
    now = datetime.now()

    Time_String = now.strftime("%H:%M:%S %p")
    time_label.config(text=Time_String)

    Day_String = now.strftime("%A")
    day_label.config(text=Day_String)

    Date_String = now.strftime("%B %d, %Y")
    date_label.config(text=Date_String)

    date_label.after(1000,Update_Ui)

my_screen = Tk()
#===========
my_screen.config(bg="black")

time_label = Label(my_screen,font=("Comic Sans",19,"bold"),fg="snow",bg="black",)
time_label.pack()

day_label = Label(my_screen,font=("Ink Free",15),fg="snow",bg="black",
                   )
day_label.pack()

date_label = Label(my_screen,font=("Arial",15,),fg="snow",bg="black",
                  )
date_label.pack()

Update_Ui()
#===========
my_screen.mainloop()