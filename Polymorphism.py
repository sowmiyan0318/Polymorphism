# Define a base class called "Shape"
class Shape:
    def area(self):
        pass

# Define a subclass called "Circle" that inherits from "Shape"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

# Define another subclass called "Rectangle" that inherits from "Shape"
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Create objects of Circle and Rectangle
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Use polymorphism to calculate the area of each shape
shapes = [circle, rectangle]

for shape in shapes:
    print(f"The area of the {type(shape).__name__} is {shape.area()}")
