# Listbox = a listing of selectable text items within its own container
from tkinter import *
def order():
    if entry.get() == '':
     print("Please select an Order..")
    else:
        # individual Order Selector
        # selected_item = listbox.get(listbox.curselection())
        # print("I Ordered :",selected_item)

        # Multi order Selector / individual ...
        foods_selector = []  # dict, set
        for i in listbox.curselection():
            # foods_selector.insert(0,"Pizaa")
            foods_selector.insert(i, listbox.get(i))
        print("I Ordered :", foods_selector)


def add():
    if entry.get() == '':
        print("Please add an Order..")
    else:
        # listbox.insert(0,"")
        listbox.insert(listbox.size(),entry.get())#beans
        print("i Added :", entry.get())
        listbox.config(height=listbox.size())
        entry.delete(0,END)
def delete():
    # individual order deletion
    # deleted_item = listbox.get(listbox.curselection())
    # listbox.delete(listbox.curselection())
    # print("I Deleted :", deleted_item)
    # listbox.config(height=listbox.size())

    # Multi Order Deletetion
    for i in reversed(listbox.curselection()):
        print("i Deleted :", listbox.get(i))
        listbox.delete(i)
    listbox.config(height=listbox.size())
#0 3
#2 2 2
#3 0 0 0
my_screen = Tk()
#===========
my_screen.config(bg="gray",
                 pady=20,
                 padx=20)
welcome = Label(my_screen,
                text="Welcome",
                bg="gray",
                fg="black",
                font=("Comic Sans",14,"bold")
                )
welcome.pack(pady=7)

listbox = Listbox(my_screen,
                  bg="maroon",
                  fg="snow",
                  font=("Comic Sans",30,"bold"),
                  selectmode=MULTIPLE,
                  )
listbox.pack(pady=7)
listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"soup")
listbox.insert(4,"salad")
listbox.insert(5,"Koshri")

listbox.config(height=listbox.size())

entry = Entry(my_screen,
              width=73)
entry.pack(pady=7)

submitButton = Button(my_screen,
                      text="Order",
                      command=order)
submitButton.pack(pady=3)

addButton = Button(my_screen,
                      text="Add",
                      command=add)
addButton.pack(pady=3)

deleteButton = Button(my_screen,
                      text="Delete",
                      command=delete)
deleteButton.pack(pady=3)


#===========
my_screen.mainloop()