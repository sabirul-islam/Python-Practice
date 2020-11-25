# LIFO = Last In First Out

books = []

books.append('c')
books.append('c++')
books.append('c#')
print(books)

books.pop()
print(books)
print('Now the first book is: ', books[-1])

books.pop()
print(books)
print('Now the first book is: ', books[-1])

books.pop()
if not books:
    print('No books left')