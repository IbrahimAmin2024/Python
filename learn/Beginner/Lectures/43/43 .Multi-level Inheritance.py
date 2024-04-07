# multi-level inheritance = when a derived (child) class inherits another
# derived (child) class


class Organism: #parent class

    alive = True

class Animal(Organism): #Child class of Animal

    def eat(self):
        print("This animal is eating")

class Dog(Animal): #Child class of Animal

    def bark(self):
        print("this dog is barking")



# print(rabbit.alive)
# fish.eat()
# hawk.slumber()

dog = Dog()
print(dog.alive)
print(dog.eat())
print(dog.bark())


