def square(x):
    return x*x

num = [1, 2, 3, 4, 5]

print(list(map(square, num)))
print(list(filter(lambda x : x % 2 == 0, num))) # You can use name function

# Comprehensive List
print([x*x for x in num]) # Comprehensive Map

print([x for x in num if x%2==0]) # Comprehensive filter