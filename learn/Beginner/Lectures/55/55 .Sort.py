# sort() method = used with lists
# test = [("Billa","a",20),("Zill","C",23),("Amr","f",22)]
# test.sort()
# for i in test:
#     print(i)
#==========================
# sort() function = used with iterables
# test = (("Billa","a",20),("Zill","C",23),("Amr","f",22))
# sorted_test = sorted(test)
# for i in sorted_test:
#     print(i)
#==========================
#method
# students = ["Ibrahim","Ahmad","Omar","Karim","Eslam","Amr"]
# students.sort(reverse=True)
# for i in students:
#     print(i)
#==========
# function
# students = ("Ibrahim","Ahmad","Omar","Karim","Eslam","Amr")
# sorted_list = sorted(students,reverse=True)
# for i in sorted_list:
#     print(i)
#===========

students = [
    ("Ibrahim","A",22),
    ("Ahmad","E",19),
    ("Omar","B",20),
    ("Karim","C",21),
    ("Eslam","D",23),
    ("Amr","F",24)
]
# students.sort()
# for i in students:
#     print(i)

#function object
Points = lambda Point:Point[2]
students.sort(key=Points,reverse=True)

for i in students:
    print(i)