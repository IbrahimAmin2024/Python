# GUI : Graphical user interface
from tkinter import *

screen = Tk() #instantiate an instance of window
#============

screen.geometry("500x500")
screen.title("My first program created by IA")

My_Icon = PhotoImage(file="cato.png")
screen.iconphoto(True,My_Icon)

screen.config(background="black",
            )
#============
screen.mainloop() #place screen on computer screen