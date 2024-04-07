import os
import tkinter
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *

def change_color():
    color = colorchooser.askcolor(title="picking a color")
    text_widget.config(fg=color[1])

def change_font(*args):
    text_widget.config(font=(font_name.get(), size_box.get()))

def new_file():
    my_screen.title("Untitled")
    text_widget.delete("1.0","end")
def open_file():
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All files",
                            "*.*"),
                            ("Text Documents",
                             "*.txt"),])
    try:
        my_screen.title(os.path.basename(file))
        text_widget.delete(1.0, END)
        file = open(file, "r")
        text_widget.insert(1.0, file.read())
    except EXCEPTION as error:
        print(error)
    finally:
        file.close()
def save_file():
    file = asksaveasfilename(initialfile="untitiled.txt",
        defaultextension=".txt",
                             filetypes=[("All files",
                              "*.*"),
                              ("Text Documents",
                               "*.txt"), ])
    if file is None:
        return
    else:
        try:
            my_screen.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_widget.get(1.0,END))

            text_widget.delete(1.0, END)
            my_screen.title("Text Editor app")
        except EXCEPTION as error:
            print(error)
        finally:
            file.close()

def cut():
    text_widget.event_generate("<<Cut>>")

def copy():
    text_widget.event_generate("<<Copy>>")
def paste():
    text_widget.event_generate("<<Paste>>")
def about():
    showinfo("About this app","This app written by ia")

def quit():
    my_screen.destroy()

my_screen = Tk()
# ===========
my_screen.title("Text Editor app")
my_screen.geometry("500x500")
my_screen.config(bg="black")

# my_screen_W = 600
# my_screen_H = 600
# window_screen_w = my_screen.winfo_screenwidth()
# window_screen_h = my_screen.winfo_screenheight()
# my_screen.geometry("{}x{}".format(my_screen_W,my_screen_H))

file = None

#config Text before push to Text ==> Scrollbar
font_name = StringVar(my_screen)
font_name.set(("Comic Sans"))

font_size = StringVar(my_screen)
font_size.set(25)

#Create a Text widget to show text input
text_widget = Text(my_screen, font=(font_name.get(),font_size.get()),bg="black",fg="#78F400",
                   bd=0)
#Create a customer grid to fill whole window size
my_screen.grid_columnconfigure(0, weight=1)
my_screen.grid_rowconfigure(0, weight=1)
text_widget.grid(sticky=tkinter.N + tkinter.E + tkinter.S + tkinter.W)
#Create a scrolling the whole text
scroll_bar = Scrollbar(text_widget)
scroll_bar.pack(side=RIGHT, fill=Y)
text_widget.config(yscrollcommand=scroll_bar.set)

#===
#===
#===
#===
#===
#===
#===

#Create a bunch of buttons inside a frame
#- create Frame:
buttons_frame = Frame(my_screen,bg="black",bd=0)
buttons_frame.grid(pady=8,)
#change font color
button_colors = Button(buttons_frame, text="Change Color",
                       command=change_color,bg="black",fg="white")
button_colors.grid(row=0,column=0,padx=5)
#change font size
button_font_size = OptionMenu(buttons_frame,font_name, *font.families(),
                              command=change_font)
button_font_size.config(bg="black", fg="WHITE",bd=0)
button_font_size.grid(row=0,column=1,padx=5)


size_box = Spinbox(buttons_frame, from_=1,to=100,
                   textvariable=font_size,
                   command=change_font,bg="black",fg="white")
size_box.grid(row=0,column=2,padx=5)

# Create a menu to my screen
menu_bar = Menu(my_screen)
my_screen.config(menu=menu_bar)

# create a menu toolbar item Called "File"
file_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
# create option inside toolbar item
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

# create a menu toolbar item Called "Edit"
edit_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
# create option inside toolbar item
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

# create a menu toolbar item Called "Help"
help_menu = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
# create option inside toolbar item
help_menu.add_command(label="About", command=about)

# ===========
my_screen.mainloop()