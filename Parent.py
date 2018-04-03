class Parent :
    def __init__(self,firstName,eyeColor):
        self.firstName=firstName
        self.eyeColor=eyeColor
        print("Contructor Parent")

    def showInfo(self):
        print("FirstName "+self.firstName)
        print("Eve Color " +self.eyeColor)

class Child(Parent) :
    def __init__(self,firstName,eyeColor,noOfToys):
        print("Child Contructor")
        Parent.__init__(self,firstName,eyeColor)
        self.noOfToys=noOfToys

    def showInfo(self):
        # print("Name ",self.firstName)
        # print("Color ",self.eyeColor)
        Parent.showInfo(self)
        print("Toys ",str(self.noOfToys))

cyrus=Parent("cyrus","blue")
print(cyrus.showInfo())

nidhish=Child("nidhish","black",5)
print(nidhish.showInfo())
# print(nidhish.noOfToys)