# labels : an area widget that holds text and / image within a window
from tkinter import *
my_screen =  Tk()
#=============
image = PhotoImage(file="cato.png")

label = Label(my_screen,
              text="im Catoo, This from Dev IA....",
              font=("Arial",45,"bold"),
              fg="yellow",
              bg="black",
              relief=SUNKEN,
              bd=25,
              padx=25,
              pady=25,
              image=image,
              compound="top"
              ).pack()


#=============
my_screen.mainloop()