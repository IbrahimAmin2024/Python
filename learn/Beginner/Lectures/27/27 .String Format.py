# {str}.format({name},{toy}) = optional method that gives users, more control when display output. {argument}
name = "Ibrahim"
toy = "Hours"
# print("Hello " + name + " playing with " + toy ) #hello Ibrahim playing with hours
# print("Hello {} playing with {}".format(name,toy))
# print("Hello {} Playing with {}".format(name,toy)) #first,second [values]
# print("Hello {} Playing with {}".format("Ahmad","Lion")) #Positional argument : very important
# print("Hello {1} Playing with {0}".format("Ibrahim","Hours")) #Positional argument : can customer
# print("Hello {name} Playing with {toy}".format(name="Ahmad",toy="lion")) #Keyword argument
# test_2 = ("i'am {} and i playing with {}") #tuples
# print(test_2.format(name,toy))
#allocated Spaces Between /before/after Argument
# test_2 = ("i'am {} and i playing with {:10}. Thanks") #:10 making 10 spaces after sec argument
# print(test_2.format(name,toy))

# test_3 = ("i'am {} and i playing with {:<10}. Thanks") #:<10 making 10 spaces After sec argument
# test_4 = ("i'am {} and i playing with {:>10}. Thanks") #:>10 making 10 spaces Before sec argument
# test_5 = ("i'am {} and i playing with {:^10}. Thanks") #:>10 making 10 spaces align{before+after} argument
# test_6 = ("i'am {} and i playing with {:10}. Thanks") #:>10 making 10 spaces align{before+after} argument
# print(test_6.format(name,toy))

# .2f,.3f Grabing only (2,3) num after decimal portion = 0.12 , 0.123
# test_7 = 3.9825 #decimal portion
# print("The number without Decimal Portion is : {:.5f}" .format(test_7)) #3.98

test_8 = 1000
print("Number with comma : {:,}".format(test_8))  # 1,000
print("Number with comma : {:X}".format(test_8))  # 3E8
print("Number with comma : {:e}".format(test_8))  # e : lower, E : upper



