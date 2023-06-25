class Rectangle:
    def _init_(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Rectangle:")
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())


class Parallelepipede(Rectangle):
    def _init_(self, length, width, height):
        super()._init_(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def display(self):
        super().display()
        print("Height:", self.height)
    …