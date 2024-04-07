# Read a file

# with open('C:\\Users\\hezoo\\OneDrive\\Desktop\\test.txt')

try:
    with open('test.txt') as file:
        print(file.read())

except FileNotFoundError:
    print("That file was not found!")