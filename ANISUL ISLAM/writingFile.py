# a = adding a new line, w = it will do overwrite
text = open('student.txt', 'a')
# text = open('student.html', 'a')
# text = open('student1.txt', 'a') # create a new document
text.write('\nDhaka, Bangladesh.')
# text.write('<h1> Good Student </h1>')
text.close()