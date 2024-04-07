# objects as arguments : passing an object as argument
class Car:
    color = None
class Motorcycle:
    color = None
def change_color(vehicle,color):
    vehicle.color = color
car_1 = Car()
car_2 = Car()
car_3 = Car()
motor_bike = Motorcycle()

change_color(car_1,"Red")
change_color(car_2,"Blue")
change_color(car_3,"White")
change_color(motor_bike,"Yellow")
print(car_1.color)
print(car_2.color)
print(car_3.color)
print(motor_bike.color)