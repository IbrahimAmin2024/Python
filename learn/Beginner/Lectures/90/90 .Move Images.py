#Move image By keys
#Moving the widget use (Label/Canvas) Mouse drag/keyboard
from tkinter import *
def Moving(event):
    Key = event.keysym
    if (Key == "w"):
        print("Pressed :",Key)
        canvas.move(image_id,0,-10)
    elif(Key == "a"):
        print("Pressed :",Key)
        canvas.move(image_id, -10, 0)
    elif(Key == "s"):
        print("Pressed :",Key)
        canvas.move(image_id, 0, 10)
    elif(Key == "d"):
        print("Pressed :",Key)
        canvas.move(image_id, 10, 0)

my_screen = Tk()
#===========
my_screen.config(bg="black")

#Creating Canvas Widget
canvas = Canvas(my_screen,width=600,height=600,bg="black")
canvas.pack()

# load image and place it on canvas
My_car = PhotoImage(file="car.png")
canvas.create_image(300,300,image = My_car) #0
# canvas.create_image(300,300,image = My_car) #1
# canvas.create_image(300,300,image = My_car) #2

# bind keys to Moving function
image_id = canvas.find_all()[0]
canvas.bind_all("<w>",Moving)
canvas.bind_all("<a>",Moving)
canvas.bind_all("<s>",Moving)
canvas.bind_all("<d>",Moving)

#===========
my_screen.mainloop()
