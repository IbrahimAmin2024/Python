#Tuples = collection which is ordered
#         used to group together related data.
# Symbol = ()

Student = ("IA", 23, "Male")
print(Student.count("IA")) #1
print(Student.index("Male")) #2

for i in Student:
   print(i, end=" ")

if "IA" in Student:
   print("My name is there..!")
else:
   print("Not Found")