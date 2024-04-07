# duck Typing

class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is qwuacking")
class Chicken:
    def walk(self):
        print("This chicken is walking")
    def talk(self):
        print("This chicken is clucking")
class Person:
    def catch(self,catching):
        catching.walk()
        catching.talk()
        print("this caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()
# person.catch(chicken)
# person.catch(duck)
