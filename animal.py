
class Animal:

    def __init__(self,color,type):
        self.color = color
        self.type = type

    def animalinfo(self):
        print(f"Type is {self.type} and Colour is {self.color}")

animal = Animal("Balck and white", "Border collie")

animal.animalinfo()
