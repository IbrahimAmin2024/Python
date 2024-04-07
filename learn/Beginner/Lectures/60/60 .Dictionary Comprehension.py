# dictionary comprehension = create dictionaries using an expression
# can can replace for loops and lambda functions

# dictionary = {Key: expression for (key,value) in iterable}
# dictionary = {Key: expression for (key,value) in iterable use if conditional}
# dictionary = {Key: (if/else) for (key,value) in iterable}
# dictionary = {Key: function(value) for {key,value} in iterable}

# value * (5/9)
# cities_in_f = {"New York":32, "Cairo":35, "Boston": 75, "Los Angeles":100}
# cities_in_c = {key: round(value * (5/9)) for(key,value) in cities_in_f.items()}

# for (key,value) in cities_in_f.items():
#     cities_in_c[key] = round(value * (5/9))
# print(cities_in_c)
#=================
# weather = {"New York":"snowing", "Cairo":"sunny", "Boston": "sunny", "Los Angeles":"snowing"}
# sunny_weather = {key: value for(key,value) in weather.items() if value == "snowing"}
# print(sunny_weather)
#=================
# cities = {"New York":32, "Cairo":35, "Boston": 75, "Los Angeles":50}
# desc_cities = {key: ("Warm" if value >= 40 else "Cold") for(key,value) in cities.items()}
# print(desc_cities)
#=================

# def Check_Temp(value):
#     if value >= 70:
#         return "Hot"
#     elif(69 >= value >= 40):
#         return "Warm"
#     else:
#         return "Cold"
# 
# 
# cities = {"New York":32, "Cairo":35, "Boston": 75, "Los Angeles":50}
# desc_cities = {key: Check_Temp(value) for(key,value) in cities.items()}
# print(desc_cities)
