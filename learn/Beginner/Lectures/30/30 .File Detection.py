# File Detection : many methods about file path
import os #opeartion system
path = "C:\\Users\\hezoo\\OneDrive\\Desktop\\test.txt"

if os.path.exists("C:\\Users\\hezoo\\OneDrive\\Desktop\\"):
    print("That location exist!")
    if os.path.isfile(path):
        print("That's a file!")
    elif (os.path.isdir(path)):
        print("That's a directory!")
    else:
        print("That file doen't exist!")

else:
    print("That location doesn't exist!")