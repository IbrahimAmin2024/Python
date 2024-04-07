# super() = Function used to give access to the methods of a parent class
#           Returns a temporary object of a parent class when used

class Grand_Father(): #parent

    def __init__(self,height,weight,age):
        self.height = height
        self.weight = weight
        self.age = age

    def useless(self):
        pass

    def Show_Result(self):
        return "Result of Grand-Father : [Height,Weight,Age]: [" + str(self.height) + "," + str(self.weight) + "," + str(self.age) + "]"


class Father(Grand_Father):

    def __init__(self, height, weight, age):
        super().__init__(height,weight,age)
        # self.height = height
        # self.weight = weight
        # self.age = age

    def Show_Result(self):
        return "Result of Father : [Height,Weight,Age]: [" + str(self.height) + "," + str(self.weight) + "," + str(self.age) + "]"


class Son(Grand_Father):
    def __init__(self, height, weight, age):
        super().__init__(height,weight,age)

    def Show_Result(self):
        return "Result of Son : [Height,Weight,Age]: [" + str(self.height) + "," + str(self.weight) + "," + str(self.age) + "]"



#Result of *** : [height,weight,age] : []:

grand_father = Grand_Father(180,45,60)
father = Father(180,80,40)
son = Son(180,70,22)

print(father.Show_Result())
print(son.Show_Result())
print(grand_father.Show_Result())