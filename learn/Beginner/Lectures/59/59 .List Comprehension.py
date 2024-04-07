# list comprehension = a way to create a new list with less syntax
# can mimic certain lambda functions, easier to read
# list = [expression for item in iterable]
# list = [expression for item in iterable use if conditional]
# list = [expression if/else for item in iterable]

students = [100,90,80,70,60,50,40,30,20,10,0] #70

# list = [expression for item in iterable]
# passed_var = lambda Point:Point >= 70
# passed_students = list(filter(passed_var,students)) #object
# print(passed_students)
#=================
# list = [expression for item in iterable use if conditional]
# passed_students = [i for i in students if i >=70]
# print(passed_students)
#=================
# list = [expression if/else for item in iterable]
# passed_students = [i if i >= 70 else "Failed" for i in students]
# print(passed_students)

# passed_students = [i if i >= 70 else "Failed" for i in students]
# print(passed_students)

# studentss = [100,90,80,70,60,50,40,30,20,10,0] #70
# new = []
# for i in studentss:
#     if i >= 70:
#         new.append(i)
#     else:
#         new.append("Failed")
# print(new)
#==

# square = [] #1,4,9,16,25
# for i in range(1,5):
#     square.append(i * i)
# print(square)

# square_0 = [i*i for i in range(1,5)]
# print(square_0)


