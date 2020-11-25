# n = input('Enter some number : ')

# listNumber = n.split()

# total = 0

# for i in listNumber:
#     total = total + int(i)
# print(total)

numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input('Enter Your Text : ')

for i in text:
    i = i.lower()
    if i >= 'a' and i <= 'z':
        numOfLetters = numOfLetters + 1
    elif i >= '0' and i <= '9':
        numOfDigits = numOfDigits + 1
    elif i >= ' ':
        numOfWords = numOfWords + 1

print('Number Of Digits : ', numOfDigits)
print('Number Of Letters : ', numOfLetters)
print('Number Of Words : ', numOfWords + 1)