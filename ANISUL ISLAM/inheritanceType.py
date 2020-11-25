# Type Of Inheritance
# 1. Heirarchical 2. Multi-level 3. Multiple

# Multi-Level Inheritance Example
class a:
    def display1(self):
        print('I am inside a class')
class b(a):
    def display2(self):
        print('I am inside b class')
class c(b):
    def display3(self):
        # super().display1()
        # super().display2()
        print('I am inside c class')

object = c()
object.display1()
object.display2()
object.display3()

# Multiple Inheritance Example
class x:
    def display(self):
        print('I am inside x class')
class y:
    def display(self):
        print('I am inside y class')
class z(y,x): # if x remain before y, it shows x result first 
    pass

obj = z()
obj.display()