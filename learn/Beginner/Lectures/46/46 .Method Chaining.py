# method chaining = calling multiple methods sequentially each call performs
#                   an action on the same object and return self

class Family:

    def Grand_Father(self):
        print("1st")
        return self

    def Father(self):
        print("2nd")
        return self

    def Son(self):
        print("3rd")


# family = Family()
# family.Grand_Father().Father()
#
# family.Grand_Father()
# family.Father()

# family\
#     .Grand_Father()\
#     .Father()