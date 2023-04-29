class Table:
    def __init__(self, l, w, h):
        self.long = l
        self.width = w
        self.height = h

    def outing(self):
        print(self.long, self.width, self.height)


class Kitchen(Table):

    def __init__(self, l, w, h):
        super().__init__(l, w, h)
        self.places = None

    def how_places(self, n):
        if n < 2:
            print("It is not kitchen table")
        else:
            self.places = n

    def out_places(self):
        print(self.places)


class Work(Table):

    def is_comfy_for_work(self):
        if 80 >= self.height >= 70:
            print("This is a good height")
        else:
            print("This is an uncomfy height")

    def is_square(self):
        if self.long == self.width:
            print("is sqaure")
        else:
            print("not square")
            