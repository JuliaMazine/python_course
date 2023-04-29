class Shape:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def info(self):
        print(f"This is a {self.size} {self.color} shape.")


class Circle(Shape):
    def __init__(self, color, size, radius):
        super().__init__(color, size)
        self.radius = radius

    def info(self):
        print(f"This is a {self.size} {self.color} circle with a radius of {self.radius} cm.")


class Square(Shape):
    def __init__(self, color, size, length):
        super().__init__(color, size)
        self.length = length

    def info(self):
        print(f"This is a {self.size} {self.color} square with a length of {self.length} cm.")


class Box:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        if isinstance(shape, Shape):
            self.shapes.append(shape)
        else:
            print("Invalid shape.")

    def show_contents(self):
        for shape in self.shapes:
            shape.info()


circle1 = Circle("red", "small", 5)
square1 = Square("blue", "medium", 3)
circle2 = Circle("green", "large", 10)
triangle1 = "invalid shape"

box1 = Box()
box1.add_shape(circle1)
box1.add_shape(square1)
box1.add_shape(circle2)
box1.add_shape(triangle1)

box1.show_contents()