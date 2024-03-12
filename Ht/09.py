import math
from file_for_import import Point

class Circle(Point):

    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius

    def __str__(self):
        return f'Circle(x = {self.x}, y = {self.y}, radius = {self.radius})'

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __sub__(self, other):
        if isinstance(other, Circle):
            new_x = self.x
            new_y = self.y
            new_radius = abs(self.radius - other.radius)
            return Circle(new_x, new_y, new_radius)

r_1 = Circle()
r_2 = Circle(1, 3, 2)
r_3 = Circle(1, 3, 5)

print(r_1)
print(r_2)
print(r_3)

print(r_1.area())
print(r_2.area())
print(r_3.area())

print(r_1.circumference())
print(r_2.circumference())
print(r_3.circumference())

result = r_3 - r_2
print("Result of subtraction:", result)
