# move a file:
import os

source = "test.txt"
destination = "C:\\Users\\hezoo\\OneDrive\\Desktop\\new_text.txt"

#FileNotFoundError try
try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved..!")
except FileNotFoundError:
    print(destination + " was not found")

