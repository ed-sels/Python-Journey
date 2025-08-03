class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print("Subclasses must implement this method")
    
class Circle(Shape):
    def __init__(self, r, pi=3.14):
        super().__init__("Circle")
        self.r = r
        self.pi = pi

    def area(self):
        return self.pi * (self.r ** 2)
    
class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__("Rectangle")
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

shapes = [Circle(5),Rectangle(4, 6),
    Circle(2),Rectangle(3, 7)]

for shape in shapes:
    print(f"{shape.name} area:", shape.area())