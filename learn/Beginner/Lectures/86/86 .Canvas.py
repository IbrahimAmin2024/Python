#canvas : widget that used to draw graphs, plots, images in a window
from tkinter import *
my_screen = Tk()
#===========
my_screen.config(bg="black",pady=15,padx=15)
canvas = Canvas(my_screen,height=500,width=500)

# canvas.create_line(0,0,500,500,fill="yellow",width=10) #first point(x,y), second point(x,y)
# canvas.create_line(0,500,500,0,fill="blue",width=10) #first point(x,y), second point(x,y)

# point_list = [50,10,400,400]
# canvas.create_rectangle(point_list,fill="yellow",outline="red",width=5) #xleft,ybutton,x width, y width

# canvas.create_polygon(250,15,500,500,0,500) #top(x,y), right(x,y), left(x,y)
# canvas.create_arc(0,0,500,500, fill="red",extent=359)

#Task Pookemon:
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=5)
canvas.create_arc(0,0,500,500,fill="white",extent=180,width=5,start=180)
canvas.create_oval(190,190,310,310,fill="yellow",width=5)

canvas.pack()
#===========
my_screen.mainloop()