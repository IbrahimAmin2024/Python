# Scale = The Scale widget provides a graphical slider object that allows
#          you to select values from a specific scale

from tkinter import *

def Checking():
    print("The Temperature is : "+ str(scale.get()) + " Degree Celicious")

my_screen = Tk()
#===========
my_screen.geometry("180x500")

image_hot = PhotoImage(file='hot.png')
hot_label = Label(text="Hot",image=image_hot,compound=TOP)
hot_label.pack()

scale = Scale(my_screen,
              from_=100,
              to=0,
              orient=VERTICAL,
              font=("Comic Sans",13,"bold"),
              tickinterval=10,
              length=300,
              troughcolor='blue',
              fg='white',
              bg='black',
              )
scale.pack()


image_cold = PhotoImage(file='cold.png')
cold_label = Label(text="Cold",image=image_cold,compound=TOP)
cold_label.pack()

submit_button = Button(my_screen,text="Checking..",command=Checking)
submit_button.pack()
#===========
my_screen.mainloop()