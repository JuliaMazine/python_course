class Hobbit:
    def __init__(self, name, age):
        self.name = name
        self._age = age
        self.__address = "The Shire"

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        self.__address = new_address

hobbit = Hobbit("Bilbo", 111)
print(hobbit.name)
print(hobbit._age)

print(hobbit.__address)

print(hobbit.get_address())

hobbit.set_address("Rivendell")
print(hobbit.get_address())

print(hobbit._Hobbit__address)