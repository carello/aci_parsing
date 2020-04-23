""" My new app
    gonna make a lot of $$$
"""
import math

# inherit from object to get additional features
class Circle(object):
    """ an advanced toolkit """
    version = '0.2'

    def __init__(self, radius):
        self.radius = radius

    # this is cool! do this so you don't expose radius init variable
    # is run after radius and updates your code!!!
    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

    @staticmethod
    def angle_to_grade(angle):
        return math.tan(math.radians(angle)) * 100.0

    def area(self):
        """ perform a quad """
        p = self.__perimeter()
        r = p / math.pi / 2.0
        return math.pi * r ** 2.0

    def perimeter(self):
        return 2.0 * math.pi * self.radius

    __perimeter = perimeter

    @classmethod
    def from_bbd(cls, bbd):
        radius = bbd / 2.0 / math.sqrt(2.0)
        #return Circle(radius)
        return cls(radius)

class Tire(Circle):
    def perimeter(self):
        return Circle.perimeter(self) * 1.25


print(Circle.version)
c = Circle(10)
print(c.radius)
print(c.area())
print(c.perimeter())

t = Tire(22)
print(t.radius)
print(t.area())
print(t.perimeter())
print("--------")
print(c.angle_to_grade(10))
