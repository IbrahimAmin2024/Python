#progress-bar : geometry manager that organize widgets in a table structure in parent
import tkinter
from tkinter import *
from tkinter.ttk import *
import time

def Start():
    GB = 400
    Download = 0
    Speed = 4 #GB

    while (Download < GB):
        time.sleep(0.05)
        Progress.set(Progress.get() + ((Speed / GB) *100))
        Download+=Speed
        Percent.set(str(int((Download/GB) * 100)) + " %") #10 "%"
        Task.set(str(Download*1000) + " MB/" + str(GB) + " GB, Downloaded")
        Rate.set("Speed Rate : " + str(Speed) + " |Per Second (GB)")
        my_screen.update_idletasks()


my_screen = Tk()
#===========
my_screen.config(bg="black",
                 pady=5,
                 padx=5)

Progress = IntVar()
Percent = StringVar()
Task = StringVar()
Rate = StringVar()
#percent
tkinter.Label(my_screen,bg="black",
              fg="white",textvariable=Percent).pack(pady=5)

#progessbar
Progressbar(my_screen,
            length=500,
            mode='determinate',
            variable=Progress).pack(pady=5)

#task
tkinter.Label(my_screen,bg="black",
              fg="white",
              textvariable=Task).pack(pady=5)

#rate
tkinter.Label(my_screen,bg="black",
              fg="white",
              textvariable=Rate).pack(pady=5)

#button-download
Button(my_screen,
       text="Download",
       command=Start).pack(pady=5)
#===========
my_screen.mainloop()