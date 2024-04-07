# nested function calls = function calls inside other function calls
#                     innermost function calls are resolved first
#                     returned value is used as argument for the next outer function

# Method : 1
numb = input("please Enter A number : ")
numb = float(numb) #3 3.0
numb = abs(numb)
numb = round(numb)
print(numb)

# Method : 2

print(round(abs(float(input("please Enter A number : ")))))

#print(round(abs(float(input("Enter num : "))))) for explanation porpuse