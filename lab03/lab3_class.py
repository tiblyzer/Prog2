import math

class Circle:
    def __init__(self,r=1):
        self.__radius = r

    def area(self):
        return self.__radius**2*math.pi

    def perimeter(self):
        return self.__radius*2*math.pi

    def getRadius(self):
        return self.__radius

    def setRadius(self,r=1):
        self.__radius = r

    def __add__(self,other):
        return self.perimeter() + other.perimeter()

c1 = Circle()
c2 = Circle()
c1.setRadius(3)
print(c1.getRadius())
c1.setRadius()
print(c1.getRadius())

print(c1.area())
print(c1.perimeter())

print(c1 + c2)