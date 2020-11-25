# r = readable, w = writable, r+ = readable and writable
file = open('student.txt', 'r+')
# print(file.writable()) # readable / writable
# text = file.read()
# print(text)
# print(len(text))

# text2 = file.readlines()
# text2 = file.readlines()[1]
# print(text2)

for line in file:
    print(line)

file.close()