# Custome Module {our own module we can create)

#messages.py

def hello():
    print("Hello this, hello func from messages module")

def bye():
    print("Bye this, Bye func from messages module")

def bye2():
    print("Bye2 this, Bye2 func from messages module")
=-=-=-
#main.py

import messages
# from messages import hello, bye , Cya
# from messages import * (import all function) this on is dangerous
# it can be import all classes contains codes and function


# from messages import bye as msg
#
# msg()

# from messages import *
# messages.bye()
