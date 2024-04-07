#for loop:
# a statment that will excute its block of code
# a limited amount of times
# while loop = unlimited
# for loop = limited

# for i in range(10):
#    print(i+1)

# for i in range(20,100):
#    print(i+1)

# for char in "Ibrahim Amen":
#    print(char, end="")

import time

# #icrement 0 - 10
# for seconds in range(0,10,1):
#    print(seconds+1, end="")
#    time.sleep(1)

#Decrement 0 - 10
for seconds in range(10,0,-1):
   print(seconds, end=" ")
   time.sleep(1)

print("\nFinished..")