class Figure:
    def __init__(self):
        self.color = "white"

    def change_color(self, new_color):
        self.color = new_color

    def print_info(self):
        pass


class Oval(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print(f'Oval, color: {self.color}, width: {self.width}, height: {self.height}')


class Square(Figure):
    def __init__(self, side_length):
        self.side_length = side_length

    def print_info(self):
        print(f'Square, color: {self.color}, side length: {self.side_length}')


oval = Oval(10, 20)
square = Square(15)

oval.print_info()
square.print_info()

oval.change_color('red')
square.change_color('blue')

oval.print_info()
square.print_info()