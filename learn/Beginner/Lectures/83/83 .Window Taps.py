from tkinter import *
from tkinter import ttk #separate Module / sub module
my_screen = Tk()
#===========
my_screen.config(bg="black")

#grand
Grand = ttk.Notebook(my_screen) #manage collection of windows and display

#father
tab1 = Frame(Grand) # new frame separated from Grand
tab2 = Frame(Grand) # new frame separated from Grand

#call grand
Grand.add(tab1,text="Tab 1")
Grand.add(tab2,text="Tab 2")

Grand.pack(expand=True,fill='both')

#child
Label(tab1,text="Text 1 , come from father (Tab 1)").pack()
Label(tab2,text="Text 2 , come from father (Tab 2)").pack()
#===========
my_screen.mainloop()