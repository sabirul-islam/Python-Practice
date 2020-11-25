num1 = {1, 2, 3, 4, 5}
print(num1)
print(2 in num1) # display true or false value

num2 = {1, 2, 3, 4, 5, 5, 3} # it does not print duplicate value
print(num2)
print(6 in num2)

num3 = set([4, 5, 8])
num3.add(6)
num3.remove(8)
print(num3)
print(4 not in num3)
print(9 not in num3)

num4 = {1, 2, 3, 4, 5}
num5 = {4, 5, 6, 7, 8}

print(num4 | num5) # Union
print(num4 & num5) # intersection
print(num4 - num5) # difference