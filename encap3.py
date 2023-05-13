class Hobbit:
    def __init__(self, name):
        self.name = name


    def introduce(self):
        print("Hello, my name is", self.name)
        self.__hobby()

    def __hobby(self):
        print(f"My hobby is gardening and eating")


hobbit1 = Hobbit("Samwise Gamgee")
hobbit1.introduce()