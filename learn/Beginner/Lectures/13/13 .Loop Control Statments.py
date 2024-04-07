# Loop Control Statments = change a loops excution from its normal squence

# break = used to terminate the loop entirely.
# continue = skip to the next iteration of the loop.
# pass = does nothing, acts as a placeholder.

#break
# while True:
#    name = input("Enter your name : ")
#    if name !="": #if u enter a valid name , if len(name) > 0
#       break #while loop False (terminate Close) While loop gonna be killed.

#continue
# phone_number = "923-123-456-789" #923-123-456-789 +923 (123-456-789)
# for i in phone_number: #i = 9 i = 2 i = 9 i = - ....
#    if i == "-":
#       continue
#    print(i, end="")

# phone_number = "+923(123-456-789)" #923123456789
# for i in phone_number:
#    if i == "-" or i == "(" or i == ")" or i == "+":
#       continue
#    print(i, end="") #923123456789

#pass
for i in range(1,8):
   if i == 5:
      pass
   else:
      print(i, end="")
