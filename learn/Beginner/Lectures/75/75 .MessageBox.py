# Message-Box = a simple pop-up Dialog which contains many messages type

from tkinter import *
from tkinter import messagebox

def msg_1():
    messagebox.showinfo(title="show info",message="msg msg msg msg msg")
def msg_2():
    messagebox.showwarning(title="show warning",message="msg msg msg msg msg")
def msg_3():
    messagebox.showerror(title="show error", message="msg msg msg msg msg")
def msg_4():
   if messagebox.askokcancel(title="show yes or no",message="msg msg msg msg msg"):
       print("i agree")
   else:
       print("i disagree")
def msg_5():
   if messagebox.askretrycancel(title="show retry",message="msg msg msg msg msg"):
       print("i agree")
   else:
       print("i disagree")

def msg_6():
   answer = messagebox.askquestion(title="show ask question", message="msg msg msg msg msg")
   if answer == "yes":
       print("i agree question")
   else:
       print("i disagree question")

def msg_7():
    answer = messagebox.askyesnocancel(title="show ask yes no cancel",message="msg msg msg msg msg",icon="warning")
    if answer:
       print("i agree")
    elif answer == False:
       print("i disagree")
    elif answer == None:
       print("i canceled [Dodged the Question]")

my_screen = Tk() #Screen
#===========
my_screen.config(bg="black",pady=25,padx=25)
my_screen.geometry("500x500")
button_1 = Button(my_screen,
                command=msg_1,
                text="msg:show info",
                font=("Comic Sans",13,"bold"))
button_1.pack(pady=10)

button_2 = Button(my_screen,
                command=msg_2,
                text="msg:show warning",
                font=("Comic Sans",13,"bold"))
button_2.pack(pady=10)

button_3 = Button(my_screen,
                command=msg_3,
                text="msg:show error",
                font=("Comic Sans",13,"bold"))
button_3.pack(pady=10)

button_4 = Button(my_screen,
                command=msg_4,
                text="msg:show ask ok or cancel",
                font=("Comic Sans",13,"bold"))
button_4.pack(pady=10)

button_5 = Button(my_screen,
                command=msg_5,
                text="msg:show ask retry",
                font=("Comic Sans",13,"bold"))
button_5.pack(pady=10)

button_6 = Button(my_screen,
                command=msg_6,
                text="msg:show ask question",
                font=("Comic Sans",13,"bold"))
button_6.pack(pady=10)

button_7 = Button(my_screen,
                command=msg_7,
                text="msg:show ask yes no cancel",
                font=("Comic Sans",13,"bold"))
button_7.pack(pady=10)
#===========
my_screen.mainloop()

