# filter() = creates a collection of elements from an iterable for which a function return true
# filter(function,iterable)

family = [
    ("Amr",20),
    ("Eslam",18),
    ("Karim",25),
    ("Sayd",15),
    ("Adel",17),
    ("Body", 10),
    ("Omar",22)
] # >= 18

#function object
#Points = lambda Point:Point[2]
# to_euro = lambda index: (index[0],index[1]*0.94)
ages = lambda age:age[1] >= 18
older_enough = list(filter(ages,family))

for i in older_enough:
    print(i)