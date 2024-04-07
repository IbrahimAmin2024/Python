from car import Car

#car,model,year,color
#car_1 = Car()
#car_2 = Car()
car_1 = Car("BMW","X3",2010,"Black")
car_2 = Car("Mazda","Mi",2012,"White")

# car_1.wheels = 1
# car_2.wheels = 2

Car.wheels = 4

print(car_1.wheels)
print(car_2.wheels)
# print(Car.wheels)


####

class Car:
    wheels = 5 #defult variable.

    # car,model,year,color
    def __init__(self,car,model,year,color): # Constructor will be called.
        # instance variable
        self.car = car
        self.model = model
        self.year = year
        self.color = color



