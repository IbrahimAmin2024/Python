# Prevents a user from creatinng an object of that class
# + compels a user to ovverride abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation
# abstract based class

from abc import ABC, abstractmethod
class Grand_Father(ABC): #Parent class

    @abstractmethod
    def name1(self):
        print("My name is Amin")

class Father(Grand_Father):#child class

    def name2(self):
        print("My name is Ahmad")

class Son(Grand_Father):#child class

    def name3(self):
        print("My name is Ibrahim")

grand_father = Grand_Father()
father = Father()
son = Son()

son.name3()
son.name1()
