from abc import ABC, abstractmethod
class shape(ABC):
    def __init__(self, dimension1, dimension2):
        self.dimension1 = dimension1
        self.dimension2 = dimension2

    @abstractmethod
    def area(self):
        pass

class triangle(shape):
    def area(self):
        triangle = (self.dimension1 * self.dimension2) / 2
        print(triangle)

class rectangle(shape):
    def area(self):
        area = self.dimension1 * self.dimension2
        print(area)

t = triangle(20, 30)
t.area()
r = rectangle(10, 20)
r.area()
