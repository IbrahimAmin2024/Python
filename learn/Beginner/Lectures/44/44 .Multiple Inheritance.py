# muliple inheritance = when a child class is derived from more
#                       than one parent class
#class Grand_Father(): Parent class
#class Father(): Parent class
#class Son_1(Father): child class
#class Son_2(Grand_Father): child class
#class Son_3(Grand_Father, Father): child
class Grand_Father(): #Parent class
    def level(self):
        print("Grand-Father")
    def appearance_1(self):
        print("Very Tall")
class Father(): #Parent class
    def level0(self):
        print("Father")
    def appearance_2(self):
        print("Very Thin")
class Son_1(Grand_Father):  # child class
    pass
class Son_2(Father):  # child class
    pass
class Son_3(Grand_Father,Father):  # child class for multiple inheritance
    pass
grand_father = Grand_Father()
father = Father()
son_1 = Son_1()
son_2 = Son_2()
son_3 = Son_3()
# grand_father.level()
# grand_father.appearance_1()
# father.level()
# father.appearance_2()
# son_1.level()
# son_1.appearance_1()
# son_2.level()
# son_2.appearance_2()
son_3.level()
son_3.level0()
son_3.appearance_1()
son_3.appearance_2()