# map() = applies a function to each item in an iterable (list,tuple,etc..)
# map(function,iterable)

Zara_USD = [
    ("Shirt",20.00),  #USD
    ("Pants",25.00),  #USD
    ("Jacket",50.00), #USD
    ("Socks",10.00)   #USD
]#0.94

#Points = lambda Point:Point[2]
#function object
to_euro = lambda index: (index[0],index[1]*0.94)

Zara_Euro = list(map(to_euro,Zara_USD))

for i in Zara_Euro:
    print(i)