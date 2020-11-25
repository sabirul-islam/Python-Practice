class shape:
    def __init__(self, dimension1, dimension2):
        self.dimension1 = dimension1
        self.dimension2 = dimension2

    def area(self):
        print('I am area method of shape class.')

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

