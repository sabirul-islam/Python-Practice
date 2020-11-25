subjects = ['javascript', 'python', 'php', 'java', 'flutter', 'kotlin']
print(subjects)
print(subjects[1])
print(subjects[2:]) # print from 2 number index
print(subjects[-1])
print('python' in subjects) # check is this subject in here?(case sensitive)
print('golang' not in subjects) # it returns true
print(subjects + ['xamarin', 45]) # add new list
print(subjects * 3) # showing this list 3 times
print(len(subjects)) # showing length and count from 1
subjects.append('c++') # insrt a item
print(subjects)
subjects.insert(2, 'c') # insert a new item in a specific location
print(subjects)
subjects.remove('kotlin') # remove a item
print(subjects)
subjects.sort() # sort the list alphabeticaly
print(subjects)
subjects.reverse()
print(subjects)
subjects.pop() # remove the last item
print(subjects)
subjects.clear() # clear all the item
print(subjects)
subjectsCopy = subjects.copy() # copy old list in a new list
print(subjectsCopy)
subjectsIndex = subjects.index('java') # showing index of an item
print(subjectsIndex)
subjectsCount = subjects.count('kotlin') # an item how many times have in the list
print(subjectsCount)