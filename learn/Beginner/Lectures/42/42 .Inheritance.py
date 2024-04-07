# inheritance

class Animal: #parent class

    alive = True

    def eat(self):
        print("This animal is eating")

    def slumber(self):
        print("This animal is sleeping")

class Rabbit(Animal): #Child class of Animal

    def run(self):
        print("This rabbit is running")

class Fish(Animal): #Child class of Animal
    def swim(self):
        print("this fish is swimming")


class Hawk(Animal): #Child class of Animal

    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

# print(rabbit.alive)
# fish.eat()
# hawk.slumber()

rabbit.run()
fish.swim()
hawk.fly()

##########
# inheritance

class Grand_father: # parent class

    def tall(self):
        print("Im very tall")

    def fat(self):
        print("im very fat")

    def lazzy(self):
        print("Im soo lazy")

    def status(self):
        print("im being soo mad, grand")

class Father(Grand_father): # child class

    def status(self):
        print("im being soo mad, father")

class Uncle(Grand_father): # child class

    def appearance(self):
        print("inheritance his appearance")


father = Father()
uncle = Uncle()

# father.tall()
# father.lazzy()
# father.fat()
#
# uncle.tall()
# uncle.lazzy()
# uncle.fat()

Grand_father().status()
