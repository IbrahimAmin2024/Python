# open a file = open a file, no need description, baka
from tkinter import *
from tkinter import filedialog
#save mode
#'a' # append mode
#'w' # write mode
#read mode
#'r' # read mode

def Save():
   file_path = filedialog.asksaveasfile(
                                        title="Save a file",
                                        filetypes=[
                                        ("Text Files", "*.txt")],)

   checking = input("u want add new futures (y/n) : ").lower()
   if checking == "y":
       addition = input("what text u want to add : ")
       file_content = str(text.get(1.0,END)) + addition
       file_path.write(file_content)
       file_path.close()
       print("ok, Done. thx")
   else:
     file_content = str(text.get(1.0, END))
     file_path.write(file_content)
     file_path.close()
     print("whatever, bye")

my_screen = Tk() #Screen
#===========

my_screen.config(bg="black",
                 pady=25,
                 padx=25)
text = Text(bg="black",
            fg="white")
text.pack()


button = Button(my_screen,
                text="save a file",
                command=Save,
                )
button.pack(pady=8)
#===========
my_screen.mainloop()

