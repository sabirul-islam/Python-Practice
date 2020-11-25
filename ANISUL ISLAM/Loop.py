# While Loop
i = 1
while i <= 10:
    print(i)
    i = i + 1

# Even Number
i = 2
while i <= 10:
    print(i)
    i = i + 2

# Odd Number
i = 1
while i <= 10:
    print(i)
    i = i + 2

# Total
n = int(input('Enter the number : '))
sum = 0
i = 1
while i <= n:
    sum = sum + i
    i = i + 1
print(sum)

# Break
i = 1
while i <= 100:
    if i == 20:
        break
    print(i)
    i = i + 1

# Continue
i = 1
while i <= 100:
    if i == 20:
        continue
    print(i)
    i = i + 1