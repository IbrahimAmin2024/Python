import tkinter
from tkinter import *

def button_press(number):
    global  equation_text
    equation_text = equation_text + str(number)
    equation_label.set(equation_text)

def equals():
    global equation_text
    #(Error Handling)
    #1) check if not pressed any syntax in the math (Done)
    #2) check if only Syntax in the math
    #3) check if result is 0 division, to prevent the error

    # if not () () () () #bad format| if no ( ) correct format
    if not ("+" in equation_label.get() or "-" in equation_label.get() or "*" in equation_label.get() or "/" in equation_label.get()):
        equation_label.set("Needed Syntax")
        equation_text = ""
        return True

        # eval performs the multiplication passed as argument
        # square_number = eval('number*number')
        # print(square_number)

    try:
        Result = str(eval(equation_text))
        equation_label.set(Result)
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("Division : Error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("Syntax : Error")
        equation_text = ""


def clears():
    global equation_text
    equation_label.set("")
    equation_text = ""

my_screen = Tk()
# ===========
my_screen.title("Calculator app")
my_screen.geometry("500x600")
my_screen.config(bg="black", pady=5, padx=5)

# Storing values:
equation_label = StringVar()

# text sender
equation_text = ""

# Create a Frame for border [Inputs]
input_frame = Frame(my_screen,background="snow")
input_frame.pack(padx=8,pady=8)

# Create a Label inside the frame of inputs
input_label = Label(input_frame,bd=0,
                    textvariable=equation_label,
                    font=("Comic Sans", 19, "bold"),
                    width=30,
                    height=2,
                    bg="black",
                    fg="snow",
                    borderwidth=5,
                    relief="ridge",
                    )
input_label.pack(padx=4,pady=4)

# Create a Frame for border [Buttons]
buttons_frame = Frame(my_screen,background="white")
buttons_frame.pack(padx=8,pady=8)

buttons_label = Label(buttons_frame,bd=0,
                      font=("Comic Sans", 19, "bold"),
                      width=30,
                      height=20,
                      bg="black",
                      borderwidth=5,
                      relief=RIDGE,
                      )
buttons_label.pack(padx=4,pady=4)

# Adding Buttons to the Parent (Label-second frame/ label buttons)
button_1 = Button(buttons_label, text=1, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(1))
button_2 = Button(buttons_label, text=2, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(2))
button_3 = Button(buttons_label, text=3, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(3))
button_4 = Button(buttons_label, text=4, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(4))
button_5 = Button(buttons_label, text=5, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(5))
button_6 = Button(buttons_label, text=6, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(6))
button_7 = Button(buttons_label, text=7, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(7))
button_8 = Button(buttons_label, text=8, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(8))
button_9 = Button(buttons_label, text=9, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(9))
button_0 = Button(buttons_label, text=0, font=("Comic Sans", 11, "bold"), height=4, width=9,
                  command=lambda: button_press(0))
button_divide = Button(buttons_label, text="/", font=("Comic Sans", 11, "bold"), height=4, width=9,
                       command=lambda: button_press("/"))
button_add = Button(buttons_label, text="+", font=("Comic Sans", 11, "bold"), height=4, width=9,
                    command=lambda: button_press("+"))
button_subtract = Button(buttons_label, text="-", font=("Comic Sans", 11, "bold"), height=4, width=9,
                         command=lambda: button_press("-"))
button_multiply = Button(buttons_label, text="*", font=("Comic Sans", 11, "bold"), height=4, width=9,
                         command=lambda: button_press("*"))
button_equal = Button(buttons_label, text="=", font=("Comic Sans", 11, "bold"), height=4, width=9,
                      command=lambda: equals())
button_dot = Button(buttons_label, text=".", font=("Comic Sans", 11, "bold"), height=4, width=9,
                    command=lambda: button_press("."))
button_clear = Button(buttons_label, text="Clear", font=("Comic Sans", 11, "bold"), height=4, width=9,
                      command=lambda: clears())


button_add.grid(row=0, column=0, padx=3, pady=3)
button_subtract.grid(row=0, column=1, padx=3, pady=3)
button_multiply.grid(row=0, column=2, padx=3, pady=3)
button_divide.grid(row=0, column=3, padx=3, pady=3)

button_1.grid(row=1, column=0, padx=3, pady=3)
button_2.grid(row=1, column=1, padx=3, pady=3)
button_3.grid(row=1, column=2, padx=3, pady=3)
button_4.grid(row=1, column=3, padx=3, pady=3)

button_5.grid(row=2, column=0, padx=3, pady=3)
button_6.grid(row=2, column=1, padx=3, pady=3)
button_7.grid(row=2, column=2, padx=3, pady=3)
button_8.grid(row=2, column=3, padx=3, pady=3)

button_9.grid(row=3, column=0, padx=3, pady=3)
button_0.grid(row=3, column=1, columnspan=3, sticky=tkinter.W + tkinter.E,pady=3,padx=3)

button_dot.grid(row=4, column=0, padx=3, pady=3)
button_clear.grid(row=4, column=1, padx=3, pady=3)
button_equal.grid(row=4, column=2, columnspan=2, sticky=tkinter.W + tkinter.E, padx=3, pady=3)

# ===========
my_screen.mainloop()