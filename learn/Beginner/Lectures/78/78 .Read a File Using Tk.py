# open a file = open a file, no need description, baka
from tkinter import *
from tkinter import filedialog #sub module

#save mode
#'a' # append mode
#'w' # write mode
#read mode
#'r' # read mode

def Open():
    file_path = filedialog.askopenfilename(title="Open a file",initialdir="D:\\",
                                           filetypes=(
                                               ("Text Files","*.txt"),
                                               ("Applications","*.exe")
                                           ),)
    # print(file_path)
    file_contet = open(file_path,'r')
    print(file_contet.read()) #read streaming file
    file_contet.close()

my_screen = Tk()
#===========
my_screen.geometry("500x500")

my_screen.config(bg="black",
                 pady=25,
                 padx=25)

button = Button(my_screen,
                text="open a file",
                command=Open,
                font=("Comic Sans",25,"bold"),)
button.pack()
#===========
my_screen.mainloop()