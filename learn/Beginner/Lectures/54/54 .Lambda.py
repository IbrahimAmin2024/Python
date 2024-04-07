# lambda Function = unction written in 1 line using lambda keyword :
#                 accepts any numbers of arguments, but 1 expression.
#                 (Think of it as a shortcut)
#                 (useful if needed for a short period of time, throw-away)
# lambda parameters: expression


double = lambda x: x * 2
multiply = lambda x,y : x * y
add = lambda x,y,z: x + y +z
full_name = lambda first_name,last_name: first_name+ " " + last_name
age_check = lambda age:True if age >= 18 else False
print(age_check(18))