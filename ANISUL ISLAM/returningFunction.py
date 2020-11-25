def add(a, b):
    total = a + b
    return total

def bigger(x, y):
    if x > y:
        return x
    else:
        return y

larger = bigger

print(add(20, 30))
# print(bigger(7, 6))
print(larger(20, 90))