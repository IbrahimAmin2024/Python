# Walrus Operator :=

# assignment expression walrus operator
# assigns values to variables as part of a larger expression

# am_i_lazy = False
# print(am_i_lazy:=True)

foods = list()
# while True:
#     food = input("what food do u like?! : ")
#     if food == "Exit".lower():
#         print(foods)
#         break
#     foods.append(food)

while food := input("what food do u like?! : ") != "Exit".lower():
    foods.append(food)


