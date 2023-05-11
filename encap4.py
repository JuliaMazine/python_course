class Hobbit:
    def __init__(self, name, height):
        self.__name = name
        self.__height = height

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_height):
        if new_height <= 1.2:
            self.__height = new_height
        else:
            print("This is too tall for a hobbit!")

