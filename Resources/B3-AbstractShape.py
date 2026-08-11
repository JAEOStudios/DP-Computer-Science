from abc import ABC, abstractmethod
import math
#abstract shape class
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return math.pi * self.radius ** 2
    def get_perimeter(self):
        return 2 * math.pi * self.radius


shapes = [
    Rectangle(10, 4),
    Rectangle(36, 7),
    Circle(42),
    Circle(5)
]

for i in range(len(shapes)):
    print(shapes[i].get_area())
    print(shapes[i].get_perimeter())