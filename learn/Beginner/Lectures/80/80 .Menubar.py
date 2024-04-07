# menu-bar = a menu which we got many items on it
from tkinter import *
def Open_File():
    print("file opened")
def Save_File():
    print("file saved")
def Exit():
    print("quit")
def cut():
    print("cut")
def copy():
    print("copy")
def paste():
    print("paste")
my_screen = Tk()
#===========
Grand_menu = Menu(my_screen)
image = PhotoImage(file="pizza.png")

my_screen.geometry("600x400")
my_screen.config(bg="black",
                 pady=25,
                 padx=25,
                 menu=Grand_menu,
                 )
my_screen.title("Menu-Bar")

Father_1_Menu = Menu(Grand_menu,font=("Comic Sans",12,"bold"),tearoff=0)
Grand_menu.add_cascade(label="File", menu= Father_1_Menu)

Father_1_Menu.add_command(label="Open",image=image,compound="left",command=Open_File)
Father_1_Menu.add_command(label="Save",image=image,compound=LEFT,command=Save_File)
Father_1_Menu.add_separator()
Father_1_Menu.add_command(label="Exit",command=Exit)

Father_2_Menu = Menu(Grand_menu,font=("Comic Sans",12,"bold"),tearoff=0)
Grand_menu.add_cascade(label="Edit", menu= Father_2_Menu)

Father_2_Menu.add_command(label="Cut",image=image,compound="left",command=cut)
Father_2_Menu.add_command(label="Copy",image=image,compound=LEFT,command=copy)
Father_2_Menu.add_command(label="Paste",command=paste)

#===========
my_screen.mainloop()