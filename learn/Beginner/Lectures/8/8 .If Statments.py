# If Statment = a block of code that will excute if it's condition is ture

#age = 18 #int
#my_name = "ibrahim" #str

# age = int(input("what is your age : "))
# if(age == 18):
#     print("you're a century old.!")
# elif age >= 18:
#     print("you're an adult.!")
# elif age < 0:
#     print("you haven't been born yet.!")
# else:
#     print("you're a child.!")


my_name = input("what is your name : ")

if(my_name == "Ahmad"):
    print("that's wrong, ahmad name")
elif my_name == "Omar":
    print("that's wrong, omar name")
elif my_name == "Ibrahim":
    print("That's Correct Name")
else:
    print("Wrong Data.!")