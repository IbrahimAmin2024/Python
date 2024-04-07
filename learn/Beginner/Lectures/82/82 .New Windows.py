from tkinter import *
#.Toplevel() = new window 'on top'.
#.Tk() = new independent winow.
#.destroy() = (closing out of old window).
def create_screan():
    new_screen = Toplevel()

    new_screen = Tk()
    old_screen.destroy()

old_screen = Tk()
#===========
Button(old_screen,text="Create new screen",command=create_screan).pack()
#===========
old_screen.mainloop()