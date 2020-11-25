class triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def areaCalculation(self):
        print(f'Area = {.5 * self.base * self.height}')


t1 = triangle(10, 20)
t1.areaCalculation()
t2 = triangle(20, 30)
t2.areaCalculation()