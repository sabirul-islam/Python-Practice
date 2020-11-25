studentId = {
    101 : 'sabirul',
    '102' : 'shimul',
    103 : 'shumit'
}

print(studentId.get(101))
print(studentId.get(106, 'Not a valid key'))
print(studentId[103])