# Multiple Animations: animate multi Objects
from tkinter import *
import time
from ball import Ball

My_Width = 800
My_Height = 600

my_screen = Tk()
#===========

#Creating Canvas Widget
canvas = Canvas(my_screen,height=My_Height,width=My_Width,bg="gray")
canvas.pack()

volly_ball1 = Ball(canvas,0,0,50,3,7,"black")
volly_ball2 = Ball(canvas,0,0,70,5,6,"red")
volly_ball3 = Ball(canvas,0,0,60,6,3,"yellow")
volly_ball4 = Ball(canvas,0,0,90,8,10,"brown")
volly_ball5 = Ball(canvas,0,0,55,7,4,"blue")
volly_ball6 = Ball(canvas,0,0,33,10,8,"green")
volly_ball7 = Ball(canvas,0,0,51,9,5,"pink")

while True:
    volly_ball1.move()
    volly_ball2.move()
    volly_ball3.move()
    volly_ball4.move()
    volly_ball5.move()
    volly_ball6.move()
    volly_ball7.move()
    my_screen.update()
    time.sleep(0.01)
# ball1 = Ball(canvas,0,0,100,3,7,"black") #canvas(master,x,y,diameter,movingx,movingy,color)
#===========
my_screen.mainloop()


##### ball.py class

class Ball():
    # canvas(master,x,y,diameter,movingx,movingy,color)

    def __init__(self,canvas,x,y,diameter,move_x,move_y,color):
        self.canvas = canvas
        self.image = canvas.create_oval(x,y,diameter,diameter,fill=color) #x,y,diameterx,diametery,fill=color
        self.moving_x = move_x
        self.moving_y = move_y

    def move(self):
        Coordinates = self.canvas.coords(self.image)
        print(Coordinates)

        if ( Coordinates[2]>= self.canvas.winfo_width() or Coordinates[0]<0):
            self.moving_x = -self.moving_x

        if ( Coordinates[3]>= self.canvas.winfo_height() or Coordinates[1]<0):
            self.moving_y = -self.moving_y

        self.canvas.move(self.image, self.moving_x, self.moving_y)



