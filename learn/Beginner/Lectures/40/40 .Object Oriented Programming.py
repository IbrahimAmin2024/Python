class Bike():
    # Constructor : assigned argument that we receive to our class object[runing,model,,,]

    def __init__(self,Running_status,Color,Model):
        self.status = Running_status
        self.color = Color
        self.model = Model


    def ride_a_bike(self): # self refers to object that use this method
        # Red, New Model, Status : True
        print("i ride this bike, " + self.color + ", " + self.model + ", Status : " + str(self.status))

    def stop_cycling(self):
        print("i stoped cycling my bike")

#=============
# PooP : Python Object Oriented Programming
# Object : we need create a class
# Class : will decribe what attributes {name,age,...} , and methods,
#         that will create your class within your main module[main.py].
#         or use a separate file solely for your class

# important if u have short class codes u can write it within your main module
# else [] long code make a separate module [new file]

#send argument from main module to class


#main module

from bike import Bike

# bike_1 = Bike()
bike_1 = Bike(True,"Blue","New Model")
bike_2 = Bike(False,"Red","old Model")

bike_1.ride_a_bike()
bike_2.ride_a_bike()

#Running_status
#Color
#Model