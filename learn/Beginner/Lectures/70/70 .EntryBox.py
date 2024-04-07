# entry widget = an widget, that have textbox accept single line of user input
from tkinter import *

def Submit():
    print("Submitted, " + entry.get())
    # entry.config(state=DISABLED)
    # entry.config(show="*")
    # entry.delete(0,END)
    # entry.insert(0,"Thanks for ur submit")


def Delete():
    print("Deleted," , entry.get())
    entry.delete(0, END)

def Backspace():
    last_string = entry.get()[-1]
    print("Last 2 string :" , entry.get()[-2:])
    print("Removed,", last_string)
    entry.delete(len(entry.get())-1,END)

my_screen = Tk()
#===========

submit_button = Button(my_screen,text="Submit",command=Submit)
submit_button.pack(side=RIGHT)

delete_button = Button(my_screen,text="Delete",command=Delete)
delete_button.pack(side=RIGHT)

BackSpace_button = Button(my_screen,text="Backspace",command=Backspace)
BackSpace_button.pack(side=RIGHT)

entry = Entry(my_screen,
              font=("Comic Sans",66),
              fg="blue",
              bg="black",
              )
entry.pack(side=LEFT)


#===========
my_screen.mainloop()