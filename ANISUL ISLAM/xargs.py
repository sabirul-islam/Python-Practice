def student (*details): # receive any number of arguments
    print(details)
    # print(details[1])

student(101, 'shimul', 4.00)

def add(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print(sum)

add(10, 20, 30, 40)

# xxargs
def studentDetails(**details): # receive any number of arguments with key value like as dictionary
    print(details)
    # print(details['name'])


studentDetails(id=101, name='shimul')