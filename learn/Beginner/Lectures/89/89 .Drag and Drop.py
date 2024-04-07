# bind 1 : click (x,y)
# bind 2 : move (x,y) Hold and draging
# Result : bind1,bind2 (x,y)
#widget.place(Result)
from tkinter import *
def click(event):
    # label_1.startingx = event.x
    # label_1.startingy = event.y
    widget = event.widget
    widget.startingx = event.x
    widget.startingy = event.y

def move(event):
    #X = Top Left Cornor for the X - Clicked x Postion + Draging new Position x

    # x = label_1.winfo_x() - label_1.startingx + event.x
    # y = label_1.winfo_y() - label_1.startingy + event.y
    # label_1.place(x=x,y=y)

    widget = event.widget
    x = widget.winfo_x() - widget.startingx + event.x
    y = widget.winfo_y() - widget.startingy + event.y
    widget.place(x=x,y=y)

my_screen = Tk()
#===========
my_screen.config(bg="black",pady=5,padx=5)

label_1 = Label(my_screen, bg="yellow", height=5,width=10)
label_1.place(x=10,y=10)

label_2 = Label(my_screen, bg="blue", height=5,width=10)
label_2.place(x=90,y=90)

label_3 = Label(my_screen, bg="red", height=5,width=10)
label_3.place(x=160,y=160)

#Button-1 click, Motion, B1-Motion Drag and move (Clicked and holding this widget to move it)
label_1.bind("<Button-1>", click) #click
label_1.bind("<B1-Motion>", move) #drag and move

label_2.bind("<Button-1>", click) #click
label_2.bind("<B1-Motion>", move) #drag and move

label_3.bind("<Button-1>", click) #click
label_3.bind("<B1-Motion>", move) #drag and move
#===========
my_screen.mainloop()