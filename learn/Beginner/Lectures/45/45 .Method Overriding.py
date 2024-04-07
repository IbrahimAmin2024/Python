#overriding method = getting the priority of called method.

class Grand_Father: #parent

    def tall1(self):
        print("Im very tall1")

class Father(Grand_Father):  # child

    def tall2(self):
        print("Im very tall2")

father = Father()
father.tall1()
father.tall2()