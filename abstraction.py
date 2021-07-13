class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side


myShape = Shape()
