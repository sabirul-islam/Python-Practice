import re
# pattern = r'[aeiou]' # all at first
# pattern = r'[a-z]' # all at first
# pattern = r'[A-Z]' # all at first
pattern = r'[A-Z][a-z][0-9]' # all at first

if re.match(pattern,'Kc3iXAdsfhghjgk8hkjdfZ'):
    print('Matched')
else:
    print('Not Matched')