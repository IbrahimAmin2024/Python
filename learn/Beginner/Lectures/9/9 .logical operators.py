#logical operators (and,or,not) = used to check if two or more conditional statment is true

temp = int(input("what is the temperature outside? :")) #int #temperature

if (temp >= 0) and (temp <= 30):
    print("the temp is good today")
    print("u can go outside, if u want")
elif( (temp < 0) or (temp > 30) ): # -0 | 30
    print("the temp is bad today")
    print("stay inside,")


if not (temp>= 0): # -0
    #ture