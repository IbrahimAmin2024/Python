# **kwargs = parameter that will pack all argument into a dictionary [] .item/ key : value
#                     useful so that a function can accept a varying amount of keyword arguments

def My_Full_name(**kwargs):
    # hello my name is Ibrahim Ahmed Amen
    kwargs['last_last'] = "3kl"
    
    print("hello my name is " + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'])
    for key,value in kwargs.items():
        print(key,value, end=" ")


My_Full_name(first='Ibrahim',last="Amen",middle="Ahmad")