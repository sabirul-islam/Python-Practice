# function is two type
# 1. library 2. user defined

def add(x, y):
    total = x + y
    print(total)

def addition(a, b, c):
    total = a + b + c
    print(total)

def sub (p, q):
    total = p - q
    print(total)

def message():
    print('No Parameter')

add(10, 20)
sub(20, 10)
addition(40, 50, 60)
message()