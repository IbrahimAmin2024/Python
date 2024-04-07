# scope = the region that a variable is recognized
#                     a variable is only available from inside the region it is created
#                     a global and locally scoped versions of a variable can be created

name = "Ibrahim" # globaly scope (available inside & outside functions)

def Display_my_name():
    name = "Ahmad" # Local scope (available only inside this function)
    print(name)

Display_my_name()
print(name)
