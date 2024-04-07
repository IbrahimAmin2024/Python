#class name
import messages
import bike

print(messages.__name__)
print(bike.__name__)

messages.access()

#=============
def access():
    if __name__ == "__main__":
        print("access from main module")
    else:#Messages
        print("access denied.!")