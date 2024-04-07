# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     the order of arguments doesn't matter, unlike positional arguments
#                     python knows the names of arguments that our function receives

def My_Name(My_first_Name,Middle_Name,Last_Name):

    #print("Hello " + My_first_Name + " "+ Middle_Name + " " + Last_Name) # Hello Ibrahim Ahmad Amen
    return "Hello " + My_first_Name + " "+ Middle_Name + " " + Last_Name

The_value =  My_Name(Last_Name="Amen",Middle_Name="Ahmad",My_first_Name="Ahmad")
print(The_value) # Hello Ibrahim Ahmad Amen

print(My_Name(Last_Name="Amen",Middle_Name="Ahmad",My_first_Name="Ahmad")) # Hello Ibrahim Ahmad Amen