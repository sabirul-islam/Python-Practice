array = [10, 20, 30, 40, 50]

n = len(array)
i = 0
sum = 0
while i < n:
    print(array[i])
    sum = array[i] + sum
    print(sum)
    i = i + 1 

for i in array:
    print (i)

sum = 0
for i in array:
    sum = sum + i
print(sum)