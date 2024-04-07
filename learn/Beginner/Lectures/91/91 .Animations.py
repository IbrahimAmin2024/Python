# 2D Animation
from tkinter import *
import time

My_Width = 500
My_Height = 500

move_x = 1
move_y = 5

my_screen = Tk()
#===========

#Creating Canvas Widget
canvas = Canvas(my_screen,height=My_Height,width=My_Width,bg="black")
canvas.pack()

# load image and place it on canvas
Bk_img = PhotoImage(file='bk.png')
bk_ = canvas.create_image(0,0,image=Bk_img,anchor=NW) #0 #Northwest

Face_img = PhotoImage(file='troll.png')
My_Face = canvas.create_image(0,0,image=Face_img,anchor=NW) #0 #Northwest


while True:
    Coordinates = canvas.coords(My_Face)
    if (Coordinates[0]>=(My_Width-Face_img.width()) or Coordinates[0] <0): #x Width
        move_x = -move_x

    if (Coordinates[1]>=(My_Height-Face_img.height()) or Coordinates[1] <0): #X Height
        move_y = -move_y

    canvas.move(My_Face,move_x,move_y) # buged ui freezed
    my_screen.update()
    time.sleep(0.01)
    # print(Coordinates)
#===========
my_screen.mainloop()
