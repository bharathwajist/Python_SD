class Dog:
    # Variable attributes
    attr1 = "mammal"
    attr2 = "dog"

    # Method attribute
    # In python "self" keyword works as this to access class local attributes 
    def fun(self):
        # print("Class Attribute : ", self.attr1)
        # print("Class Attribute : ", self.attr2)
        pass

# Main 
if "__main__" == __name__:
    Rogger = Dog()

    print(Rogger.fun())
    # print(Rogger.fun)