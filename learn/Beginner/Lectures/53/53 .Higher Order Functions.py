# Higher Order Function = a function that either :
#                         1. accepts a function as an argument
# or
#                         2. returns a function
#                          (as in python, functions are also treaded as objects)

def lowe_case(text):
    return text.lower()

def upper_case(text):
    return text.upper()

def my_text(value):
    print(value("HELOO"))


# print(lowe_case("HELOO"))
# print(upper_case("Hello"))
# my_text(lowe_case)

#5 / 2 = 2.5
#10 / 2 = 5

def divisor(first):
    def dividend(second):
        return first / second
    return dividend

# divide = divisor(5)
# print(divide(2))

# print(divisor(10)(2))
