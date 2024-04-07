# *args = parameter that will pack all argument into a tuple ()
#                     useful so that a function can accept a varying amount of arguments

def Adding(*Adding): # {*Adding = (1,2,3,4,5,6) } List convert = list(Adding) > [1,2,3,4,5,6] >
    Result = 0
    Adding = list(Adding) #[1,2,3,4,5,6]
    Adding[0] = 0 #[0,2,3,4,5,6]

    for i in Adding:
        Result += i #Result = 0 | result = result + 0 | result = result + 2 | result = result + 3...etc

    return Result


print(Adding(1,2,3,4,5,6)) #21 => 20  | Adding(1,2,3,4,5,6) = return result = 20
