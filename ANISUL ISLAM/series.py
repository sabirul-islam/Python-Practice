n = int(input('Enter the last number : '))

# sum = 0
# multiplication = 1

# for i in range (1, n + 1, 1):
#     sum = sum + i
# print(sum)

# for i in range (2, n + 1, 2): # sum of even number
#     sum = sum + i
#     print (sum)

# for i in range (1, n + 1, 2):
#     sum = sum + i
# print(sum)

# for i in range (1, n + 1, 1):
    # sum = sum + i * i
# print(i)

# for i in range (1, n + 1, 1):
#     sum = sum + (1 / i)
#     print(sum)

# for i in range (1, n + 1, 1):
#     multiplication = multiplication * i
#     print(multiplication)

for i in range(2, n, 1):
    if n % i == 0:
        print('not a prime number')
        break
else:
    print('is a prime number')